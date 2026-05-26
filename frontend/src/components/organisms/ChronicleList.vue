<template>
  <div class="chronicles-section">
    <div class="filters-header">
      <h3 class="filter-title">{{ t('chronicles.filterBy') }}</h3>
      <div class="filters-row">
        <select class="wireframe-input filter-select">
          <option value="">{{ t('chronicles.allTrades') }}</option>
        </select>
        <select class="wireframe-input filter-select">
          <option value="">{{ t('chronicles.birthDate') }}</option>
        </select>
        <select class="wireframe-input filter-select">
          <option value="">{{ t('chronicles.allContinents') }}</option>
        </select>
      </div>
      <div class="elegant-divider"></div>
    </div>

    <div v-if="loading" class="loading-text">{{ t('chronicles.loading') }}</div>

    <div v-else-if="errorMessage" class="error-message">{{ errorMessage }}</div>

    <div v-else-if="stories.length === 0" class="loading-text">
      {{ t('chronicles.noStories') }}
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
            <span>{{ t('chronicles.noImage') }}</span>
          </div>

          <div class="card-content">
            <div class="card-meta">
              {{ t('chronicles.trade') }}: {{ professionLabel(story.profession) }} &nbsp;|&nbsp;
              {{ t('chronicles.age') }}: {{ ageLabel(story.age_range) }} &nbsp;|&nbsp;
              {{ t('chronicles.country') }}: {{ story.origin_country }}
            </div>
            <p class="card-text">{{ truncate(story.content, 120) }}</p>
            <div class="card-actions">
              <button class="wireframe-button" @click="goToStoryDetail(story.id)">{{ t('chronicles.viewMore') }}</button>
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
import { useI18n } from 'vue-i18n'
import { getStories } from '../../api/stories'

const { t } = useI18n()
const router = useRouter()

const stories = ref([])
const loading = ref(true)
const errorMessage = ref('')
const filters = reactive({
  profession: '',
  age_range: ''
})

const professionOptions = [
  { label: t('professions.casa'), value: 'casa' },
  { label: t('professions.campo'), value: 'campo' },
  { label: t('professions.industria'), value: 'industria' },
  { label: t('professions.limpieza'), value: 'limpieza' },
  { label: t('professions.otro'), value: 'otro' }
]

const ageOptions = [
  { label: t('ages.under_18'), value: 'under_18' },
  { label: t('ages.18_25'), value: '18_25' },
  { label: t('ages.26_35'), value: '26_35' },
  { label: t('ages.36_45'), value: '36_45' },
  { label: t('ages.46_60'), value: '46_60' },
  { label: t('ages.over_60'), value: 'over_60' }
]

const professionMap = {
  casa: 'casa',
  campo: 'campo',
  industria: 'industria',
  limpieza: 'limpieza',
  otro: 'otro'
}

const ageMap = {
  under_18: 'under_18',
  '18_25': '18_25',
  '26_35': '26_35',
  '36_45': '36_45',
  '46_60': '46_60',
  over_60: 'over_60'
}

const KNOWN_PROFESSIONS = ['casa', 'campo', 'industria', 'limpieza', 'otro']
const KNOWN_AGES = ['under_18', '18_25', '26_35', '36_45', '46_60', 'over_60']

const professionLabel = (val) => {
  if (!val) return val
  const key = val.toLowerCase().replace(/\s+/g, '_')
  return KNOWN_PROFESSIONS.includes(key) ? t(`professions.${key}`) : val
}

const ageLabel = (val) => {
  if (!val) return val
  const key = val.toLowerCase()
  return KNOWN_AGES.includes(key) ? t(`ages.${key}`) : val
}

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
  color: var(--color-yellow);
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
  background: var(--color-yellow);
  margin-bottom: var(--wf-spacing-lg);
}

.chronicle-card {
  padding: 0;
  display: flex;
  flex-direction: column;
  border: none;
  border-radius: 12px;
  background: var(--color-red);
  transition: all 0.3s ease;
  color: var(--color-white);
}

/* Chronicles List */
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
  background: var(--color-red);
  transition: all 0.3s ease;
  color: var(--color-white);
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
  width: 180px;
  height: 16px;
  background: rgba(255, 255, 255, 0.35);
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
  color: var(--color-white);
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
  color: var(--color-white);
  margin-bottom: var(--wf-spacing-lg);
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
