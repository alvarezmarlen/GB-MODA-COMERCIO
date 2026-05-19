<template>
  <form @submit.prevent="onFormSubmit" class="create-story-form">
    <FormGroup label="Título de la historia">
      <BaseInput
        v-model="formData.title"
        placeholder="Escribe el título aquí..."
      />
    </FormGroup>

    <FormGroup label="Profesión">
      <BaseSelect
        v-model="formData.profession"
        :options="professionOptions"
        placeholder="▼ Seleccionar profesión"
      />
    </FormGroup>

    <FormGroup label="Edad">
      <BaseSelect
        v-model="formData.ageRange"
        :options="ageOptions"
        placeholder="▼ Seleccionar rango de edad"
      />
    </FormGroup>

    <FormGroup label="Descripción de la historia">
      <BaseTextarea
        v-model="formData.description"
        placeholder="Escribe aquí la historia o descripción completa..."
      />
    </FormGroup>

    <div class="checkbox-container">
      <BaseCheckbox v-model="formData.acceptedTerms" />
      <BaseLabel>Acepto los términos y permisos para publicar imágenes y contenido.</BaseLabel>
    </div>

    <FormGroup label="Subir fotografía">
      <BaseFileUpload :disabled="!formData.acceptedTerms" :max-files="2" @update:files="handleFilesUpdate" />
    </FormGroup>

    <div class="actions">
      <BaseButton type="submit" :disabled="!isFormValid">PUBLICAR</BaseButton>
    </div>
  </form>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import FormGroup from '../molecules/FormGroup.vue'
import BaseInput from '../atoms/BaseInput.vue'
import BaseSelect from '../atoms/BaseSelect.vue'
import BaseTextarea from '../atoms/BaseTextarea.vue'
import BaseCheckbox from '../atoms/BaseCheckbox.vue'
import BaseLabel from '../atoms/BaseLabel.vue'
import BaseFileUpload from '../atoms/BaseFileUpload.vue'
import BaseButton from '../atoms/BaseButton.vue'
import { useForm } from '../../composables/useForm'
import { useStoryStore } from '../../composables/useStoryStore'

const router = useRouter()
const { setStory } = useStoryStore()
const uploadedFiles = ref([])

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

const { formData, handleSubmit } = useForm({
  title: '',
  profession: '',
  ageRange: '',
  description: '',
  acceptedTerms: false
})

const handleFilesUpdate = (files) => {
  uploadedFiles.value = files
}

const isFormValid = computed(() => {
  return (
    formData.title.trim().length > 0 &&
    formData.profession !== '' &&
    formData.ageRange !== '' &&
    formData.description.trim().length > 0 &&
    formData.acceptedTerms
  )
})

const onFormSubmit = () => {
  handleSubmit((data) => {
    // Generate object URLs for local image display
    const imageUrls = uploadedFiles.value.map(file => URL.createObjectURL(file))
    
    setStory({
      title: data.title,
      profession: data.profession,
      ageRange: data.ageRange,
      description: data.description,
      images: imageUrls
    })

    console.log('Publishing story:', data)
    alert('Historia publicada con éxito')
    router.push('/story-detail')
  })
}
</script>

<style scoped>
.checkbox-container {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  margin-bottom: var(--wf-spacing-md);
}

.actions {
  display: flex;
  justify-content: center;
  margin-top: var(--wf-spacing-lg);
}

.create-story-form :deep(.wireframe-button) {
  width: auto;
  min-width: 200px;
}
</style>
