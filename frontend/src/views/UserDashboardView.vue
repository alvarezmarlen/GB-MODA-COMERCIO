<template>
  <DashboardTemplate title="Mi Perfil">
    <section class="wireframe-container profile-section">
      <div class="section-header">
        <h2 class="section-title">DATOS PERSONALES</h2>
        <button class="wireframe-button" @click="toggleEditMode">
          {{ isEditing ? '✕ Cancelar' : '✎ Editar' }}
        </button>
      </div>
      <div class="profile-fields">
        <div class="profile-field">
          <label class="wireframe-label">Nombre de usuario</label>
          <input v-if="isEditing" v-model="editData.username" class="wireframe-input" type="text" />
          <div v-else class="field-value">{{ user.username }}</div>
        </div>
        <div class="profile-field">
          <label class="wireframe-label">Correo electrónico</label>
          <input v-if="isEditing" v-model="editData.email" class="wireframe-input" type="email" />
          <div v-else class="field-value">{{ user.email }}</div>
        </div>
        <div class="profile-field">
          <label class="wireframe-label">Contraseña</label>
          <input v-if="isEditing" v-model="editData.password" class="wireframe-input" type="password" placeholder="Nueva contraseña" />
          <div v-else class="field-value">••••••••</div>
        </div>
      </div>
      <div v-if="isEditing" class="save-actions">
        <button class="wireframe-button save-btn" @click="saveChanges">✓ Guardar Cambios</button>
      </div>
    </section>

    <section class="wireframe-container stories-section">
      <div class="section-header">
        <h2 class="section-title">MIS HISTORIAS</h2>
        <span class="story-count">{{ userStories.length }} historia(s)</span>
      </div>
      <div v-if="userStories.length > 0" class="user-stories-list">
        <div v-for="story in userStories" :key="story.id" class="user-story-card">
          <div class="story-card-top-bar"><div class="top-bar-inner"></div></div>
          <div class="story-card-body">
            <div v-if="story.images && story.images.length > 0" class="story-card-image-box">
              <img :src="story.images[0].url" :alt="story.title" class="story-card-image" />
            </div>
            <div v-else class="story-card-image-box"><span>Sin imagen</span></div>
            <div class="story-card-content">
              <h3 class="story-card-title">{{ story.title }}</h3>
              <div class="story-card-meta">Oficio: {{ getProfLabel(story.profession) }} &nbsp;|&nbsp; Edad: {{ getAgeLabel(story.age_range) }}</div>
              <p class="story-card-excerpt">{{ story.content?.substring(0, 100) }}{{ story.content?.length > 100 ? '...' : '' }}</p>
              <button class="wireframe-button" @click="goToDetail(story.id)">Ver más</button>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="empty-state">
        <div class="empty-icon-box"><span class="empty-icon">☐</span></div>
        <p class="empty-text">Aún no has subido ninguna historia.</p>
        <p class="empty-subtext">Comparte tu primera crónica con la comunidad.</p>
        <button class="wireframe-button" @click="$router.push('/create-story')">+ Crear Historia</button>
      </div>
    </section>
  </DashboardTemplate>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../composables/useAuthStore'
import { getStories } from '../api/stories'
import { updateUser as apiUpdateUser } from '../api/users'
import DashboardTemplate from '../components/templates/DashboardTemplate.vue'

const router = useRouter()

const { user, updateUser } = useAuthStore()
const isEditing = ref(false)
const editData = reactive({ username: '', email: '', password: '' })

const userStories = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    userStories.value = await getStories({ user_id: user.value.id })
  } catch {
    userStories.value = []
  } finally {
    loading.value = false
  }
})

const toggleEditMode = () => {
  if (!isEditing.value) {
    editData.username = user.value.username
    editData.email = user.value.email
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
    const updated = await apiUpdateUser(user.value.id, payload)
    updateUser({ username: updated.username, email: updated.email })
    isEditing.value = false
    alert('Datos actualizados con éxito')
  } catch {
    alert('Error al actualizar los datos')
  }
}

const goToDetail = (id) => router.push({ name: 'story-detail', params: { id } })

const getProfLabel = (k) => ({ casa:'Casa', campo:'Campo', industria:'Industria', limpieza:'Limpieza', otro:'Otro' }[k] || 'N/A')
const getAgeLabel = (k) => ({ under_18:'<18', '18_25':'18-25', '26_35':'26-35', '36_45':'36-45', '46_60':'46-60', over_60:'>60' }[k] || 'N/A')
</script>

<style scoped>
.profile-section, .stories-section { padding: var(--wf-spacing-lg) !important; }
.section-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:var(--wf-spacing-lg); border-bottom:2px solid var(--wf-border); padding-bottom:var(--wf-spacing-sm); }
.section-title { font-size:1.1rem; letter-spacing:2px; text-transform:uppercase; margin:0; }
.profile-fields { display:flex; flex-direction:column; gap:var(--wf-spacing-md); }
.profile-field { display:flex; flex-direction:column; gap:4px; }
.field-value { padding:var(--wf-spacing-sm); border:1px dashed var(--wf-placeholder); background:#fafafa; min-height:38px; display:flex; align-items:center; }
.save-actions { display:flex; justify-content:flex-end; margin-top:var(--wf-spacing-lg); padding-top:var(--wf-spacing-md); border-top:1px solid var(--wf-placeholder); }
.save-btn { background:var(--wf-border); color:var(--wf-bg); }
.save-btn:hover { background:#333; }
.story-count { font-size:0.85rem; border:1px dashed var(--wf-border); padding:4px 10px; border-radius:var(--wf-radius); }
.user-stories-list { display:flex; flex-direction:column; gap:var(--wf-spacing-md); }
.user-story-card { border:2px solid var(--wf-border); background:var(--wf-bg); display:flex; flex-direction:column; transition:all 0.3s ease; }
.user-story-card:hover { box-shadow:4px 4px 0px var(--wf-border); transform:translate(-2px,-2px); }
.story-card-top-bar { background:var(--wf-button-bg); border-bottom:2px solid var(--wf-border); padding:6px 16px; }
.top-bar-inner { width:120px; height:12px; background:var(--wf-placeholder); }
.story-card-body { display:flex; gap:var(--wf-spacing-md); padding:var(--wf-spacing-md); }
.story-card-image-box { width:120px; height:120px; background:var(--wf-button-bg); display:flex; justify-content:center; align-items:center; font-weight:bold; border:2px solid var(--wf-border); flex-shrink:0; text-transform:uppercase; letter-spacing:1px; font-size:0.8rem; overflow:hidden; }
.story-card-image { width:100%; height:100%; object-fit:cover; }
.story-card-content { flex:1; display:flex; flex-direction:column; gap:var(--wf-spacing-sm); }
.story-card-title { font-size:1rem; text-transform:uppercase; letter-spacing:1px; margin:0; }
.story-card-meta { font-size:0.85rem; font-weight:bold; }
.story-card-excerpt { font-size:0.85rem; line-height:1.5; margin:0; }
.empty-state { display:flex; flex-direction:column; align-items:center; padding:var(--wf-spacing-lg) 0; gap:var(--wf-spacing-sm); }
.empty-icon-box { width:80px; height:80px; border:2px dashed var(--wf-placeholder); display:flex; justify-content:center; align-items:center; margin-bottom:var(--wf-spacing-sm); }
.empty-icon { font-size:2rem; color:var(--wf-placeholder); }
.empty-text { font-weight:bold; margin:0; }
.empty-subtext { font-size:0.85rem; color:var(--wf-placeholder); margin:0 0 var(--wf-spacing-sm) 0; }
@media (max-width:600px) {
  .section-header { flex-direction:column; gap:var(--wf-spacing-sm); }
  .story-card-body { flex-direction:column; align-items:center; }
  .story-card-image-box { width:100%; max-width:200px; }
}
</style>
