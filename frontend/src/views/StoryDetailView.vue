<template>
  <div class="story-detail-template">
    <header class="template-header">
      <button class="wireframe-button back-button" @click="goBack">
        ← Volver
      </button>
    </header>

    <main class="template-content">
      <div v-if="loading" class="loading-text">Cargando historia...</div>

      <div v-else-if="!storyToShow" class="loading-text">Historia no encontrada.</div>

      <div v-else class="wireframe-container story-card">
        <div class="story-title-box">
          <h2>{{ storyToShow.title }}</h2>
        </div>

        <hr class="wf-divider" />

        <div class="story-images-container" :class="{ 'double-images': storyToShow.images.length === 2 }">
          <template v-if="storyToShow.images.length > 0">
            <div
              v-for="(img, idx) in storyToShow.images"
              :key="idx"
              class="story-image-wrapper"
            >
              <img :src="img.url || img" :alt="'Imagen de la historia'" class="story-image" />
            </div>
          </template>
          <template v-else>
            <div class="story-image-placeholder">
              <span class="placeholder-icon"></span>
              <p>IMAGEN DE LA HISTORIA</p>
            </div>
          </template>
        </div>

        <div class="story-meta">
          <span class="meta-item"><strong>Oficio:</strong> {{ professionLabel }}</span>
          <span class="meta-separator">│</span>
          <span class="meta-item"><strong>Edad:</strong> {{ storyToShow.age }} años</span>
          <span class="meta-separator">│</span>
          <span class="meta-item"><strong>País:</strong> {{ storyToShow.originCountry || storyToShow.origin_country }}</span>
        </div>

        <hr class="wf-divider" />

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
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useStoryStore } from '../composables/useStoryStore'
import { getStoryById } from '../api/stories'

const router = useRouter()
const route = useRoute()
const { currentStory, setStory } = useStoryStore()

const loading = ref(false)
const storyToShow = ref(null)

const goBack = () => {
  router.push('/')
}

const professionLabel = computed(() => {
  const mapping = {
    casa: 'Casa',
    campo: 'Campo',
    industria: 'Industria',
    limpieza: 'Limpieza',
    otro: 'Otro'
  }
  return mapping[storyToShow.value?.profession] || 'No especificado'
})

const formattedDescription = computed(() => {
  if (!storyToShow.value?.description && !storyToShow.value?.content) return []
  const text = storyToShow.value.description || storyToShow.value.content
  return text.split('\n\n').filter(p => p.trim() !== '')
})

const loadStory = async (id) => {
  loading.value = true
  try {
    if (currentStory.id == id) {
      storyToShow.value = currentStory
    } else {
      const data = await getStoryById(id)
      setStory({
        id: data.id,
        title: data.title,
        profession: data.profession,
        age: data.age,
        description: data.content,
        images: data.images || []
      })
      storyToShow.value = currentStory
    }
  } catch {
    storyToShow.value = null
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  const id = Number(route.params.id)
  if (id) loadStory(id)
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

.loading-text {
  text-align: center;
  padding: var(--wf-spacing-lg);
  font-weight: bold;
  color: var(--wf-text);
  border: 2px dashed var(--wf-border);
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

.story-description {
  font-size: 1rem;
  line-height: 1.7;
}

.story-description p {
  margin-bottom: var(--wf-spacing-md);
  text-align: justify;
}

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
