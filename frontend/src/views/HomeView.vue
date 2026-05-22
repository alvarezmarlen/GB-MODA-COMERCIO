<template>
  <div class="home-view-container">
    <!-- Hero Section -->
    <div class="wireframe-container hero-container">
      <div class="hero-grid">
        <!-- Left: Image Column -->
        <div class="hero-left-box">
          <div class="image-placeholder-box">
            <svg class="crossed-lines" xmlns="http://www.w3.org/2000/svg">
              <line x1="0" y1="0" x2="100%" y2="100%" />
              <line x1="100%" y1="0" x2="0" y2="100%" />
            </svg>
            <div class="image-label">{{ t('home.imageLabel') }}</div>
          </div>
        </div>

        <!-- Right: Text Column -->
        <div class="hero-right-box">
          <h1 class="hero-title">{{ t('home.brandTitle') }}</h1>
          <p class="hero-paragraph">
            {{ t('home.heroParagraph') }}
          </p>
        </div>
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
.home-view-container {
  padding: var(--wf-spacing-md) 0;
  animation: fadeIn 0.4s ease-out;
}

.hero-container {
  margin: 0;
  padding: var(--wf-spacing-lg) !important;
  background: var(--wf-bg);
  border-width: 2px;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.12fr 1fr;
  gap: var(--wf-spacing-lg);
  align-items: stretch;
  min-height: 380px;
}

.hero-left-box {
  display: flex;
  flex: 1;
}

.image-placeholder-box {
  flex: 1;
  border: 2px solid var(--wf-border);
  background: #fdfdfd;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 340px;
  transition: all 0.3s ease;
}

.crossed-lines {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.crossed-lines line {
  stroke: var(--wf-placeholder);
  stroke-width: 1.5;
}

.image-label {
  position: relative;
  background: var(--wf-bg);
  padding: 6px 16px;
  border: 2px solid var(--wf-border);
  font-family: monospace;
  font-weight: bold;
  font-size: 1rem;
  letter-spacing: 2px;
  z-index: 2;
  text-transform: uppercase;
}

.image-placeholder-box:hover {
  background: #f9f9f9;
  box-shadow: 4px 4px 0px var(--wf-border);
  transform: translate(-2px, -2px);
}

.image-placeholder-box:hover .image-label {
  background: var(--wf-border);
  color: var(--wf-bg);
}

.hero-right-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: var(--wf-spacing-lg);
  border: 2px solid var(--wf-border);
  background: var(--wf-bg);
  transition: all 0.3s ease;
}

.hero-right-box:hover {
  box-shadow: 4px 4px 0px var(--wf-border);
  transform: translate(-2px, -2px);
}

.hero-title {
  font-size: 2rem;
  font-weight: bold;
  letter-spacing: 2px;
  margin-bottom: var(--wf-spacing-md);
  text-transform: uppercase;
  border-bottom: 2px solid var(--wf-border);
  padding-bottom: var(--wf-spacing-xs);
}

.hero-paragraph {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--wf-text);
  margin: 0;
  text-align: justify;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 800px) {
  .hero-grid {
    grid-template-columns: 1fr;
    gap: var(--wf-spacing-md);
  }
  
  .image-placeholder-box {
    min-height: 260px;
  }
  
  .hero-right-box {
    padding: var(--wf-spacing-md);
  }
  
  .hero-title {
    font-size: 1.6rem;
  }
}
</style>
