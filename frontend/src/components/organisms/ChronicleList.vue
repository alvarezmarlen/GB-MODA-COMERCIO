<template>
  <div class="chronicles-section">
    <!-- Filters Header -->
    <div class="filters-header">
      <h3 class="filter-title">Filtrado</h3>
      <div class="filters-row">
        <select class="wireframe-input filter-select">
          <option value="">Oficio</option>
        </select>
        <select class="wireframe-input filter-select">
          <option value="">Edad</option>
        </select>
      </div>
      <div class="elegant-divider"></div>
    </div>

    <!-- Chronicles List -->
    <div class="chronicles-list">
      <!-- Card 1 -->
      <div class="chronicle-card wireframe-container">
        <!-- Top Bar (as in the design) -->
        <div class="card-top-bar">
          <div class="card-top-bar-inner"></div>
        </div>
        
        <!-- Card Body -->
        <div class="card-body">
          <div class="card-image-box">
            <span>Imagen</span>
          </div>
          
          <div class="card-content">
            <div class="card-meta">
              Oficio: Casa &nbsp;|&nbsp; Edad: 45 años
            </div>
            <div class="placeholder-lines">
              <div class="placeholder-line"></div>
              <div class="placeholder-line"></div>
              <div class="placeholder-line short"></div>
            </div>
            <div class="card-actions">
              <button class="wireframe-button" @click="goToStoryDetail">Ver más</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="chronicle-card wireframe-container">
        <!-- Top Bar (as in the design) -->
        <div class="card-top-bar">
          <div class="card-top-bar-inner"></div>
        </div>
        
        <!-- Card Body -->
        <div class="card-body">
          <div class="card-image-box">
            <span>Imagen</span>
          </div>
          
          <div class="card-content">
            <div class="card-meta">
              Oficio: Campo &nbsp;|&nbsp; Edad: 32 años
            </div>
            <div class="placeholder-lines">
              <div class="placeholder-line"></div>
              <div class="placeholder-line"></div>
              <div class="placeholder-line short"></div>
            </div>
            <div class="card-actions">
              <button class="wireframe-button" @click="goToStoryDetail">Ver más</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goToStoryDetail = () => {
  router.push({ name: 'story-detail' })
}
</script>

<style scoped>
.chronicles-section {
  width: 100%;
  max-width: 1100px;
  margin: var(--wf-spacing-lg) auto 0;
  padding: 0 32px;
  box-sizing: border-box;
}

/* Filters */
.filters-header {
  margin-bottom: var(--wf-spacing-lg);
  padding: 0 0 0 0;
}

.filter-title {
  font-size: 1.8rem;
  color: var(--color-amarillo);
  margin-bottom: var(--wf-spacing-sm);
  text-transform: none;
  letter-spacing: 0.5px;
}

.filters-row {
  display: flex;
  gap: var(--wf-spacing-md);
  margin-bottom: var(--wf-spacing-md);
}

.filter-select {
  width: 220px;
  cursor: pointer;
  background: var(--wf-bg);
  color: var(--wf-text);
  appearance: none;
  background-image: url('data:image/svg+xml;utf8,<svg fill="black" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>');
  background-repeat: no-repeat;
  background-position-x: 95%;
  background-position-y: 50%;
  padding-right: 30px;
  border: 2px solid var(--wf-border);
  border-radius: 0;
  font-weight: bold;
}

.elegant-divider {
  width: 100%;
  height: 2px;
  background: var(--color-amarillo);
  margin-bottom: var(--wf-spacing-lg);
}

.chronicle-card {
  padding: 0;
  display: flex;
  flex-direction: column;
  border: none;
  border-radius: 12px;
  background: var(--color-rojo);
  transition: all 0.3s ease;
  color: var(--color-blanco);
}

/* Chronicles List */
.chronicles-list {
  display: flex;
  flex-direction: column;
  gap: var(--wf-spacing-lg);
}

/* Card */
.chronicle-card {
  padding: 0;
  display: flex;
  flex-direction: column;
  border: none;
  border-radius: 12px;
  background: var(--color-rojo);
  transition: all 0.3s ease;
  color: var(--color-blanco);
}

.chronicle-card:hover {
  box-shadow: 6px 6px 0px rgba(0, 0, 0, 0.15);
  transform: translate(-2px, -2px);
}

/* Top bar of the card */
.card-top-bar {
  background: rgba(255, 255, 255, 0.14);
  border-bottom: 2px solid rgba(255, 255, 255, 0.4);
  padding: 8px 16px;
  display: flex;
}

.card-top-bar-inner {
  width: 150px;
  height: 16px;
  background: rgba(255, 255, 255, 0.35);
}

/* Body of the card */
.card-body {
  display: flex;
  gap: var(--wf-spacing-lg);
  padding: var(--wf-spacing-lg);
}

.card-image-box {
  width: 200px;
  height: 200px;
  background: rgba(255, 255, 255, 0.12);
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--color-blanco);
  font-weight: bold;
  border: none;
  flex-shrink: 0;
  text-transform: none;
  letter-spacing: 0;
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.card-meta {
  font-weight: bold;
  color: var(--color-blanco);
  margin-bottom: var(--wf-spacing-lg);
  font-size: 1.1rem;
}

.placeholder-lines {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: auto;
}

.placeholder-line {
  height: 12px;
  background: var(--wf-placeholder);
  width: 100%;
}

.placeholder-line.short {
  width: 85%;
}

.card-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: var(--wf-spacing-md);
}

/* Responsive */
@media (max-width: 768px) {
  .card-body {
    flex-direction: column;
    align-items: center;
  }
  
  .card-image-box {
    width: 100%;
    max-width: 300px;
  }
}
</style>
