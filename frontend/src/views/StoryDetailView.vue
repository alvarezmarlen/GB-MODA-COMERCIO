<template>
  <div class="story-detail-template">
    <header class="template-header">
      <button class="wireframe-button back-button" @click="goBack">
        ← Volver
      </button>
    </header>

    <main class="template-content">
      <div class="wireframe-container story-card">
        <!-- Title Box -->
        <div class="story-title-box">
          <h2>{{ storyToShow.title }}</h2>
        </div>

        <hr class="wf-divider" />

        <!-- Image Gallery (1 or 2 Images) -->
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
          <!-- Placeholder Wireframe Box if no image is uploaded -->
          <template v-else>
            <div class="story-image-placeholder">
              <span class="placeholder-icon"></span>
              <p>IMAGEN DE LA HISTORIA</p>
            </div>
          </template>
        </div>

        <!-- Metadata Section -->
        <div class="story-meta">
          <span class="meta-item"><strong>Oficio:</strong> {{ professionLabel }}</span>
          <span class="meta-separator">│</span>
          <span class="meta-item"><strong>Edad:</strong> {{ ageRangeLabel }}</span>
        </div>

        <hr class="wf-divider" />

        <!-- Description Paragraphs -->
        <div class="story-description">
          <p v-for="(paragraph, index) in formattedDescription" :key="index">
            {{ paragraph }}
          </p>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useStoryStore } from '../composables/useStoryStore'

const router = useRouter()
const { currentStory } = useStoryStore()

// We read directly from currentStory, which can be populated by the form or loaded from a database/API.
const storyToShow = computed(() => currentStory)

const goBack = () => {
  router.push('/')
}

// Translations for user-friendly display
const professionLabel = computed(() => {
  const mapping = {
    casa: 'Casa',
    campo: 'Campo',
    industria: 'Industria',
    limpieza: 'Limpieza',
    otro: 'Otro'
  }
  return mapping[storyToShow.value.profession] || 'No especificado'
})

const ageRangeLabel = computed(() => {
  const mapping = {
    under_18: 'Menor de 18 años',
    '18_25': '18 - 25 años',
    '26_35': '26 - 35 años',
    '36_45': '36 - 45 años',
    '46_60': '46 - 60 años',
    over_60: 'Más de 60 años'
  }
  return mapping[storyToShow.value.ageRange] || 'No especificada'
})

const formattedDescription = computed(() => {
  if (!storyToShow.value.description) return []
  return storyToShow.value.description.split('\n\n').filter(p => p.trim() !== '')
})
</script>

<style scoped>
.story-detail-template {
  max-width: 800px;
  margin: 0 auto;
  padding: var(--wf-spacing-md);
}

.template-header {
  margin-bottom: var(--wf-spacing-md);
  border-bottom: 2px solid var(--wf-border);
  padding-bottom: var(--wf-spacing-sm);
}

.back-button {
  text-decoration: none;
  font-weight: bold;
}

.story-card {
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: var(--wf-spacing-md);
}

.story-title-box {
  border: 1px solid var(--wf-border);
  padding: var(--wf-spacing-md);
  text-align: center;
  background: var(--wf-button-bg);
}

.story-title-box h2 {
  margin: 0;
  font-size: 1.5rem;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.wf-divider {
  border: none;
  border-top: 2px solid var(--wf-border);
  margin: var(--wf-spacing-sm) 0;
}

/* Image grid logic for 1 or 2 images */
.story-images-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--wf-spacing-md);
  width: 100%;
}

.story-images-container.double-images {
  grid-template-columns: 1fr 1fr;
}

.story-image-wrapper {
  border: 1px solid var(--wf-border);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  background: #fdfdfd;
}

.story-image {
  width: 100%;
  height: auto;
  max-height: 400px;
  object-fit: cover;
  display: block;
}

/* Wireframe placeholder styles */
.story-image-placeholder {
  border: 1px dashed var(--wf-border);
  padding: 4rem 2rem;
  text-align: center;
  background: #fafafa;
}

.placeholder-icon {
  font-size: 3rem;
  display: block;
  margin-bottom: var(--wf-spacing-sm);
}

/* Metadata row styling */
.story-meta {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: var(--wf-spacing-lg);
  font-size: 1.1rem;
  padding: var(--wf-spacing-sm) 0;
}

.meta-separator {
  color: var(--wf-border);
  font-weight: bold;
}

/* Description formatting */
.story-description {
  font-size: 1rem;
  line-height: 1.7;
}

.story-description p {
  margin-bottom: var(--wf-spacing-md);
  text-align: justify;
}

/* Responsive adjustments */
@media (max-width: 600px) {
  .story-images-container.double-images {
    grid-template-columns: 1fr;
  }
  .story-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: var(--wf-spacing-sm);
  }
  .meta-separator {
    display: none;
  }
}
</style>
