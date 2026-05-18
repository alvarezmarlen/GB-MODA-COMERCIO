<template>
  <nav class="base-navbar">
    <!-- Left: Language selector -->
    <div class="navbar-left">
      <button class="navbar-btn lang-btn" @click="toggleLanguage">
         {{ currentLang }}
      </button>
    </div>

    <!-- Center: Navigation Tabs -->
    <div class="navbar-center">
      <router-link to="/create-story" class="navbar-tab" active-class="active-tab">
        Inicio
      </router-link>
      <router-link to="/create-story" class="navbar-tab" active-class="active-tab">
        + Crear Historia
      </router-link>
    </div>

    <!-- Right: Profile Indicator & Logout -->
    <div class="navbar-right">
      <div class="profile-info">
        <span class="user-icon"></span>
        <span class="username">{{ user.username || 'Usuario' }}</span>
      </div>
      <button class="navbar-btn logout-btn" @click="handleLogout">
        <span class="logout-icon">[→</span> Cerrar Sesión
      </button>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../composables/useAuthStore'

const router = useRouter()
const { user, logout } = useAuthStore()
const currentLang = ref('ES')

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
.base-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 2px solid var(--wf-border);
  background-color: var(--wf-bg);
  padding: var(--wf-spacing-sm) var(--wf-spacing-md);
  margin-bottom: var(--wf-spacing-lg);
  font-family: 'Courier New', Courier, monospace;
}

.navbar-left, .navbar-right {
  display: flex;
  align-items: center;
  gap: var(--wf-spacing-md);
}

.navbar-center {
  display: flex;
  gap: var(--wf-spacing-sm);
}

/* Common button styling */
.navbar-btn {
  padding: 6px 12px;
  border: 1px solid var(--wf-border);
  background-color: var(--wf-button-bg);
  color: var(--wf-text);
  font-family: inherit;
  font-weight: bold;
  font-size: 0.9rem;
  cursor: pointer;
  border-radius: var(--wf-radius);
  transition: all 0.2s ease;
}

.navbar-btn:hover {
  background-color: var(--wf-button-hover);
}

.lang-btn {
  letter-spacing: 1px;
}

/* Tabs styling */
.navbar-tab {
  padding: 8px 16px;
  border: 1px solid transparent;
  color: var(--wf-text);
  text-decoration: none;
  font-weight: bold;
  font-size: 0.95rem;
  border-radius: var(--wf-radius);
  transition: all 0.2s ease;
}

.navbar-tab:hover {
  background-color: var(--wf-button-bg);
  border-color: var(--wf-border);
}

.active-tab {
  background-color: var(--wf-border);
  color: var(--wf-bg) !important;
  border-color: var(--wf-border);
}

/* Profile indicator & logout */
.profile-info {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border: 1px dashed var(--wf-border);
  border-radius: var(--wf-radius);
  font-size: 0.9rem;
  font-weight: bold;
}

.user-icon {
  font-size: 1.1rem;
}

.logout-btn {
  border-color: var(--wf-border);
}

.logout-icon {
  font-weight: bold;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .base-navbar {
    flex-direction: column;
    gap: var(--wf-spacing-sm);
    align-items: stretch;
    padding: var(--wf-spacing-md);
  }

  .navbar-left, .navbar-center, .navbar-right {
    justify-content: center;
    width: 100%;
  }

  .navbar-center {
    margin: var(--wf-spacing-sm) 0;
  }
}
</style>
