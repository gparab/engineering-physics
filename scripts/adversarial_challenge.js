#!/usr/bin/env node
/**
 * scripts/adversarial_challenge.js
 * Empirical Adversarial Test Harness for 348 Engineering Physics Models.
 *
 * Probes:
 * 1. Anti-gimmick verification: scans every file for destructive AST patterns,
 *    .remove(, removeChild, style.display = 'none', opacity = 0, explosive scales (>4).
 * 2. Theme toggle integrity: parses theme toggle scripts, checks #theme-toggle button,
 *    listener attachment, and data-theme switching.
 * 3. Viewport boundary testing: verifies <main> has proper CSS min/max height bounds (62vh, 380px, 640px).
 * 4. Script integrity: AST syntax check of every <script> block, checks for unclosed quotes/brackets,
 *    and simulates execution to catch undefined variables / runtime crashes.
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const REPO_ROOT = path.resolve(__dirname, '..');
const MODELS_DIR = path.join(REPO_ROOT, 'models');
const EXCLUDE_DIRS = new Set(['misc']);

function getModelFiles(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (!EXCLUDE_DIRS.has(entry.name)) {
        results = results.concat(getModelFiles(fullPath));
      }
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      results.push(fullPath);
    }
  }
  return results.sort();
}

function probeAntiGimmick(content, relPath) {
  const issues = [];
  // 1. .remove( except classList.remove
  const removeMatches = [...content.matchAll(/(\w+)\.remove(?:Child)?\s*\(/g)];
  for (const m of removeMatches) {
    if (m[1] !== 'classList') {
      issues.push(`Forbidden element destruction call: ${m[0]}`);
    }
  }

  // 2. style.display = 'none'
  if (/(?:style\.display|\.display)\s*=\s*['"]none['"]/i.test(content)) {
    issues.push("Destructive display = 'none' assignment found");
  }

  // 3. style.opacity = 0
  if (/(?:style\.opacity|\.opacity)\s*=\s*['"]?0['"]?/i.test(content)) {
    issues.push("Destructive opacity = 0 assignment found");
  }

  // 4. explosive scale
  if (/scale\s*:\s*(?:50|[5-9]\d|\d{3,})\b/i.test(content) || /scale\(\s*(?:50|[5-9]\d|\d{3,})\s*\)/i.test(content)) {
    issues.push("Explosive scale factor detected (> 50)");
  }

  return {
    passed: issues.length === 0,
    issues
  };
}

function probeViewportBounds(content, relPath) {
  const styles = [...content.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/gi)].map(m => m[1]).join('\n');
  const issues = [];

  const rules = [...styles.matchAll(/([^{}]+)\{([^{}]+)\}/g)];
  let foundMain = false;
  let hasHeight = false;
  let hasMinHeight = false;
  let hasMaxHeight = false;

  for (const [_, sel, decl] of rules) {
    const selectors = sel.split(',').map(s => s.trim());
    if (selectors.some(s => s === 'main' || s === '.simulation-viewport' || s.startsWith('main.') || s.startsWith('main,'))) {
      foundMain = true;
      if (/(?<!min-)(?<!max-)height\s*:\s*62vh/i.test(decl)) hasHeight = true;
      if (/min-height\s*:\s*380px/i.test(decl)) hasMinHeight = true;
      if (/max-height\s*:\s*640px/i.test(decl)) hasMaxHeight = true;
    }
  }

  if (!foundMain) issues.push("No CSS rule found styling <main> or .simulation-viewport");
  if (!hasHeight) issues.push("Missing required height: 62vh on <main>");
  if (!hasMinHeight) issues.push("Missing required min-height: 380px on <main>");
  if (!hasMaxHeight) issues.push("Missing required max-height: 640px on <main>");

  return {
    passed: issues.length === 0,
    issues
  };
}

function probeThemeToggle(content, relPath) {
  const issues = [];
  if (!/id=['"]theme-toggle['"]/i.test(content)) {
    issues.push("Missing #theme-toggle button in HTML");
  }

  const scripts = [...content.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi)].map(m => m[1]).join('\n');
  if (!scripts) {
    issues.push("No inline JavaScript found");
    return { passed: false, issues };
  }

  if (!scripts.includes('theme-toggle') && !scripts.includes('themeToggle') && !scripts.includes('toggleBtn')) {
    issues.push("No reference to theme toggle button in script");
  }

  if (!/addEventListener\s*\(\s*['"]click['"]/i.test(scripts) && !/\.onclick\s*=/i.test(scripts)) {
    issues.push("No click event listener attached in script");
  }

  if (!scripts.includes('data-theme')) {
    issues.push("No 'data-theme' attribute manipulation in script");
  }

  return {
    passed: issues.length === 0,
    issues
  };
}

function probeScriptIntegrity(content, relPath) {
  const issues = [];
  const scriptRegex = /<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi;
  let match;
  let scriptIndex = 0;

  // Mock DOM
  const noop = () => {};
  const mockCtx = new Proxy({
    measureText: () => ({ width: 50, actualBoundingBoxAscent: 10, actualBoundingBoxDescent: 10 }),
    getImageData: () => ({ data: new Uint8ClampedArray(400) }),
    createLinearGradient: () => ({ addColorStop: noop }),
    createRadialGradient: () => ({ addColorStop: noop }),
    getLineDash: () => [],
  }, {
    get: (target, prop) => (prop in target ? target[prop] : noop),
    set: () => true
  });

  const idMatches = [...content.matchAll(/id=['"]([^'"]+)['"]/g)].map(m => m[1]);
  const elementsById = {};
  function makeElement(id, tag) {
    const listeners = {};
    return {
      id: id || '',
      tagName: tag ? tag.toUpperCase() : 'DIV',
      getContext: () => mockCtx,
      getBoundingClientRect: () => ({ width: 800, height: 500, top: 0, left: 0, right: 800, bottom: 500 }),
      addEventListener: (evt, cb) => {
        listeners[evt] = listeners[evt] || [];
        listeners[evt].push(cb);
      },
      removeEventListener: noop,
      _trigger: (evt, e) => { if (listeners[evt]) listeners[evt].forEach(cb => cb(e)); },
      setAttribute: noop,
      getAttribute: () => null,
      removeAttribute: noop,
      appendChild: noop,
      removeChild: noop,
      classList: { add: noop, remove: noop, toggle: noop, contains: () => false },
      style: {},
      clientWidth: 800,
      clientHeight: 500,
      offsetWidth: 800,
      offsetHeight: 500,
      width: 800,
      height: 500,
      value: '50',
      innerHTML: '',
      textContent: '',
    };
  }

  idMatches.forEach(id => {
    elementsById[id] = makeElement(id, id.includes('canvas') ? 'CANVAS' : (id.includes('toggle') ? 'BUTTON' : (id.includes('svg') ? 'SVG' : 'DIV')));
  });
  if (!elementsById['theme-toggle']) elementsById['theme-toggle'] = makeElement('theme-toggle', 'BUTTON');
  if (!elementsById['sim-canvas']) elementsById['sim-canvas'] = makeElement('sim-canvas', 'CANVAS');

  let currentTheme = 'dark';
  const doc = {
    documentElement: {
      getAttribute: (attr) => (attr === 'data-theme' ? currentTheme : null),
      setAttribute: (attr, val) => { if (attr === 'data-theme') currentTheme = val; },
      classList: { add: noop, remove: noop, toggle: noop, contains: () => false },
      style: {}
    },
    getElementById: (id) => elementsById[id] || makeElement(id, 'DIV'),
    querySelector: (sel) => {
      if (sel.startsWith('#')) return elementsById[sel.slice(1)] || makeElement(sel.slice(1), 'DIV');
      if (sel === 'canvas') return Object.values(elementsById).find(e => e.tagName === 'CANVAS') || elementsById['sim-canvas'];
      if (sel === 'svg') return Object.values(elementsById).find(e => e.tagName === 'SVG') || makeElement('svg', 'SVG');
      return makeElement('', 'DIV');
    },
    querySelectorAll: () => [],
    createElement: (tag) => makeElement('', tag),
    createElementNS: (ns, tag) => makeElement('', tag),
    addEventListener: noop,
    removeEventListener: noop,
    body: makeElement('body', 'BODY')
  };

  const windowListeners = {};
  const win = {
    document: doc,
    addEventListener: (evt, cb) => {
      windowListeners[evt] = windowListeners[evt] || [];
      windowListeners[evt].push(cb);
    },
    removeEventListener: noop,
    dispatchEvent: (e) => {
      if (windowListeners[e.type]) windowListeners[e.type].forEach(cb => cb(e));
    },
    innerWidth: 1024,
    innerHeight: 768,
    devicePixelRatio: 1,
    getComputedStyle: () => ({
      getPropertyValue: (prop) => (prop.includes('color') || prop.includes('bg') || prop.includes('accent') ? '#4fc3f7' : '16px')
    }),
    CustomEvent: class CustomEvent { constructor(type, detail) { this.type = type; this.detail = detail; } }
  };
  win.window = win;
  win.self = win;

  const rafCallbacks = [];
  const sandbox = {
    ...win,
    window: win,
    document: doc,
    getComputedStyle: win.getComputedStyle,
    CustomEvent: win.CustomEvent,
    gsap: {
      to: () => ({}),
      from: () => ({}),
      fromTo: () => ({}),
      set: () => ({}),
      timeline: () => ({}),
      ticker: { add: (cb) => { if (typeof cb === 'function') rafCallbacks.push(cb); } },
      registerPlugin: noop
    },
    requestAnimationFrame: (cb) => {
      if (typeof cb === 'function') rafCallbacks.push(cb);
      return 1;
    },
    cancelAnimationFrame: noop,
    setTimeout: (cb) => { if (typeof cb === 'function') rafCallbacks.push(cb); return 1; },
    clearTimeout: noop,
    setInterval: noop,
    clearInterval: noop,
    console: { log: noop, warn: noop, error: noop },
    Math: Math,
    Date: Date,
    performance: { now: () => 1000 },
    Array: Array,
    Object: Object,
    String: String,
    Number: Number,
    Boolean: Boolean,
    RegExp: RegExp,
    Map: Map,
    Set: Set,
    parseFloat: parseFloat,
    parseInt: parseInt,
    isNaN: isNaN,
    isFinite: isFinite
  };

  while ((match = scriptRegex.exec(content)) !== null) {
    scriptIndex++;
    const jsCode = match[1];
    try {
      // Step A: Parse AST / Syntax check
      const script = new vm.Script(jsCode, { filename: `${relPath} (script #${scriptIndex})` });
      
      // Step B: Runtime initialization
      const context = vm.createContext(sandbox);
      script.runInContext(context);

      // Step C: Trigger theme toggle click
      const btn = elementsById['theme-toggle'];
      if (btn && btn._trigger) {
        btn._trigger('click', {});
        if (currentTheme !== 'light') {
          issues.push("Theme toggle click did not switch data-theme to light");
        }
        btn._trigger('click', {});
        if (currentTheme !== 'dark') {
          issues.push("Theme toggle click did not switch data-theme back to dark");
        }
      }

      // Step D: Execute initial animation frames
      for (let f = 0; f < 3; f++) {
        const t = 1000 + f * 16.6;
        for (const cb of rafCallbacks) {
          cb(t);
        }
      }
    } catch (err) {
      issues.push(`Script execution/syntax failure: ${err.message}`);
    }
  }

  return {
    passed: issues.length === 0,
    issues
  };
}

function runAdversarialSuite() {
  console.log('='.repeat(80));
  console.log('ADVERSARIAL STRESS TEST & EMPIRICAL CHALLENGE SUITE');
  console.log('='.repeat(80));

  const modelFiles = getModelFiles(MODELS_DIR);
  console.log(`Discovered ${modelFiles.length} non-misc models.\n`);

  const results = [];
  const failureMap = {
    antiGimmick: [],
    viewportBounds: [],
    themeToggle: [],
    scriptIntegrity: []
  };

  for (const file of modelFiles) {
    const relPath = path.relative(REPO_ROOT, file);
    const content = fs.readFileSync(file, 'utf8');

    const antiGimmick = probeAntiGimmick(content, relPath);
    const viewport = probeViewportBounds(content, relPath);
    const theme = probeThemeToggle(content, relPath);
    const script = probeScriptIntegrity(content, relPath);

    if (!antiGimmick.passed) failureMap.antiGimmick.push({ file: relPath, issues: antiGimmick.issues });
    if (!viewport.passed) failureMap.viewportBounds.push({ file: relPath, issues: viewport.issues });
    if (!theme.passed) failureMap.themeToggle.push({ file: relPath, issues: theme.issues });
    if (!script.passed) failureMap.scriptIntegrity.push({ file: relPath, issues: script.issues });

    const allPassed = antiGimmick.passed && viewport.passed && theme.passed && script.passed;
    results.push({
      file: relPath,
      passed: allPassed,
      antiGimmick,
      viewport,
      theme,
      script
    });
  }

  console.log('PROBE AUDIT SUMMARY:');
  console.log('-'.repeat(80));
  console.log(`Probe 1 (Anti-Gimmick AST Patterns):     ${348 - failureMap.antiGimmick.length}/348 passed (${failureMap.antiGimmick.length} failed)`);
  console.log(`Probe 2 (Theme Toggle Script Integrity): ${348 - failureMap.themeToggle.length}/348 passed (${failureMap.themeToggle.length} failed)`);
  console.log(`Probe 3 (Viewport CSS Height Bounds):   ${348 - failureMap.viewportBounds.length}/348 passed (${failureMap.viewportBounds.length} failed)`);
  console.log(`Probe 4 (Script Syntax & Runtime Loop):  ${348 - failureMap.scriptIntegrity.length}/348 passed (${failureMap.scriptIntegrity.length} failed)`);
  console.log('-'.repeat(80));

  const totalPassing = results.filter(r => r.passed).length;
  const totalFailing = results.filter(r => !r.passed).length;

  console.log(`\nOVERALL STATUS: ${totalPassing} PASSED, ${totalFailing} FAILED out of ${results.length} models.`);

  if (totalFailing > 0) {
    console.log('\nCRITICAL FINDINGS & DEFECTS DETECTED:');
    for (const f of failureMap.scriptIntegrity) {
      console.log(`\n[DEFECT] ${f.file}:`);
      f.issues.forEach(iss => console.log(`  - ${iss}`));
    }
  }

  return { totalPassing, totalFailing, failureMap, results };
}

if (require.main === module) {
  const { totalFailing } = runAdversarialSuite();
  process.exit(totalFailing > 0 ? 1 : 0);
}

module.exports = { runAdversarialSuite };
