<template>
  <DashboardTemplate :title="t('admin.title')">
    <!-- Stats bar -->
    <div class="stats-bar">
      <div class="stat-item">
        <span class="stat-number">{{ stories.length }}</span>
        <span class="stat-label">{{ t('admin.totalStories') }}</span>
      </div>
      <div class="stat-divider"></div>
      <div class="stat-item">
        <span class="stat-number">{{ uniqueAuthors }}</span>
        <span class="stat-label">{{ t('admin.authors') }}</span>
      </div>
    </div>

    <!-- All Stories Management -->
    <section class="admin-stories-section">
      <div class="section-header">
        <h2 class="section-title">{{ t('admin.management') }}</h2>
      </div>

      <div v-if="stories.length > 0" class="admin-stories-list">
        <div v-for="story in stories" :key="story.id" class="admin-story-card">
          <div class="admin-card-top-bar">
            <span class="admin-card-id">#{{ story.id }}</span>
          </div>
          <div class="admin-card-body">
            <div v-if="story.images && story.images.length > 0" class="admin-card-image-box">
              <img :src="story.images[0].url" :alt="story.title" class="admin-card-image" />
            </div>
            <div v-else class="admin-card-image-box"><span>{{ t('admin.noImage') }}</span></div>
            <div class="admin-card-content">
              <h3 class="admin-card-title">{{ story.title }}</h3>
              <div class="admin-card-meta">
                {{ t('admin.trade') }}: {{ story.profession }} &nbsp;|&nbsp;
                {{ t('admin.age') }}: {{ story.age_range }} &nbsp;|&nbsp;
                {{ t('admin.country') }}: {{ story.origin_country }}
              </div>
              <p class="admin-card-desc">{{ story.content?.substring(0, 120) }}{{ story.content?.length > 120 ? '...' : '' }}</p>
            </div>
          </div>
          <div class="admin-card-actions">
            <button class="custom-button edit-btn" @click="startEdit(story)">{{ t('admin.modify') }}</button>
            <button class="custom-button delete-btn" @click="confirmDelete(story)">{{ t('admin.delete') }}</button>
          </div>
        </div>
      </div>

      <div v-else class="empty-state">
        <p class="empty-text">{{ t('admin.noStories') }}</p>
      </div>
    </section>

    <!-- Edit Modal -->
    <div v-if="editingStory" class="modal-overlay" @click.self="cancelEdit">
      <div class="modal-content">
        <div class="section-header">
          <h2 class="section-title">{{ t('admin.editTitle') }}</h2>
          <button class="custom-button" @click="cancelEdit">✕</button>
        </div>
        <div class="modal-fields">
          <div class="modal-field">
            <label class="custom-label">{{ t('admin.titleLabel') }}</label>
            <input v-model="editForm.title" class="wireframe-input" type="text" />
          </div>
          <div class="modal-field">
            <label class="custom-label">{{ t('admin.descriptionLabel') }}</label>
            <textarea v-model="editForm.content" class="wireframe-input modal-textarea" rows="4"></textarea>
          </div>
        </div>
        <div class="modal-actions">
          <button class="custom-button" @click="cancelEdit">{{ t('admin.cancel') }}</button>
          <button class="custom-button save-btn" @click="saveEdit">{{ t('admin.save') }}</button>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation -->
    <div v-if="deletingStory" class="modal-overlay" @click.self="cancelDelete">
      <div class="modal-content modal-small">
        <h2 class="section-title" style="margin-bottom: var(--wf-spacing-md);">{{ t('admin.confirmDelete') }}</h2>
        <p>{{ t('admin.confirmDeleteMsg', { title: deletingStory.title }) }}</p>
        <div class="modal-actions">
          <button class="custom-button" @click="cancelDelete">{{ t('admin.cancel') }}</button>
          <button class="custom-button delete-btn" @click="executeDelete">{{ t('admin.delete') }}</button>
        </div>
      </div>
    </div>
  </DashboardTemplate>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { getStories, updateStory, deleteStory } from '../api/stories'
import DashboardTemplate from '../components/templates/DashboardTemplate.vue'

const { t } = useI18n()

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
  } catch {
  }
}

const confirmDelete = (story) => { deletingStory.value = story }
const cancelDelete = () => { deletingStory.value = null }

const executeDelete = async () => {
  try {
    await deleteStory(deletingStory.value.id)
    stories.value = stories.value.filter(s => s.id !== deletingStory.value.id)
    deletingStory.value = null
  } catch {
  }
}

const getProfLabel = (k) => k ? t(`professions.${k}`) : 'N/A'
const getAgeLabel = (k) => k ? t(`ages.${k}`) : 'N/A'
</script>

<style scoped>
.custom-button { background:var(--color-red); color:var(--color-white); border:none; border-radius:var(--wf-radius); padding:8px 16px; cursor:pointer; font-weight:bold; }
.custom-label { display:block; font-size:0.85rem; font-weight:bold; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px; }
.stats-bar { display:flex; align-items:center; justify-content:center; gap:var(--wf-spacing-lg); padding:var(--wf-spacing-md) var(--wf-spacing-lg); border:1px solid var(--color-red); border-radius:var(--wf-radius); margin-bottom:20px; background-color:var(--color-white); }
.stat-item { display:flex; flex-direction:column; align-items:center; gap:4px; }
.stat-number { font-size:1.8rem; font-weight:bold; letter-spacing:2px; }
.stat-label { font-size:0.8rem; text-transform:uppercase; letter-spacing:1px; }
.stat-divider { width:2px; height:40px; background:var(--color-red); }
.admin-stories-section { padding:var(--wf-spacing-lg); border:1px solid var(--color-red); border-radius:var(--wf-radius); background-color:var(--color-white); }
.section-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:var(--wf-spacing-lg); border-bottom:4px solid var(--color-red); padding-bottom:var(--wf-spacing-sm); }
.section-title { font-size:1.1rem; letter-spacing:2px; text-transform:uppercase; margin:0; color:var(--color-yellow); }
.admin-stories-list { display:flex; flex-direction:column; gap:var(--wf-spacing-md); }
.admin-story-card { border:1px solid var(--color-primary); background:#fff; display:flex; flex-direction:column; transition:all 0.3s ease; border-radius:var(--wf-radius); padding:10px; }
.admin-card-top-bar { padding:6px 16px; display:flex; justify-content:space-between; align-items:center; font-size:0.85rem; font-weight:bold; }
.admin-card-id { letter-spacing:1px; }
.admin-card-body { display:flex; gap:var(--wf-spacing-md); padding:var(--wf-spacing-md); }
.admin-card-image-box { width:120px; height:120px; background:var(--wf-button-bg); display:flex; justify-content:center; align-items:center; font-weight:bold; border:1px solid var(--color-primary); flex-shrink:0; text-transform:uppercase; letter-spacing:1px; font-size:0.8rem; overflow:hidden; }
.admin-card-image { width:100%; height:100%; object-fit:cover; }
.admin-card-content { flex:1; display:flex; flex-direction:column; gap:var(--wf-spacing-sm); }
.admin-card-title { font-size:1rem; text-transform:uppercase; letter-spacing:1px; margin:0; }
.admin-card-meta { font-size:0.85rem; font-weight:bold; }
.admin-card-desc { font-size:0.85rem; line-height:1.5; margin:0; }
.admin-card-actions { display:flex; justify-content:flex-end; gap:var(--wf-spacing-sm); padding:var(--wf-spacing-sm) var(--wf-spacing-md); border-top:1px solid var(--color-primary); }
.edit-btn { font-size:0.85rem; }
.delete-btn { font-size:0.85rem; }
.save-btn { background:var(--color-red); color:var(--color-white); }
.save-btn:hover { background:#333; }
.modal-overlay { position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.4); display:flex; justify-content:center; align-items:center; z-index:1000; }
.modal-content { width:90%; max-width:550px; padding:var(--wf-spacing-lg); background:var(--wf-bg); border-radius:var(--wf-radius); }
.modal-small { max-width:420px; }
.modal-fields { display:flex; flex-direction:column; gap:var(--wf-spacing-md); }
.modal-field { display:flex; flex-direction:column; gap:4px; margin-bottom:10px; }
.modal-textarea { resize:vertical; font-family:inherit; }
.modal-actions { display:flex; justify-content:flex-end; gap:var(--wf-spacing-sm); margin-top:var(--wf-spacing-lg); padding-top:var(--wf-spacing-md); border-top:1px solid var(--color-primary); }
.empty-state { text-align:center; padding:var(--wf-spacing-lg) 0; }
.empty-text { font-weight:bold; }
@media (max-width:600px) {
  .stats-bar { flex-direction:column; }
  .stat-divider { width:40px; height:2px; }
  .admin-card-body { flex-direction:column; align-items:center; }
  .admin-card-image-box { width:100%; max-width:200px; }
  .admin-card-actions { flex-direction:column; }
}
</style>
