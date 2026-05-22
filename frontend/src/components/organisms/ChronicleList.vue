<template>
  <div class="chronicles-section">
    <div class="filters-header">
      <h3 class="filter-title">FILTRAR POR</h3>
      <div class="filters-row">
        <select v-model="filters.profession" class="wireframe-input filter-select" @change="applyFilters">
          <option value="">Oficio (todos)</option>
          <option v-for="opt in professionOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
        </select>
        <select v-model="filters.age_range" class="wireframe-input filter-select" @change="applyFilters">
          <option value="">Edad (todas)</option>
          <option v-for="opt in ageOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
        </select>
      </div>
      <div class="elegant-divider"></div>
    </div>

    <div v-if="filterCountry" class="active-filter-bar">
      <span class="filter-label">Mostrando historias de: <strong>{{ filterCountry }}</strong></span>
      <button class="wireframe-button clear-filter-btn" @click="$emit('clear-filter')">Mostrar todas</button>
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
import { ref, reactive, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { getStories } from '../../api/stories'

const props = defineProps({
  filterCountry: { type: String, default: '' }
})

defineEmits(['clear-filter'])

const router = useRouter()

const stories = ref([])
const loading = ref(true)
const errorMessage = ref('')
const filters = reactive({
  profession: '',
  age_range: ''
})

const professionOptions = [
  { label: 'Servicios Domésticos', value: 'servicios_domesticos' },
  { label: 'Trabajo Social', value: 'trabajo_social' },
  { label: 'Educación', value: 'educacion' },
  { label: 'cuidados', value: 'cuidados' },  
  { label: 'Sanidad', value: 'sanidad' },
  { label: 'Gestión Administrativa', value: 'gestion_administrativa' },
  { label: 'Hosteleria', value: 'hosteleria' },
  { label: 'Industria', value: 'industria' },
  { label: 'Agricultura', value: 'agricultura' },
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
  servicios_domesticos: 'Servicios Domésticos',
  trabajo_social: 'Trabajo Social',
  educacion: 'Educación',
  cuidados: 'Cuidados',
  sanidad: 'Sanidad',
  gestion_administrativa: 'Gestión Administrativa',
  hosteleria: 'Hostelería',
  industria: 'Industria',
  agricultura: 'Agricultura',
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
    if (props.filterCountry) f.origin_country = props.filterCountry
    stories.value = await getStories(f)
  } catch (err) {
    stories.value = []
    errorMessage.value = err.message
  } finally {
    loading.value = false
  }
}

watch(() => props.filterCountry, () => {
  fetchStories()
})

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
  margin-top: var(--wf-spacing-lg);
  padding: 0;
}

.filters-header {
  margin-bottom: var(--wf-spacing-lg);
}

.filter-title {
  font-size: 1rem;
  font-weight: bold;
  color: var(--wf-text);
  margin-bottom: var(--wf-spacing-sm);
  text-transform: uppercase;
  letter-spacing: 1px;
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
  background: var(--wf-border);
  margin-bottom: var(--wf-spacing-lg);
}

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

.chronicles-list {
  display: flex;
  flex-direction: column;
  gap: var(--wf-spacing-lg);
}

.chronicle-card {
  padding: 0;
  display: flex;
  flex-direction: column;
  border: 2px solid var(--wf-border);
  background: var(--wf-bg);
  transition: all 0.3s ease;
}

.chronicle-card:hover {
  box-shadow: 4px 4px 0px var(--wf-border);
  transform: translate(-2px, -2px);
}

.card-top-bar {
  background: var(--wf-button-bg);
  border-bottom: 2px solid var(--wf-border);
  padding: 8px 16px;
  display: flex;
}

.card-top-bar-inner {
  font-weight: bold;
  font-size: 0.95rem;
  letter-spacing: 1px;
  text-transform: uppercase;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.card-body {
  display: flex;
  gap: var(--wf-spacing-lg);
  padding: var(--wf-spacing-lg);
}

.card-image-box {
  width: 200px;
  height: 200px;
  background: var(--wf-button-bg);
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--wf-text);
  font-weight: bold;
  border: 2px solid var(--wf-border);
  flex-shrink: 0;
  text-transform: uppercase;
  letter-spacing: 2px;
  overflow: hidden;
}

.card-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.card-meta {
  font-weight: bold;
  color: var(--wf-text);
  margin-bottom: var(--wf-spacing-md);
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

.active-filter-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--wf-spacing-md);
  margin-bottom: var(--wf-spacing-lg);
  border: 2px solid var(--wf-border);
  background: var(--wf-button-bg);
}

.filter-label {
  font-size: 1rem;
  color: var(--wf-text);
}

.clear-filter-btn {
  font-size: 0.85rem;
  padding: 4px 12px;
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
