<template>
  <div class="story-detail-template">
    <div class="template-inner">
      <header class="template-header">
        <h1 class="template-title">DETALLE DE LA HISTORIA</h1>
        <button class="wireframe-button back-button" @click="goBack">
          ← Volver
        </button>
      </header>

      <main class="template-content">
        <div class="story-card">
          <div class="story-title-box">
            <h2>{{ storyToShow.title }}</h2>
          </div>

          <div class="story-images-container" :class="{ 'double-images': storyToShow.images.length === 2 }">
            <template v-if="storyToShow.images.length > 0">
              <div
                v-for="(img, idx) in storyToShow.images"
                :key="idx"
                class="story-image-wrapper"
              >
                <img :src="img" alt="Imagen de la historia" class="story-image" />
              </div>
            </template>
            <template v-else>
              <div class="story-image-placeholder">
                <p>IMAGEN DE LA HISTORIA</p>
              </div>
            </template>
          </div>

          <div class="story-meta">
            <span class="meta-item"><strong>Oficio:</strong> {{ professionLabel }}</span>
            <span class="meta-item"><strong>Edad:</strong> {{ ageRangeLabel }}</span>
          </div>

          <div class="story-description">
            <p v-for="(paragraph, index) in formattedDescription" :key="index">
              {{ paragraph }}
            </p>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useStoryStore } from '../composables/useStoryStore'

const router = useRouter()
const { currentStory } = useStoryStore()
const storyToShow = computed(() => currentStory)

const goBack = () => router.push('/')

const professionLabel = computed(() => storyToShow.value.profession || 'No especificado')
const ageRangeLabel = computed(() => storyToShow.value.ageRange || 'No especificada')
const formattedDescription = computed(() => {
  if (!storyToShow.value.description) return []
  return storyToShow.value.description.split('\n\n').filter(p => p.trim() !== '')
})
</script>

<style scoped>
.story-detail-template {
  position: relative;
  min-height: 100vh;
  width: 100%;
  overflow: hidden;
}

.template-inner {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px 100px;
  padding-top: 100px;
}

/* Side images mirroring CreateStoryTemplate */
.story-detail-template::before,
.story-detail-template::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 120px;
  background-repeat: repeat-y;
  background-position: top center;
  background-size: cover;
  opacity: 0.96;
  pointer-events: none;
  z-index: 0;
}

.story-detail-template::before {
  left: 0;
  background-image: url('../assets/1.png');
}

.story-detail-template::after {
  right: 0;
  background-image: url('../assets/2.png');
}

.template-inner {
  position: relative;
  z-index: 1;
}

@media (max-width: 900px) {
  .story-detail-template::before,
  .story-detail-template::after {
    display: none;
  }
}

.template-header {
  text-align: center;
  margin-bottom: var(--wf-spacing-lg);
  border-bottom: 5px solid var(--color-red);
  padding-bottom: var(--wf-spacing-sm);
}

h1.template-title {
  font-size: 1.5rem;
  letter-spacing: 2px;
  color: var(--color-yellow);
  margin-bottom: 20px;
}

.back-button {
  background: var(--color-red);
  color: var(--color-white);
  border: none;
  border-radius: var(--wf-radius);
  padding: 8px 16px;
  cursor: pointer;
}

.story-card {
  padding: var(--wf-spacing-lg);
  background: var(--wf-bg);
  border-radius: var(--wf-radius);
}

.story-title-box h2 {
  font-size: 1.5rem;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.story-image-wrapper {
  margin-bottom: 20px;
  border: 1px solid var(--color-primary);
  border-radius: var(--wf-radius);
}

.story-image {
  width: 100%;
  height: auto;
  display: block;
}

.story-meta {
  display: flex;
  gap: 20px;
  margin: 20px 0;
  font-weight: bold;
}

.story-description p {
  line-height: 1.7;
  margin-bottom: 15px;
}

@media (max-width: 680px) {
  .story-detail-template {
    padding-top: 140px;
  }
}
</style>
