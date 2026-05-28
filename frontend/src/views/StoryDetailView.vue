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
        <div v-if="loading" class="loading-text">Cargando historia...</div>
        <div v-else-if="!storyToShow" class="loading-text">Historia no encontrada.</div>
        <div v-else class="story-card">
          <div class="story-title-box">
            <h2>{{ storyToShow.title }}</h2>
          </div>

          <div class="story-images-container" :class="{ 'double-images': storyToShow?.images?.length === 2 }">
            <template v-if="storyToShow?.images?.length > 0">
              <div
                v-for="(img, idx) in storyToShow.images"
                :key="idx"
                class="story-image-wrapper"
              >
                <img :src="img.url || img" alt="Imagen de la historia" class="story-image" />
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
            <span class="meta-item"><strong>Continente:</strong> {{ storyToShow.originCountry || 'No especificado' }}</span>
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
  return mapping[storyToShow.value?.profession] || storyToShow.value?.profession || 'No especificado'
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
  return mapping[storyToShow.value?.ageRange || storyToShow.value?.age_range] || storyToShow.value?.ageRange || storyToShow.value?.age_range || 'No especificada'
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
        originCountry: data.origin_country,
        ageRange: data.age_range,
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
  font-weight: bold;
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
  margin-bottom: 20px;
  border: 1px solid var(--color-primary);
  border-radius: var(--wf-radius);
  overflow: hidden;
}

.story-image {
  width: 100%;
  height: auto;
  display: block;
}

.story-image-placeholder {
  border: 1px dashed var(--color-primary);
  padding: 4rem 2rem;
  text-align: center;
  background: #fafafa;
}

.story-meta {
  display: flex;
  gap: 20px;
  margin: 20px 0;
  font-weight: bold;
  flex-wrap: wrap;
}

.story-description p {
  line-height: 1.7;
  margin-bottom: 15px;
  word-wrap: break-word;
  overflow-wrap: break-word;
  word-break: break-word;
  white-space: pre-wrap;
  hyphens: auto;
}

.loading-text {
  text-align: center;
  padding: var(--wf-spacing-lg);
  font-weight: bold;
  color: var(--wf-text);
  border: 2px dashed var(--wf-border);
  background: var(--wf-bg);
  border-radius: var(--wf-radius);
}

@media (max-width: 680px) {
  .story-detail-template {
    padding-top: 140px;
  }
}
</style>
