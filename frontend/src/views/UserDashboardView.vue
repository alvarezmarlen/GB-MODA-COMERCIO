<template>
  <DashboardTemplate :title= "t('dashboard.title')" >
    <section class="profile-section">
      <div class="section-header">
        <h2 class="section-title">{{ t('dashboard.personalData') }}</h2>
        <button class="custom-button" @click="toggleEditMode">
          {{ isEditing ? t('dashboard.cancel') :  t('dashboard.edit') }}
        </button>
      </div>
      <div class="profile-fields">
        <div class="profile-field">
          <label class="custom-label">{{ t('dashboard.usernameLabel') }}</label>
          <input v-if="isEditing" v-model="editData.username" class="wireframe-input" type="text" />
          <div v-else class="field-value">{{ user.username }}</div>
        </div>
        <div class="profile-field">
          <label class="custom-label">{{ t('dashboard.emailLabel') }}</label>
          <input v-if="isEditing" v-model="editData.email" class="wireframe-input" type="email" />
          <div v-else class="field-value">{{ user.email }}</div>
        </div>
        <div class="profile-field">
          <label class="custom-label">{{ t('dashboard.passwordLabel') }}</label>
          <input v-if="isEditing" v-model="editData.password" class="wireframe-input" type="password" placeholder="t('auth.passwordNewPlaceholder')" />
          <div v-else class="field-value">••••••••</div>
        </div>
      </div>
      <div v-if="isEditing" class="save-actions">
        <button class="custom-button save-btn" @click="saveChanges">{{ t('dashboard.saveChanges') }}</button>
      </div>
    </section>

    <section class="stories-section">
      <div class="section-header">
        <h2 class="section-title">{{ t('dashboard.myStories') }}</h2>
        <span class="story-count">{{ userStories.length }} {{ t('dashboard.storyCount') }}</span>
      </div>
      <div v-if="errorMessage" class="error-banner">{{ errorMessage }}</div>
      <div v-if="userStories.length > 0" class="user-stories-list">
        <div v-for="story in userStories" :key="story.id" class="user-story-card">
          <div class="story-card-top-bar"><div class="top-bar-inner"></div></div>
          <div class="story-card-body">
            <div v-if="story.images && story.images.length > 0" class="story-card-image-box">
              <img :src="story.images[0].url" :alt="story.title" class="story-card-image" />
            </div>
            <div v-else class="story-card-image-box"><span>{{ t('dashboard.noImage') }}</span></div>
            <div class="story-card-content">
              <h3 class="story-card-title">{{ story.title }}</h3>
              <div class="story-card-meta">{{ t('dashboard.trade') }}: {{ t(story.profession) }} &nbsp;|&nbsp; {{ t('dashboard.age') }}: {{ getAgeLabel(story.age_range) }}</div>
              <p class="story-card-excerpt">{{ story.content?.substring(0, 100) }}{{ story.content?.length > 100 ? '...' : '' }}</p>
              <button class="custom-button" @click="goToDetail(story.id)">{{ t('dashboard.viewMore') }}</button>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="empty-state">
        <div class="empty-icon-box"><span class="empty-icon">☐</span></div>
        <p class="empty-text">{{ t('dashboard.emptyTitle') }}</p>
        <p class="empty-subtext">{{ t('dashboard.emptySubtext') }}</p>
        <button class="custom-button" @click="$router.push('/create-story')">{{ t('dashboard.createFirstStory') }}</button>
      </div>
    </section>
  </DashboardTemplate>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useAuthStore } from '../composables/useAuthStore'
import { getStories } from '../api/stories'
import { updateUser as apiUpdateUser } from '../api/users'
import DashboardTemplate from '../components/templates/DashboardTemplate.vue'

const { t } = useI18n()
const router = useRouter()

const { user, updateUser } = useAuthStore()
const isEditing = ref(false)
const editData = reactive({ username: '', email: '', password: '' })

const userStories = ref([])
const loading = ref(true)
const errorMessage = ref('')

onMounted(async () => {
  try {
    userStories.value = await getStories({ user_id: user.id })
  } catch {
    userStories.value = []
  } finally {
    loading.value = false
  }
})

const toggleEditMode = () => {
  if (!isEditing.value) {
    editData.username = user.username
    editData.email = user.email
    editData.password = ''
  }
  isEditing.value = !isEditing.value
}

const saveChanges = async () => {
  const payload = {}
  if (editData.username) payload.nombre_usuario = editData.username
  if (editData.email) payload.email = editData.email
  if (editData.password) payload.password = editData.password
  try {
    const updated = await apiUpdateUser(user.id, payload)
    updateUser({ username: updated.username, email: updated.email })
    isEditing.value = false
    alert('Datos actualizados con éxito')
  } catch (err) {
    alert('Error al actualizar los datos: ' + err.message)
  }
}

const goToDetail = (id) => router.push({ name: 'story-detail', params: { id } })

const getProfLabel = (k) => k ? t(`professions.${k}`) : 'N/A'
const getAgeLabel = (k) => k ? t(`ages.${k}`) : 'N/A'
</script>

<style scoped>
.custom-button { background:var(--color-red); color:var(--color-white); border:none; border-radius:var(--wf-radius); padding:8px 16px; cursor:pointer; font-weight:bold; }
.custom-label { display:block; font-size:0.85rem; font-weight:bold; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px; }
.profile-section, .stories-section { padding:var(--wf-spacing-lg); border:1px solid var(--color-red); border-radius:var(--wf-radius); margin-bottom:20px; background-color:var(--color-white); }
.section-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:var(--wf-spacing-lg); border-bottom:2px solid var(--color-red); padding-bottom:var(--wf-spacing-sm); }
.section-title { font-size:1.1rem; letter-spacing:2px; text-transform:uppercase; margin:0; color:var(--color-yellow); }
.profile-fields { display:flex; flex-direction:column; gap:var(--wf-spacing-md); }
.profile-field { display:flex; flex-direction:column; gap:4px; }
.field-value { padding:var(--wf-spacing-sm); border:1px solid var(--color-primary); background:#fafafa; min-height:38px; display:flex; align-items:center; border-radius:var(--wf-radius); }
.save-actions { display:flex; justify-content:flex-end; margin-top:var(--wf-spacing-lg); padding-top:var(--wf-spacing-md); border-top:1px solid var(--color-primary); }
.save-btn { background:var(--color-red); color:var(--color-white); }
.save-btn:hover { background:#333; }
.story-count { font-size:0.85rem; border:1px solid var(--color-red); padding:4px 10px; border-radius:var(--wf-radius); color:var(--color-red); }
.user-stories-list { display:flex; flex-direction:column; gap:var(--wf-spacing-md); }
.user-story-card { border:1px solid var(--color-primary); background:#fff; display:flex; flex-direction:column; transition:all 0.3s ease; border-radius:var(--wf-radius); padding:10px; }
.story-card-top-bar { padding:6px 16px; }
.top-bar-inner { width:120px; height:12px; background:var(--wf-placeholder); }
.story-card-body { display:flex; gap:var(--wf-spacing-md); padding:var(--wf-spacing-md); }
.story-card-image-box { width:120px; height:120px; background:var(--wf-button-bg); display:flex; justify-content:center; align-items:center; font-weight:bold; border:1px solid var(--color-primary); flex-shrink:0; text-transform:uppercase; letter-spacing:1px; font-size:0.8rem; overflow:hidden; }
.story-card-image { width:100%; height:100%; object-fit:cover; }
.story-card-content { flex:1; display:flex; flex-direction:column; gap:var(--wf-spacing-sm); }
.story-card-title { font-size:1rem; text-transform:uppercase; letter-spacing:1px; margin:0; }
.story-card-meta { font-size:0.85rem; font-weight:bold; }
.story-card-excerpt { font-size:0.85rem; line-height:1.5; margin:0; }
.empty-state { display:flex; flex-direction:column; align-items:center; padding:var(--wf-spacing-lg) 0; gap:var(--wf-spacing-sm); }
.empty-icon-box { width:80px; height:80px; border:1px dashed var(--color-primary); display:flex; justify-content:center; align-items:center; margin-bottom:var(--wf-spacing-sm); }
.empty-icon { font-size:2rem; color:var(--color-primary); }
.empty-text { font-weight:bold; margin:0; }
.empty-subtext { font-size:0.85rem; color:var(--color-primary); margin:0 0 var(--wf-spacing-sm) 0; }
@media (max-width:600px) {
  .section-header { flex-direction:column; gap:var(--wf-spacing-sm); }
  .story-card-body { flex-direction:column; align-items:center; }
  .story-card-image-box { width:100%; max-width:200px; }
}
</style>
