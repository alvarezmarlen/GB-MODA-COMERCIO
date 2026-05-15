<template>
  <div class="file-upload" @click="triggerInput">
    <input
      type="file"
      ref="fileInput"
      class="hidden"
      @change="handleFileChange"
      accept="image/*"
    />
    <div class="upload-content">
      <span class="upload-icon">＋</span>
      <p v-if="!fileName">Arrastra una foto aquí o haz click</p>
      <p v-else>{{ fileName }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const fileInput = ref(null)
const fileName = ref('')

const triggerInput = () => {
  fileInput.value.click()
}

const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    fileName.value = file.name
  }
}
</script>

<style scoped>
.file-upload {
  border: 1px dashed var(--wf-border);
  padding: var(--wf-spacing-lg);
  text-align: center;
  cursor: pointer;
  background: var(--wf-bg);
  transition: background 0.2s;
}

.file-upload:hover {
  background: var(--wf-button-bg);
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
}
</style>
