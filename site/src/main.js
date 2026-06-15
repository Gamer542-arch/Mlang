import './style.css';

// ===== I18N TRANSLATIONS =====
const UI_STRINGS = {
  en: {
    langFlag: '🇬🇧', langNative: 'English',
    'Loading...': 'Loading documentation...',
    footer: 'MLang © 2026 — Built with 🔥',
    pageNotFound: 'Page Not Found',
    pageNotFoundDesc: 'The documentation page could not be loaded.',
    settings: 'Settings', langLabel: 'Language', themeLabel: 'Theme',
    themeDark: 'Dark', themeLight: 'Light',
  },
  pl: {
    langFlag: '🇵🇱', langNative: 'Polski',
    'Loading...': 'Ładowanie dokumentacji...',
    footer: 'MLang © 2026 — Stworzone z 🔥',
    pageNotFound: 'Nie znaleziono strony',
    pageNotFoundDesc: 'Nie udało się załadować strony.',
    settings: 'Ustawienia', langLabel: 'Język', themeLabel: 'Motyw',
    themeDark: 'Ciemny', themeLight: 'Jasny',
  },
  de: {
    langFlag: '🇩🇪', langNative: 'Deutsch',
    'Loading...': 'Dokumentation wird geladen...',
    footer: 'MLang © 2026',
    pageNotFound: 'Seite nicht gefunden',
    pageNotFoundDesc: 'Die Dokumentationsseite konnte nicht geladen werden.',
    settings: 'Einstellungen', langLabel: 'Sprache', themeLabel: 'Design',
    themeDark: 'Dunkel', themeLight: 'Hell',
  },
};

const LANG_LIST = [
  { code: 'en', flag: '🇬🇧', name: 'English' },
  { code: 'pl', flag: '🇵🇱', name: 'Polski' },
  { code: 'de', flag: '🇩🇪', name: 'Deutsch' },
];

// ===== PAGE MANIFEST =====
const PAGE_TITLES = {
  'Getting Started':     { en: 'Getting Started',  pl: 'Na początek',       de: 'Erste Schritte' },
  'Language':             { en: 'Language',          pl: 'Język',             de: 'Sprache' },
  'Minecraft API':       { en: 'Minecraft API',    pl: 'Minecraft API',     de: 'Minecraft API' },
  'Standard Library':    { en: 'Standard Library',  pl: 'Biblioteka Standardowa', de: 'Standardbibliothek' },
  'GUI System':          { en: 'GUI System',        pl: 'System GUI',        de: 'GUI-System' },
  'Tutorials':           { en: 'Tutorials',         pl: 'Poradniki',         de: 'Tutorials' },
  'Bridge':              { en: 'Bridge',            pl: 'Bridge',            de: 'Bridge' },
};

const PAGES = [
  { section: 'Getting Started', items: [
    'README.md', { en:'Overview', pl:'Przegląd', de:'Übersicht' },
    '05-tutorials/01-installation.md', { en:'Installation', pl:'Instalacja', de:'Installation' },
    '05-tutorials/02-first-script.md', { en:'First Script', pl:'Pierwszy skrypt', de:'Erstes Skript' },
    '08-roadmap.md', { en:'Roadmap', pl:'Mapa rozwoju', de:'Roadmap' },
  ]},
  { section: 'Language', items: [
    '01-language/01-syntax.md', { en:'Syntax', pl:'Składnia', de:'Syntax' },
    '01-language/03-control-flow.md', { en:'Control Flow', pl:'Kontrola przepływu', de:'Kontrollfluss' },
    '01-language/04-classes.md', { en:'Classes & OOP', pl:'Klasy i OOP', de:'Klassen & OOP' },
    '01-language/05-error-handling.md', { en:'Error Handling', pl:'Obsługa błędów', de:'Fehlerbehandlung' },
    '01-language/06-collections.md', { en:'Collections', pl:'Kolekcje', de:'Sammlungen' },
  ]},
  { section: 'Minecraft API', items: [
    '02-api/01-player.md', { en:'Player API', pl:'Player API', de:'Player API' },
    '02-api/02-world.md', { en:'World API', pl:'World API', de:'World API' },
    '02-api/03-entity.md', { en:'Entity API', pl:'Entity API', de:'Entity API' },
    '02-api/04-item.md', { en:'Item API', pl:'Item API', de:'Item API' },
    '02-api/05-inventory.md', { en:'Inventory API', pl:'Inventory API', de:'Inventory API' },
    '02-api/06-chat.md', { en:'Chat API', pl:'Chat API', de:'Chat API' },
    '02-api/07-sound-particle.md', { en:'Sound & Particle', pl:'Dźwięki i cząsteczki', de:'Sound & Partikel' },
    '02-api/09-nbt.md', { en:'NBT API', pl:'NBT API', de:'NBT API' },
    '02-api/10-effect.md', { en:'Effect API', pl:'Effect API', de:'Effect API' },
  ]},
  { section: 'Standard Library', items: [
    '03-stdlib/01-math.md', { en:'GL.Math', pl:'GL.Math', de:'GL.Math' },
    '03-stdlib/02-string.md', { en:'GL.String', pl:'GL.String', de:'GL.String' },
    '03-stdlib/03-list.md', { en:'GL.List', pl:'GL.List', de:'GL.List' },
    '03-stdlib/04-dict.md', { en:'GL.Dict', pl:'GL.Dict', de:'GL.Dict' },
    '03-stdlib/05-json.md', { en:'GL.JSON', pl:'GL.JSON', de:'GL.JSON' },
    '03-stdlib/07-time.md', { en:'GL.Time', pl:'GL.Time', de:'GL.Time' },
    '03-stdlib/08-vector.md', { en:'GL.Vector', pl:'GL.Vector', de:'GL.Vector' },
    '03-stdlib/09-color.md', { en:'GL.Color', pl:'GL.Color', de:'GL.Color' },
    '03-stdlib/10-event.md', { en:'GL.Event', pl:'GL.Event', de:'GL.Event' },
  ]},
  { section: 'GUI System', items: [
    '04-gui/01-widgets.md', { en:'Widgets', pl:'Widgety', de:'Widgets' },
  ]},
  { section: 'Tutorials', items: [
    '05-tutorials/03-working-with-player.md', { en:'Player Control', pl:'Sterowanie graczem', de:'Spielersteuerung' },
    '05-tutorials/04-building-with-world.md', { en:'World Building', pl:'Budowanie świata', de:'Weltbau' },
  ]},
  { section: 'Bridge', items: [
    '06-bridge/01-protocol.md', { en:'Protocol Spec', pl:'Specyfikacja protokołu', de:'Protokollspezifikation' },
    '06-bridge/02-setup.md', { en:'Mod Setup', pl:'Konfiguracja moda', de:'Mod-Einrichtung' },
    '06-bridge/03-python-client.md', { en:'Python Client', pl:'Klient Python', de:'Python-Client' },
    '06-bridge/04-troubleshooting.md', { en:'Troubleshooting', pl:'Rozwiązywanie problemów', de:'Fehlerbehebung' },
  ]},
];

const DEFAULT_PAGE = 'README.md';

// ===== STATE =====
let currentPage = DEFAULT_PAGE;
let currentLang = localStorage.getItem('mlang-lang') || navigator.language.slice(0,2);
if (!LANG_LIST.find(l => l.code === currentLang)) currentLang = 'en';
let theme = localStorage.getItem('mlang-theme') || 'dark';

// ===== DOM =====
const nav = document.getElementById('nav');
const contentDiv = document.getElementById('markdown-content');
const loadingEl = document.getElementById('loading');
const loadingText = document.getElementById('loading-text');
const footerText = document.getElementById('footer-text');
const sidebar = document.getElementById('sidebar');
const menuToggle = document.getElementById('menu-toggle');
const themeToggleBtn = document.getElementById('theme-toggle');
const html = document.documentElement;

// ===== I18N =====
function t(key) {
  return (UI_STRINGS[currentLang] && UI_STRINGS[currentLang][key]) || key;
}

function sectionTitle(sec) {
  return (PAGE_TITLES[sec] && PAGE_TITLES[sec][currentLang]) || PAGE_TITLES[sec]?.en || sec;
}

function itemTitle(titles) {
  if (typeof titles === 'string') return titles;
  return titles[currentLang] || titles.en || Object.values(titles)[0];
}

function langDocPath(path) {
  return `docs/${currentLang}/${path}`;
}

function fallbackDocPath(path) {
  return `docs/en/${path}`;
}

// ===== RENDER =====
function renderSidebar() {
  nav.innerHTML = '';
  PAGES.forEach(sec => {
    const section = document.createElement('div');
    section.className = 'nav-section';
    const header = document.createElement('div');
    header.className = 'nav-section-header';
    header.innerHTML = `${sectionTitle(sec.section)} <span class="arrow">▼</span>`;
    header.onclick = () => {
      header.classList.toggle('collapsed');
      section.querySelectorAll('.nav-link').forEach(l =>
        l.style.display = header.classList.contains('collapsed') ? 'none' : '');
    };
    section.appendChild(header);

    for (let i = 0; i < sec.items.length; i += 2) {
      const path = sec.items[i];
      const titles = sec.items[i + 1];
      const link = document.createElement('div');
      link.className = 'nav-link';
      link.textContent = itemTitle(titles);
      link.dataset.path = path;
      link.onclick = () => {
        loadPage(path);
        if (window.innerWidth <= 800) sidebar.classList.remove('open');
      };
      section.appendChild(link);
    }
    nav.appendChild(section);
  });
  nav.querySelector('.nav-section-header')?.classList.remove('collapsed');
}

function renderLanguageSelector() {
  const sel = document.getElementById('lang-selector');
  if (!sel) return;
  sel.innerHTML = '';
  LANG_LIST.forEach(lang => {
    const opt = document.createElement('div');
    opt.className = 'lang-option' + (lang.code === currentLang ? ' active' : '');
    opt.dataset.lang = lang.code;
    opt.innerHTML = `<span class="lang-flag">${lang.flag}</span> ${lang.name}`;
    opt.onclick = () => { switchLanguage(lang.code); sel.classList.remove('open'); };
    sel.appendChild(opt);
  });
}

function renderSettings() {
  const panel = document.getElementById('settings-panel');
  panel.innerHTML = `
    <h3>${t('settings')}</h3>
    <div class="setting-row">
      <span>${t('themeLabel')}</span>
      <div class="setting-options">
        <button class="setting-btn ${theme==='dark'?'active':''}" data-theme="dark">${t('themeDark')}</button>
        <button class="setting-btn ${theme==='light'?'active':''}" data-theme="light">${t('themeLight')}</button>
      </div>
    </div>
    <div class="setting-row">
      <span>${t('langLabel')}</span>
      <div class="lang-selector-wrapper">
        <button id="lang-btn" class="lang-btn">
          <span class="lang-flag">${getFlag()}</span> ${getLangName()} <span class="arrow-down">▼</span>
        </button>
        <div id="lang-selector" class="lang-dropdown"></div>
      </div>
    </div>`;
  document.getElementById('lang-btn').onclick = () =>
    document.getElementById('lang-selector').classList.toggle('open');
  panel.querySelectorAll('.setting-btn').forEach(btn =>
    btn.onclick = () => { theme = btn.dataset.theme; applyTheme(); renderSettings(); });
  renderLanguageSelector();
}

function getFlag() { return LANG_LIST.find(l => l.code === currentLang)?.flag || '🇬🇧'; }
function getLangName() { return LANG_LIST.find(l => l.code === currentLang)?.name || 'English'; }

function switchLanguage(code) {
  currentLang = code;
  localStorage.setItem('mlang-lang', code);
  translateStatic();
  renderSidebar();
  renderSettings();
  loadPage(currentPage);
}

function translateStatic() {
  loadingText.textContent = t('Loading...');
  footerText.textContent = t('footer');
}

// ===== PAGE LOADING =====
function mdLoad(text) {
  if (typeof marked !== 'undefined' && marked.parse) {
    return marked.parse(text, { breaks: true, gfm: true });
  }
  // Fallback: render as plain text with basic formatting
  return '<pre style="white-space:pre-wrap;font-family:var(--font-mono);font-size:13px">'
    + escapeHtml(text) + '</pre>';
}

async function loadPage(path) {
  currentPage = path;
  loadingEl.classList.remove('hidden');
  contentDiv.classList.add('hidden');

  try {
    let resp = await fetch('/' + langDocPath(path));
    if (!resp.ok) resp = await fetch('/' + fallbackDocPath(path));
    if (!resp.ok) throw new Error('404');

    const text = await resp.text();
    contentDiv.innerHTML = mdLoad(text);

    document.querySelectorAll('.nav-link').forEach(l => {
      l.classList.toggle('active', l.dataset.path === path);
      if (l.dataset.path === path) l.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    });

    contentDiv.querySelectorAll('pre code').forEach(b => {
      if (typeof hljs !== 'undefined') hljs.highlightElement(b);
    });

  } catch (e) {
    contentDiv.innerHTML = `<h1>${t('pageNotFound')}</h1><p>${t('pageNotFoundDesc')}</p>
      <p style="color:var(--error)">${path}</p>`;
  } finally {
    loadingEl.classList.add('hidden');
    contentDiv.classList.remove('hidden');
    document.getElementById('content').scrollTop = 0;
  }
}

function escapeHtml(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

// ===== THEME =====
function applyTheme() {
  html.setAttribute('data-theme', theme);
  themeToggleBtn.textContent = theme === 'dark' ? '☀' : '🌙';
  localStorage.setItem('mlang-theme', theme);
}

themeToggleBtn.onclick = () => { theme = theme === 'dark' ? 'light' : 'dark'; applyTheme(); };

// ===== MOBILE =====
menuToggle.onclick = () => sidebar.classList.toggle('open');
document.addEventListener('click', e => {
  if (window.innerWidth <= 800 && !sidebar.contains(e.target) && e.target !== menuToggle)
    sidebar.classList.remove('open');
  if (!e.target.closest('.lang-selector-wrapper'))
    document.querySelectorAll('.lang-dropdown').forEach(d => d.classList.remove('open'));
});

// ===== INIT =====
function init() {
  applyTheme();
  translateStatic();
  renderSidebar();
  renderSettings();
  loadPage(DEFAULT_PAGE);
}

document.readyState === 'loading'
  ? document.addEventListener('DOMContentLoaded', init)
  : init();
