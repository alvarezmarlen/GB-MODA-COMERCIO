<template>
  <div class="chronicles-section">
    <div class="filters-header">
      <h3 class="filter-title">Filtrado</h3>
      <div class="filters-row">
        <select class="wireframe-input filter-select">
          <option value="">Profesion u oficio</option>
        </select>
        <select class="wireframe-input filter-select">
          <option value="">Fecha de nacimiento</option>
        </select>
        <select class="wireframe-input filter-select">
          <option value="">Continente</option>
        </select>
      </div>
      <div class="elegant-divider"></div>
    </div>

    <div v-if="loading" class="loading-text">Cargando historias...</div>

    <div v-else-if="errorMessage" class="error-message">{{ errorMessage }}</div>

    <div v-else-if="stories.length === 0" class="loading-text">
      No hay historias disponibles.
    </div>

    <div v-else class="chronicles-list">
      <div
        v-for="story in stories"
        :key="story.id"
        class="chronicle-card wireframe-container"
      >
        <div class="card-top-bar">
          <div class="card-top-bar-inner">{{ story.title }}</div>
        </div>

        <div class="card-body">
          <div v-if="story.images && story.images.length > 0" class="card-image-box">
            <img :src="story.images[0].url" :alt="story.title" class="card-image" />
          </div>
          <div v-else class="card-image-box">
            <span>Sin imagen</span>
          </div>

          <div class="card-content">
            <div class="card-meta">
              Oficio: {{ professionLabel(story.profession) }} &nbsp;|&nbsp;
              Edad: {{ ageLabel(story.age_range) }} &nbsp;|&nbsp;
              País: {{ story.origin_country }}
            </div>
            <p class="card-text">{{ truncate(story.content, 120) }}</p>
            <div class="card-actions">
              <button class="wireframe-button" @click="goToStoryDetail(story.id)">Ver más</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getStories } from '../../api/stories'

const router = useRouter()

const stories = ref([])
const loading = ref(true)
const errorMessage = ref('')
const filters = reactive({
  profession: '',
  age_range: ''
})

const professionOptions = [
  { label: 'Casa', value: 'casa' },
  { label: 'Campo', value: 'campo' },
  { label: 'Industria', value: 'industria' },
  { label: 'Limpieza', value: 'limpieza' },
  { label: 'Otro', value: 'otro' }
]

const ageOptions = [
  { label: 'Menor de 18', value: 'under_18' },
  { label: '18 - 25 años', value: '18_25' },
  { label: '26 - 35 años', value: '26_35' },
  { label: '36 - 45 años', value: '36_45' },
  { label: '46 - 60 años', value: '46_60' },
  { label: 'Más de 60', value: 'over_60' }
]

const professionMap = {
  casa: 'Casa',
  campo: 'Campo',
  industria: 'Industria',
  limpieza: 'Limpieza',
  otro: 'Otro'
}

const ageMap = {
  under_18: 'Menor de 18',
  '18_25': '18 - 25 años',
  '26_35': '26 - 35 años',
  '36_45': '36 - 45 años',
  '46_60': '46 - 60 años',
  over_60: 'Más de 60'
}

const professionLabel = (val) => professionMap[val] || val
const ageLabel = (val) => ageMap[val] || val

const truncate = (text, max) => {
  if (!text) return ''
  return text.length > max ? text.slice(0, max) + '...' : text
}

const fetchStories = async () => {
  loading.value = true
  errorMessage.value = ''
  try {
    const f = {}
    if (filters.profession) f.profession = filters.profession
    if (filters.age_range) f.age_range = filters.age_range
    stories.value = await getStories(f)
  } catch (err) {
    stories.value = []
    errorMessage.value = err.message
  } finally {
    loading.value = false
  }
}

const applyFilters = () => {
  fetchStories()
}

const goToStoryDetail = (id) => {
  router.push({ name: 'story-detail', params: { id } })
}

onMounted(fetchStories)
</script>

<style scoped>
.chronicles-section {
  width: 100%;
  max-width: 1100px;
  margin: var(--wf-spacing-lg) auto 0;
  padding: 0 32px;
  box-sizing: border-box;
}

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
  width: 300px;
  cursor: pointer;
  background: var(--wf-bg);
  color: var(--wf-text);
  appearance: none;
  background-repeat: no-repeat;
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

<<<<<<< HEAD
.loading-text {
  text-align: center;
  padding: var(--wf-spacing-lg);
  font-weight: bold;
  color: var(--wf-text);
  border: 2px dashed var(--wf-border);
}

.error-message {
  text-align: center;
  padding: var(--wf-spacing-lg);
  font-weight: bold;
  color: #d32f2f;
  background: #fce4ec;
  border: 1px solid #d32f2f;
}

=======
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
>>>>>>> 6ed8127b298c299995bd9f118e8e76e019848375
.chronicles-list {
  display: flex;
  flex-direction: column;
  gap: var(--wf-spacing-lg);
  align-items: center;
}

.chronicle-card {
  width: min(100%, 9900px);
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

.card-top-bar {
  background: rgba(255, 255, 255, 0.14);
  border-bottom: 2px solid rgba(255, 255, 255, 0.4);
  padding: 8px 16px;
  display: flex;
}

.card-top-bar-inner {
<<<<<<< HEAD
  font-weight: bold;
  font-size: 0.95rem;
  letter-spacing: 1px;
  text-transform: uppercase;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
=======
  width: 180px;
  height: 16px;
  background: rgba(255, 255, 255, 0.35);
>>>>>>> 6ed8127b298c299995bd9f118e8e76e019848375
}

.card-body {
  display: flex;
  gap: calc(var(--wf-spacing-lg) * 1.2);
  padding: var(--wf-spacing-lg);
}

.card-image-box {
  width: 240px;
  height: 240px;
  background: rgba(255, 255, 255, 0.12);
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--color-blanco);
  font-weight: bold;
  border: none;
  flex-shrink: 0;
<<<<<<< HEAD
  text-transform: uppercase;
  letter-spacing: 2px;
  overflow: hidden;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
=======
  text-transform: none;
  letter-spacing: 0;
>>>>>>> 6ed8127b298c299995bd9f118e8e76e019848375
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.card-meta {
  font-weight: bold;
<<<<<<< HEAD
  color: var(--wf-text);
  margin-bottom: var(--wf-spacing-md);
=======
  color: var(--color-blanco);
  margin-bottom: var(--wf-spacing-lg);
>>>>>>> 6ed8127b298c299995bd9f118e8e76e019848375
  font-size: 1.1rem;
}

.card-text {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--wf-text);
  margin: 0 0 var(--wf-spacing-md);
  text-align: justify;
}

.card-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: auto;
}

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
