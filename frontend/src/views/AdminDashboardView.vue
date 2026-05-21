<template>
  <DashboardTemplate title="Panel Admin">
    <!-- Stats bar -->
    <div class="stats-bar wireframe-container">
      <div class="stat-item">
        <span class="stat-number">{{ stories.length }}</span>
        <span class="stat-label">Total Historias</span>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <span class="stat-number">{{ uniqueAuthors }}</span>
        <span class="stat-label">Autores</span>
      </div>
    </div>

    <!-- All Stories Management -->
    <section class="wireframe-container admin-stories-section">
      <div class="section-header">
        <h2 class="section-title">GESTIÓN DE HISTORIAS</h2>
      </div>

      <div v-if="stories.length > 0" class="admin-stories-list">
        <div v-for="story in stories" :key="story.id" class="admin-story-card">
          <div class="admin-card-top-bar">
            <span class="admin-card-id">#{{ story.id }}</span>
          </div>
          <div class="admin-card-body">
            <div class="admin-card-image-box"><span>Imagen</span></div>
            <div class="admin-card-content">
              <h3 class="admin-card-title">{{ story.title }}</h3>
              <div class="admin-card-meta">
                Oficio: {{ getProfLabel(story.profession) }} &nbsp;|&nbsp;
                Edad: {{ getAgeLabel(story.age_range) }} &nbsp;|&nbsp;
                País: {{ story.origin_country }}
              </div>
              <p class="admin-card-desc">{{ story.content?.substring(0, 120) }}{{ story.content?.length > 120 ? '...' : '' }}</p>
            </div>
          </div>
          <div class="admin-card-actions">
            <button class="wireframe-button edit-btn" @click="startEdit(story)">✎ Modificar</button>
            <button class="wireframe-button delete-btn" @click="confirmDelete(story)">✕ Borrar</button>
          </div>
        </div>
      </div>

      <div v-else class="empty-state">
        <p class="empty-text">No hay historias registradas.</p>
      </div>
    </section>

    <!-- Edit Modal -->
    <div v-if="editingStory" class="modal-overlay" @click.self="cancelEdit">
      <div class="wireframe-container modal-content">
        <div class="section-header">
          <h2 class="section-title">MODIFICAR HISTORIA</h2>
          <button class="wireframe-button" @click="cancelEdit">✕</button>
        </div>
        <div class="modal-fields">
          <div class="modal-field">
            <label class="wireframe-label">Título</label>
            <input v-model="editForm.title" class="wireframe-input" type="text" />
          </div>
          <div class="modal-field">
            <label class="wireframe-label">Descripción</label>
            <textarea v-model="editForm.content" class="wireframe-input modal-textarea" rows="4"></textarea>
          </div>
        </div>
        <div class="modal-actions">
          <button class="wireframe-button" @click="cancelEdit">Cancelar</button>
          <button class="wireframe-button save-btn" @click="saveEdit">✓ Guardar</button>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation -->
    <div v-if="deletingStory" class="modal-overlay" @click.self="cancelDelete">
      <div class="wireframe-container modal-content modal-small">
        <h2 class="section-title" style="margin-bottom: var(--wf-spacing-md);">CONFIRMAR ELIMINACIÓN</h2>
        <p>¿Estás seguro de que deseas borrar la historia <strong>"{{ deletingStory.title }}"</strong>?</p>
        <div class="modal-actions">
          <button class="wireframe-button" @click="cancelDelete">Cancelar</button>
          <button class="wireframe-button delete-btn" @click="executeDelete">✕ Borrar</button>
        </div>
      </div>
    </div>
  </DashboardTemplate>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { getStories, updateStory, deleteStory } from '../api/stories'
import DashboardTemplate from '../components/templates/DashboardTemplate.vue'

const stories = ref([])
const loading = ref(true)

const editingStory = ref(null)
const deletingStory = ref(null)
const editForm = reactive({ title: '', content: '' })

const uniqueAuthors = computed(() => new Set(stories.value.map(s => s.user_id)).size)

onMounted(async () => {
  try {
    stories.value = await getStories()
  } catch {
    stories.value = []
  } finally {
    loading.value = false
  }
})

const startEdit = (story) => {
  editingStory.value = story
  editForm.title = story.title
  editForm.content = story.content
}

const cancelEdit = () => { editingStory.value = null }

const saveEdit = async () => {
  try {
    const updated = await updateStory(editingStory.value.id, {
      title: editForm.title,
      content: editForm.content,
    })
    const idx = stories.value.findIndex(s => s.id === editingStory.value.id)
    if (idx !== -1) stories.value[idx] = updated
    editingStory.value = null
    alert('Historia actualizada con éxito')
  } catch {
    alert('Error al actualizar la historia')
  }
}

const confirmDelete = (story) => { deletingStory.value = story }
const cancelDelete = () => { deletingStory.value = null }

const executeDelete = async () => {
  try {
    await deleteStory(deletingStory.value.id)
    stories.value = stories.value.filter(s => s.id !== deletingStory.value.id)
    deletingStory.value = null
    alert('Historia eliminada con éxito')
  } catch {
    alert('Error al eliminar la historia')
  }
}

const getProfLabel = (k) => ({ casa:'Casa', campo:'Campo', industria:'Industria', limpieza:'Limpieza', otro:'Otro' }[k] || 'N/A')
const getAgeLabel = (k) => ({ under_18:'<18', '18_25':'18-25', '26_35':'26-35', '36_45':'36-45', '46_60':'46-60', over_60:'>60' }[k] || 'N/A')
</script>

<style scoped>
.stats-bar { display:flex; align-items:center; justify-content:center; gap:var(--wf-spacing-lg); padding:var(--wf-spacing-md) var(--wf-spacing-lg) !important; }
.stat-item { display:flex; flex-direction:column; align-items:center; gap:4px; }
.stat-number { font-size:1.8rem; font-weight:bold; letter-spacing:2px; }
.stat-label { font-size:0.8rem; text-transform:uppercase; letter-spacing:1px; }
.stat-divider { width:2px; height:40px; background:var(--wf-border); }
.admin-stories-section { padding:var(--wf-spacing-lg) !important; }
.section-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:var(--wf-spacing-lg); border-bottom:2px solid var(--wf-border); padding-bottom:var(--wf-spacing-sm); }
.section-title { font-size:1.1rem; letter-spacing:2px; text-transform:uppercase; margin:0; }
.admin-stories-list { display:flex; flex-direction:column; gap:var(--wf-spacing-md); }
.admin-story-card { border:2px solid var(--wf-border); background:var(--wf-bg); display:flex; flex-direction:column; transition:all 0.3s ease; }
.admin-story-card:hover { box-shadow:4px 4px 0px var(--wf-border); transform:translate(-2px,-2px); }
.admin-card-top-bar { background:var(--wf-button-bg); border-bottom:2px solid var(--wf-border); padding:6px 16px; display:flex; justify-content:space-between; align-items:center; font-size:0.85rem; font-weight:bold; }
.admin-card-id { letter-spacing:1px; }
.admin-card-author { font-weight:normal; font-style:italic; }
.admin-card-body { display:flex; gap:var(--wf-spacing-md); padding:var(--wf-spacing-md); }
.admin-card-image-box { width:120px; height:120px; background:var(--wf-button-bg); display:flex; justify-content:center; align-items:center; font-weight:bold; border:2px solid var(--wf-border); flex-shrink:0; text-transform:uppercase; letter-spacing:1px; font-size:0.8rem; }
.admin-card-content { flex:1; display:flex; flex-direction:column; gap:var(--wf-spacing-sm); }
.admin-card-title { font-size:1rem; text-transform:uppercase; letter-spacing:1px; margin:0; }
.admin-card-meta { font-size:0.85rem; font-weight:bold; }
.admin-card-desc { font-size:0.85rem; line-height:1.5; margin:0; }
.admin-card-actions { display:flex; justify-content:flex-end; gap:var(--wf-spacing-sm); padding:var(--wf-spacing-sm) var(--wf-spacing-md); border-top:1px dashed var(--wf-placeholder); }
.edit-btn { font-size:0.85rem; }
.delete-btn { font-size:0.85rem; background:#fff; border-color:var(--wf-border); }
.delete-btn:hover { background:var(--wf-border); color:var(--wf-bg); }
.save-btn { background:var(--wf-border); color:var(--wf-bg); }
.save-btn:hover { background:#333; }
/* Modal */
.modal-overlay { position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.4); display:flex; justify-content:center; align-items:center; z-index:1000; animation:fadeIn 0.2s ease; }
.modal-content { width:90%; max-width:550px; padding:var(--wf-spacing-lg) !important; background:var(--wf-bg); }
.modal-small { max-width:420px; }
.modal-fields { display:flex; flex-direction:column; gap:var(--wf-spacing-md); }
.modal-field { display:flex; flex-direction:column; gap:4px; }
.modal-textarea { resize:vertical; font-family:inherit; }
.modal-actions { display:flex; justify-content:flex-end; gap:var(--wf-spacing-sm); margin-top:var(--wf-spacing-lg); padding-top:var(--wf-spacing-md); border-top:1px solid var(--wf-placeholder); }
.empty-state { text-align:center; padding:var(--wf-spacing-lg) 0; }
.empty-text { font-weight:bold; }
@keyframes fadeIn { from{opacity:0} to{opacity:1} }
@media (max-width:600px) {
  .stats-bar { flex-direction:column; }
  .stat-divider { width:40px; height:2px; }
  .admin-card-body { flex-direction:column; align-items:center; }
  .admin-card-image-box { width:100%; max-width:200px; }
  .admin-card-actions { flex-direction:column; }
}
</style>
