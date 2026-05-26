<template>
  <DashboardTemplate title="Mi Perfil">
    <section class="profile-section">
      <div class="section-header">
        <h2 class="section-title">DATOS PERSONALES</h2>
        <button class="custom-button" @click="toggleEditMode">
          {{ isEditing ? '✕ Cancelar' : '✎ Editar' }}
        </button>
      </div>
      <div class="profile-fields">
        <div class="profile-field">
          <label class="custom-label">Nombre de usuario</label>
          <input v-if="isEditing" v-model="editData.username" class="wireframe-input" type="text" />
          <div v-else class="field-value">{{ user.username }}</div>
        </div>
        <div class="profile-field">
          <label class="custom-label">Correo electrónico</label>
          <input v-if="isEditing" v-model="editData.email" class="wireframe-input" type="email" />
          <div v-else class="field-value">{{ user.email }}</div>
        </div>
        <div class="profile-field">
          <label class="custom-label">Contraseña</label>
          <input v-if="isEditing" v-model="editData.password" class="wireframe-input" type="password" placeholder="Nueva contraseña" />
          <div v-else class="field-value">••••••••</div>
        </div>
      </div>
      <div v-if="isEditing" class="save-actions">
        <button class="custom-button save-btn" @click="saveChanges">✓ Guardar Cambios</button>
      </div>
    </section>

    <section class="stories-section">
      <div class="section-header">
        <h2 class="section-title">MIS HISTORIAS</h2>
        <span class="story-count">{{ userStories.length }} historia(s)</span>
      </div>
      <div v-if="userStories.length > 0" class="user-stories-list">
        <div v-for="story in userStories" :key="story.id" class="user-story-card">
          <div class="story-card-top-bar"><div class="top-bar-inner"></div></div>
          <div class="story-card-body">
            <div class="story-card-image-box"><span>Imagen</span></div>
            <div class="story-card-content">
              <h3 class="story-card-title">{{ story.title }}</h3>
              <div class="story-card-meta">Oficio: {{ getProfLabel(story.profession) }} &nbsp;|&nbsp; Edad: {{ getAgeLabel(story.ageRange) }}</div>
              <p class="story-card-excerpt">{{ story.description?.substring(0, 100) }}{{ story.description?.length > 100 ? '...' : '' }}</p>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="empty-state">
        <div class="empty-icon-box"><span class="empty-icon">☐</span></div>
        <p class="empty-text">Aún no has subido ninguna historia.</p>
        <p class="empty-subtext">Comparte tu primera crónica con la comunidad.</p>
        <button class="custom-button" @click="$router.push('/create-story')">+ Crear Historia</button>
      </div>
    </section>
  </DashboardTemplate>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { useAuthStore } from '../composables/useAuthStore'
import { useStoryStore } from '../composables/useStoryStore'
import DashboardTemplate from '../components/templates/DashboardTemplate.vue'

const { user, updateUser } = useAuthStore()
const { stories } = useStoryStore()
const isEditing = ref(false)
const editData = reactive({ username: '', email: '', password: '' })

const userStories = computed(() => stories.filter(s => s.author === user.value.username))

const toggleEditMode = () => {
  if (!isEditing.value) {
    editData.username = user.value.username
    editData.email = user.value.email
    editData.password = ''
  }
  isEditing.value = !isEditing.value
}

const saveChanges = () => {
  const updates = {}
  if (editData.username) updates.username = editData.username
  if (editData.email) updates.email = editData.email
  if (editData.password) updates.password = editData.password
  updateUser(updates)
  isEditing.value = false
  alert('Datos actualizados con éxito')
}

const getProfLabel = (k) => ({ casa:'Casa', campo:'Campo', industria:'Industria', limpieza:'Limpieza', otro:'Otro' }[k] || 'N/A')
const getAgeLabel = (k) => ({ under_18:'<18', '18_25':'18-25', '26_35':'26-35', '36_45':'36-45', '46_60':'46-60', over_60:'>60' }[k] || 'N/A')
</script>

<style scoped>
.custom-button {
  background: var(--color-red);
  color: var(--color-white);
  border: none;
  border-radius: var(--wf-radius);
  padding: 8px 16px;
  cursor: pointer;
  font-weight: bold;
}
.profile-section, .stories-section { padding: var(--wf-spacing-lg); border:1px solid var(--color-red); border-radius:var(--wf-radius); margin-bottom:20px; background-color: var(--color-white); }
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
.story-card-image-box { width:120px; height:120px; background:var(--wf-button-bg); display:flex; justify-content:center; align-items:center; font-weight:bold; border:1px solid var(--color-primary); flex-shrink:0; text-transform:uppercase; letter-spacing:1px; font-size:0.8rem; }
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
