<template>
  <div class="home-view-container">

    <!-- ── HERO: Logo izquierda / Texto derecha ── -->
    <div class="hero-section">
      <!-- Logo sin ningún estilo decorativo, se camufla con el fondo azul -->
      <div class="hero-logo-col">
        <img src="../assets/Logo.jpg" alt="{{ t('home.imageLabel') }}" class="hero-logo" />
      </div>

      <!-- Texto -->
      <div class="hero-text-col">
        <h1 class="hero-title">{{ t('home.brandTitle') }}</h1>
        <p class="hero-paragraph">
           {{ t('home.heroParagraph') }}
        </p>
      </div>
    </div>

    <!-- Map Section -->
    <InteractiveMap
      :selectedContinent="selectedContinent"
      @continent-selected="selectedContinent = $event"
    />

     <!-- Chronicles / Filters Section -->
    <ChronicleList
      v-if="authStore.isAuthenticated"
      :selectedContinent="selectedContinent"
    />
    <div v-else class="login-prompt">
      <h2>{{ t('home.loginPromptTitle') }}</h2>
      <p>{{ t('home.loginPromptText') }}</p>
      <div class="login-prompt-actions">
        <router-link to="/login" class="prompt-btn primary">{{ t('home.loginPromptLogin') }}</router-link>
        <router-link to="/register" class="prompt-btn secondary">{{ t('home.loginPromptRegister') }}</router-link>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import InteractiveMap from '../components/organisms/InteractiveMap.vue'
import ChronicleList from '../components/organisms/ChronicleList.vue'
import { useAuthStore } from '../composables/useAuthStore'
const { t } = useI18n()

const authStore = useAuthStore()
const selectedContinent = ref('')
</script>

<style scoped>
/* ── Variables ── */
.home-view-container {
  --color-principal: #2D6A8B;
  --color-rojo:      #E93C44;
  --color-amarillo:  #FCD015;
  --color-blanco:    #FFFFFF;

  position: relative;
  overflow: hidden;
  background: var(--color-principal);
  min-height: 100vh;
  padding: 0 80px;
  animation: fadeIn 0.45s ease-out;
}

.home-view-container::before,
.home-view-container::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 70px;
  background-repeat: repeat-y;
  background-position: top center;
  background-size: 70px auto;
  opacity: 0.96;
  pointer-events: none;
}

.home-view-container::before {
  left: 0;
  background-image: url('../assets/1.png');
}

.home-view-container::after {
  right: 0;
  background-image: url('../assets/2.png');
}

@media (max-width: 900px) {
  .home-view-container {
    padding: 0 24px;
  }

  .home-view-container::before,
  .home-view-container::after {
    display: none;
  }
}

/* ── HERO layout: dos columnas ── */
.hero-section {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 48px;
  padding: 60px 64px 72px;
  max-width: 1100px;
  margin: 0 auto;
}

/* ── Columna izquierda: logo ── */
.hero-logo-col {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-logo {
  display: block;
  width: clamp(200px, 28vw, 360px);
  height: auto;
  object-fit: contain;
  /* Sin ningún filtro, borde ni efecto — imagen limpia */
}

/* ── Columna derecha: texto ── */
.hero-text-col {
  flex: 1;
}

.hero-title {
  font-size: clamp(1.2rem, 3.2vw, 2.8rem);
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--color-amarillo);
  border-bottom: 4px solid var(--color-rojo);
  padding-bottom: 14px;
  margin-bottom: 24px;
  display: inline-block;
  line-height: 1.15;
  white-space: normal;
  word-break: break-word;
}

.hero-paragraph {
  font-size: clamp(1rem, 1.6vw, 1.2rem);
  line-height: 1.75;
  color: var(--color-blanco);
  font-weight: 400;
  max-width: 560px;
  margin: 0;
}

/* ── Animación ── */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Responsive: apila en móvil ── */
@media (max-width: 768px) {
  .hero-section {
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 40px 16px 48px;
    gap: 24px;
  }

  .hero-paragraph {
    max-width: 100%;
  }

  .hero-logo {
    width: clamp(160px, 50vw, 280px);
  }
}

@media (max-width: 480px) {
  .home-view-container {
    padding: 0 12px;
  }

  .hero-section {
    padding: 32px 12px 40px;
    gap: 16px;
  }

  .login-prompt {
    padding: 24px 16px;
    margin: 24px auto;
  }

  .login-prompt h2 {
    font-size: 1.4rem;
  }

  .login-prompt-actions {
    flex-direction: column;
    gap: 12px;
  }

  .prompt-btn {
    text-align: center;
  }
}

/* ── Login Prompt (No Authenticated) ── */
.login-prompt {
  text-align: center;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 40px;
  border-radius: 12px;
  max-width: 600px;
  margin: 40px auto;
  color: var(--color-blanco);
}

.login-prompt h2 {
  color: var(--color-amarillo);
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 1.8rem;
}

.login-prompt p {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 24px;
}

.login-prompt-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
}

.prompt-btn {
  text-decoration: none;
  padding: 10px 24px;
  border-radius: 999px;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.2s ease;
}

.prompt-btn.primary {
  background: var(--color-amarillo);
  color: #333;
}

.prompt-btn.primary:hover {
  background: #e6bd13;
  transform: translateY(-2px);
}

.prompt-btn.secondary {
  background: transparent;
  color: var(--color-blanco);
  border: 2px solid var(--color-blanco);
}

.prompt-btn.secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
}
</style>
