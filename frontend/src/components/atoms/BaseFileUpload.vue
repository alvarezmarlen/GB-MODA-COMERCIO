<template>
  <div class="file-upload" :class="{ 'is-disabled': disabled }" @click="triggerInput">
    <input
      type="file"
      ref="fileInput"
      class="hidden"
      @change="handleFileChange"
      accept="image/*"
      :disabled="disabled"
      multiple
    />
    <div class="upload-content">
      <span class="upload-icon">＋</span>
      <p v-if="files.length === 0">{{ t('fileUpload.dragDrop') }}</p>
      <div v-else class="file-names">
        <p v-for="(file, index) in files" :key="index">{{ file.name }}</p>
      </div>
      <p v-if="files.length > 0" class="file-count">{{ t('fileUpload.selectedCount', { count: files.length, max: maxFiles }) }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

const props = defineProps({
  disabled: {
    type: Boolean,
    default: false
  },
  maxFiles: {
    type: Number,
    default: 2
  }
})

const emit = defineEmits(['update:files'])

const fileInput = ref(null)
const files = ref([])

const triggerInput = () => {
  if (!props.disabled) {
    fileInput.value.click()
  }
}

const handleFileChange = (event) => {
  if (props.disabled) return

  const selectedFiles = Array.from(event.target.files)
  
  if (selectedFiles.length > props.maxFiles) {
    alert(t('fileUpload.maxFilesAlert', { max: props.maxFiles }))
    files.value = selectedFiles.slice(0, props.maxFiles)
  } else {
    files.value = selectedFiles
  }
  emit('update:files', files.value)
}
</script>

<style scoped>
.file-upload {
  border: 1px dashed var(--color-red);
  border-radius: var(--wf-radius);
  padding: var(--wf-spacing-lg);
  text-align: center;
  cursor: pointer;
  background: var(--wf-bg);
  transition: background 0.2s, opacity 0.2s;
}

.file-upload:hover:not(.is-disabled) {
  background: var(--wf-button-bg);
}

.file-upload.is-disabled {
  cursor: not-allowed;
  opacity: 0.5;
  background: #f5f5f5;
}

.hidden {
  display: none;
}

.upload-icon {
  font-size: 2rem;
  display: block;
  margin-bottom: var(--wf-spacing-sm);
}

.upload-content p {
  font-size: 0.9rem;
  margin: 2px 0;
}

.file-names {
  margin-bottom: 8px;
}

.file-count {
  font-size: 0.8rem;
  color: #666;
  margin-top: 4px;
}
</style>
