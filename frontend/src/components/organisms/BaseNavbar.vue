<template>
  <div class="navbar-wrapper">
    <nav class="base-navbar" :class="{ 'navbar--hidden': isHidden }">

      <!-- Left: Language selector -->
      <div class="navbar-left">
        <select class="lang-select" v-model="locale" @change="onLocaleChange">
          <option v-for="opt in languageOptions" :key="opt.value" :value="opt.value">
            {{ opt.label }}
          </option>
        </select>
      </div>

      <!-- Center: Navigation Tabs (desktop) -->
      <div class="navbar-center desktop-only">
        <router-link to="/" class="nav-link" active-class="nav-link--active">
          {{ t('nav.home') }}
        </router-link>
        <router-link v-if="authStore.isAuthenticated" to="/create-story" class="nav-link" active-class="nav-link--active">
          {{ t('nav.createStory') }}
        </router-link>
      </div>

      <!-- Right: Profile & Logout (desktop) -->
      <div class="navbar-right desktop-only">
        <template v-if="authStore.isAuthenticated">
          <router-link :to="authStore.user?.role === 'admin' ? '/admin' : '/dashboard'" class="username">👤 {{ authStore.user?.username || 'Usuario' }}</router-link>
          <button class="pill-btn logout-btn" @click="handleLogout">
            {{ t('nav.logout') }}
          </button>
        </template>
        <template v-else>
          <router-link to="/login" class="nav-link">{{ t('auth.loginLink') }}</router-link>
          <router-link to="/register" class="pill-btn">{{ t('auth.registerLink') }}</router-link>
        </template>
      </div>

      <!-- Hamburger toggle (mobile only) -->
      <button class="hamburger-btn mobile-only" @click="toggleMenu" :aria-label="t('nav.menu')">
        <span class="hamburger-line" :class="{ open: isMenuOpen }"></span>
        <span class="hamburger-line" :class="{ open: isMenuOpen }"></span>
        <span class="hamburger-line" :class="{ open: isMenuOpen }"></span>
      </button>

    </nav>

    <!-- Mobile menu overlay (FUERA del nav para evitar problemas con transform) -->
    <div class="mobile-menu-overlay" :class="{ 'mobile-menu--open': isMenuOpen }" @click.self="closeMenu">
      <div class="mobile-menu-panel" :class="{ 'mobile-menu--open': isMenuOpen }">
        <div class="mobile-menu-header">
          <span class="mobile-menu-title">{{ t('nav.menu') }}</span>
          <button class="mobile-close-btn" @click="closeMenu">✕</button>
        </div>
        <div class="mobile-menu-links">
          <router-link to="/" class="mobile-nav-link" @click="closeMenu">
            {{ t('nav.home') }}
          </router-link>
          <router-link v-if="authStore.isAuthenticated" to="/create-story" class="mobile-nav-link" @click="closeMenu">
            {{ t('nav.createStory') }}
          </router-link>
          <div class="mobile-menu-divider"></div>
          <template v-if="authStore.isAuthenticated">
            <router-link :to="authStore.user?.role === 'admin' ? '/admin' : '/dashboard'" class="mobile-nav-link" @click="closeMenu">
              👤 {{ authStore.user?.username || 'Usuario' }}
            </router-link>
            <button class="mobile-nav-link mobile-logout" @click="handleLogoutClose">
              {{ t('nav.logout') }}
            </button>
          </template>
          <template v-else>
            <router-link to="/login" class="mobile-nav-link" @click="closeMenu">
              {{ t('auth.loginLink') }}
            </router-link>
            <router-link to="/register" class="mobile-nav-link mobile-register" @click="closeMenu">
              {{ t('auth.registerLink') }}
            </router-link>
          </template>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useAuthStore } from '../../composables/useAuthStore'

const { t, locale } = useI18n()
const router = useRouter()
const authStore = useAuthStore()

const languageOptions = computed(() => [
  { value: 'ar', label: t('lang.ar') },
  { value: 'es', label: t('lang.es') },
  { value: 'en', label: t('lang.en') },
  { value: 'eu', label: t('lang.eu') },
  { value: 'fr', label: t('lang.fr') },
  { value: 'ro', label: t('lang.ro') },
])

const onLocaleChange = () => {
  localStorage.setItem('locale', locale.value)
}

// ── Smart hide/show on scroll ──────────────────────────────
const isHidden = ref(false)
let lastScrollY = 0
const THRESHOLD = 8

const onScroll = () => {
  const currentY = window.scrollY
  if (currentY <= 0) {
    isHidden.value = false
  } else if (currentY > lastScrollY + 4) {
    isHidden.value = true
  } else if (lastScrollY - currentY > THRESHOLD) {
    isHidden.value = false
  }
  lastScrollY = currentY
}

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))

// ── Hamburger menu ────────────────────────────────────────
const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const handleLogoutClose = () => {
  closeMenu()
  handleLogout()
}

// ── Actions ───────────────────────────────────────────────
const handleLogout = () => {
  authStore.logout()
  alert(t('nav.logoutSuccess'))
  router.push('/')
}
</script>

<style scoped>
/* ── Fixed floating pill ── */
.base-navbar {
  position: fixed;
  top: 16px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;

  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;

  width: calc(100% - 48px);
  max-width: 820px;

  background: #FCD015;
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);

  border-radius: 999px;
  padding: 10px 20px;

  box-shadow:
    0 4px 24px rgba(0, 0, 0, 0.13),
    0 1px 4px rgba(0, 0, 0, 0.07);

  font-family: 'Inter', system-ui, sans-serif;

  /* Animación de entrada/salida */
  transition:
    transform 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    opacity 0.3s ease,
    box-shadow 0.3s ease;
}

.navbar--hidden {
  transform: translateX(-50%) translateY(calc(-100% - 20px));
  opacity: 0;
  pointer-events: none;
}

.base-navbar:not(.navbar--hidden):hover {
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.16),
    0 2px 6px rgba(0, 0, 0, 0.09);
}

/* ── Sections ── */
.navbar-left,
.navbar-right {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}

.navbar-center {
  display: flex;
  align-items: center;
  gap: 4px;
}

/* ── Nav links ── */
.nav-link {
  padding: 7px 16px;
  border-radius: 999px;
  color: #444;
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  transition: background 0.2s ease, color 0.2s ease;
  white-space: nowrap;
}

.nav-link:hover {
  background: #f0f0f0;
  color: #111;
}

.nav-link--active {
  background: #2D6A8B;
  color: #fff !important;
}

/* ── Pill buttons ── */
.pill-btn {
  padding: 7px 16px;
  border-radius: 999px;
  border: 1.5px solid #e0e0e0;
  background: transparent;
  color: #333;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  letter-spacing: 0.03em;
  transition: background 0.2s ease, border-color 0.2s ease;
  font-family: inherit;
}

.pill-btn:hover {
  background: #f5f5f5;
  border-color: #bbb;
}

.role-badge {
  font-size: 0.65rem;
  letter-spacing: 1px;
  padding: 2px 6px;
  border: 1px solid var(--wf-border);
  background: var(--wf-button-bg);
  border-radius: 2px;
}

.logout-btn {
  color: #c0392b;
  border-color: #f5c6c4;
}

.logout-btn:hover {
  background: #fff5f5;
  border-color: #e0a8a6;
}

/* ── Username ── */
.username {
  font-size: 0.85rem;
  font-weight: 500;
  color: #555;
  white-space: nowrap;
  text-decoration: none;
  transition: color 0.2s ease;
}

.username:hover {
  color: #111;
}

/* ── Wrapper to hold nav + overlay without transform issues ── */
.navbar-wrapper {
  position: relative;
}

/* ── Desktop-only elements ── */
.desktop-only {
  display: flex;
}

.mobile-only {
  display: none;
}

/* ── Hamburger button ── */
.hamburger-btn {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 4px;
  width: 36px;
  height: 36px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px;
  border-radius: 8px;
  transition: background 0.2s ease;
}

.hamburger-btn:hover {
  background: rgba(0, 0, 0, 0.06);
}

.hamburger-line {
  display: block;
  width: 20px;
  height: 2.5px;
  background: #444;
  border-radius: 2px;
  transition: all 0.3s ease;
  transform-origin: center;
}

.hamburger-line.open:nth-child(1) {
  transform: translateY(6.5px) rotate(45deg);
}

.hamburger-line.open:nth-child(2) {
  opacity: 0;
}

.hamburger-line.open:nth-child(3) {
  transform: translateY(-6.5px) rotate(-45deg);
}

/* ── Mobile menu overlay ── */
.mobile-menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
  pointer-events: none;
}

.mobile-menu-overlay.mobile-menu--open {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
}

.mobile-menu-panel {
  position: fixed;
  top: 0;
  right: 0;
  width: 300px;
  max-width: 85vw;
  height: 100%;
  background: #ffffff;
  box-shadow: -8px 0 32px rgba(0, 0, 0, 0.2);
  transform: translateX(100%);
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  display: flex;
  flex-direction: column;
  z-index: 1000;
}

.mobile-menu-panel.mobile-menu--open {
  transform: translateX(0);
}

.mobile-menu-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 24px 16px;
  border-bottom: 1px solid #e8e8e8;
  background: #fafafa;
}

.mobile-menu-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #222;
  letter-spacing: 0.5px;
}

.mobile-close-btn {
  background: none;
  border: none;
  font-size: 1.4rem;
  cursor: pointer;
  color: #555;
  padding: 4px 10px;
  border-radius: 6px;
  transition: background 0.2s ease;
  line-height: 1;
}

.mobile-close-btn:hover {
  background: #e8e8e8;
}

.mobile-menu-links {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 8px 0;
  overflow-y: auto;
  background: #ffffff;
}

.mobile-nav-link {
  display: block;
  padding: 16px 24px;
  font-size: 1.05rem;
  font-weight: 600;
  color: #222;
  text-decoration: none;
  transition: background 0.15s ease, color 0.15s ease;
  border: none;
  background: transparent;
  text-align: left;
  width: 100%;
  font-family: inherit;
  cursor: pointer;
  letter-spacing: 0.3px;
}

.mobile-nav-link:hover {
  background: #f0f0f0;
  color: #000;
}

.mobile-nav-link:active {
  background: #e0e0e0;
}

.mobile-nav-link.mobile-register {
  color: #1a5a7a;
  font-weight: 700;
}

.mobile-nav-link.mobile-logout {
  color: #c0392b;
  font-weight: 600;
}

.mobile-menu-divider {
  height: 1px;
  background: #e0e0e0;
  margin: 8px 24px;
}

/* ── Responsive ── */
@media (max-width: 680px) {
  .base-navbar {
    top: 10px;
    width: calc(100% - 24px);
    border-radius: 20px;
    padding: 10px 14px;
    gap: 6px;
  }

  .desktop-only {
    display: none;
  }

  .mobile-only {
    display: flex;
  }

  .hamburger-btn {
    display: flex;
  }

  .username {
    display: none;
  }
}
</style>
