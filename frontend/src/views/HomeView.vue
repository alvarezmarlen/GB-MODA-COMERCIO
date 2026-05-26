<template>
  <div class="home-view-container">

    <!-- ── HERO: Logo izquierda / Texto derecha ── -->
    <div class="hero-section">
      <!-- Logo sin ningún estilo decorativo, se camufla con el fondo azul -->
      <div class="hero-logo-col">
        <img src="../assets/Logo.jpg" alt="Logo GB-Moda-Comercio" class="hero-logo" />
      </div>

      <!-- Texto -->
      <div class="hero-text-col">
        <h1 class="hero-title">{{ t('home.brandTitle') }}</h1>
        <p class="hero-paragraph">{{ t('home.heroParagraph') }}</p>
      </div>
    </div>

    <!-- Map Section -->
    <InteractiveMap />

    <!-- Chronicles / Filters Section -->
    <ChronicleList />

  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import InteractiveMap from '../components/organisms/InteractiveMap.vue'
import ChronicleList from '../components/organisms/ChronicleList.vue'

const { t } = useI18n()
</script>

<style scoped>
/* ── Variables ── */
.home-view-container {
  position: relative;
  overflow: hidden;
  background: var(--color-primary);
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
  font-size: clamp(1.4rem, 3.2vw, 2.8rem);
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--color-yellow);
  border-bottom: 4px solid var(--color-red);
  padding-bottom: 14px;
  margin-bottom: 24px;
  display: inline-block;
  line-height: 1.15;
  white-space: nowrap;
}

.hero-paragraph {
  font-size: clamp(1rem, 1.6vw, 1.2rem);
  line-height: 1.75;
  color: var(--color-white);
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
    padding: 48px 24px 56px;
    gap: 32px;
  }

  .hero-paragraph {
    max-width: 100%;
  }
}
</style>
