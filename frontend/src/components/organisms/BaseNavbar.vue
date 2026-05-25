<template>
  <nav class="base-navbar" :class="{ 'navbar--hidden': isHidden }">

    <!-- Left: Language selector -->
    <div class="navbar-left">
      <button class="pill-btn lang-btn" @click="toggleLanguage">
        {{ currentLang }}
      </button>
    </div>

    <!-- Center: Navigation Tabs -->
    <div class="navbar-center">
      <router-link to="/" class="nav-link" active-class="nav-link--active">
        Inicio
      </router-link>
      <router-link to="/create-story" class="nav-link" active-class="nav-link--active">
        + Crear Historia
      </router-link>
    </div>

    <!-- Right: Profile & Logout -->
    <div class="navbar-right">
      <span class="username">👤 {{ user.username || 'Usuario' }}</span>
      <button class="pill-btn logout-btn" @click="handleLogout">
        Salir →
      </button>
    </div>

  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../composables/useAuthStore'

const router = useRouter()
const { user, isAdmin, logout } = useAuthStore()
const currentLang = ref('ES')

// ── Smart hide/show on scroll ──────────────────────────────
const isHidden = ref(false)
let lastScrollY = 0
const THRESHOLD = 8 // px hacia arriba para reaparecer

const onScroll = () => {
  const currentY = window.scrollY
  if (currentY <= 0) {
    // Siempre visible en el tope
    isHidden.value = false
  } else if (currentY > lastScrollY + 4) {
    // Scrolleando hacia abajo → ocultar
    isHidden.value = true
  } else if (lastScrollY - currentY > THRESHOLD) {
    // Scrolleando hacia arriba con suficiente impulso → mostrar
    isHidden.value = false
  }
  lastScrollY = currentY
}

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))

// ── Actions ───────────────────────────────────────────────
const toggleLanguage = () => {
  currentLang.value = currentLang.value === 'ES' ? 'EN' : 'ES'
  alert(`Idioma cambiado a: ${currentLang.value}`)
}

const handleLogout = () => {
  logout()
  alert('Sesión cerrada con éxito')
  router.push('/login')
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

  background: rgba(255, 255, 255, 0.97);
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
}

/* ── Responsive ── */
@media (max-width: 680px) {
  .base-navbar {
    top: 10px;
    width: calc(100% - 24px);
    flex-wrap: wrap;
    border-radius: 20px;
    padding: 12px 16px;
    gap: 10px;
  }

  .navbar-center {
    order: 3;
    width: 100%;
    justify-content: center;
  }

  .username {
    display: none;
  }
}
</style>
