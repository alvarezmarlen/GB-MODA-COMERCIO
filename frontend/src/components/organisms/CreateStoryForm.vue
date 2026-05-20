<template>
  <form @submit.prevent="onFormSubmit" class="create-story-form">
    <FormGroup label="Título de la historia">
      <BaseInput
        v-model="formData.title"
        placeholder="Escribe el título aquí..."
      />
    </FormGroup>

    <FormGroup label="Profesión">
      <BaseInput
        v-model="formData.profession"
        placeholder="Escribe el oficio..."
      />
    </FormGroup>

    <FormGroup label="Edad">
      <BaseSelect
        v-model="formData.ageRange"
        :options="ageOptions"
        placeholder="▼ Seleccionar rango de edad"
      />
    </FormGroup>

    <FormGroup label="País de origen">
      <BaseInput
        v-model="formData.originCountry"
        placeholder="Escribe el país de origen..."
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

    <div v-if="submitError" class="error-message">{{ submitError }}</div>

    <div class="actions">
      <BaseButton type="submit" :disabled="!isFormValid || isSubmitting">
        {{ isSubmitting ? 'PUBLICANDO...' : 'PUBLICAR' }}
      </BaseButton>
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
import { useAuthStore } from '../../composables/useAuthStore'
import { createStory, uploadStoryImage } from '../../api/stories'

const router = useRouter()
const { setStory } = useStoryStore()
const { user } = useAuthStore()
const uploadedFiles = ref([])
const isSubmitting = ref(false)
const submitError = ref('')

const ageOptions = [
  { label: 'Menor de 18', value: 'under_18' },
  { label: '18 - 25 años', value: '18_25' },
  { label: '26 - 35 años', value: '26_35' },
  { label: '36 - 45 años', value: '36_45' },
  { label: '46 - 60 años', value: '46_60' },
  { label: 'Más de 60', value: 'over_60' }
]

const { formData } = useForm({
  title: '',
  profession: '',
  ageRange: '',
  originCountry: '',
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
    formData.originCountry !== '' &&
    formData.description.trim().length > 0 &&
    formData.acceptedTerms
  )
})

const onFormSubmit = async () => {
  isSubmitting.value = true
  submitError.value = ''

  try {
    const data = { ...formData }
    const storyData = {
      user_id: user.value?.id || 1,
      title: data.title,
      content: data.description,
      origin_country: data.originCountry,
      profession: data.profession,
      age_range: data.ageRange
    }

    const created = await createStory(storyData)

    const imageUrls = []
    if (uploadedFiles.value.length > 0) {
      for (const file of uploadedFiles.value) {
        const img = await uploadStoryImage(created.id, file)
        imageUrls.push(img.url)
      }
    }

    setStory({
      id: created.id,
      title: created.title,
      profession: created.profession,
      ageRange: created.age_range,
      description: created.content,
      images: imageUrls.length > 0 ? imageUrls : []
    })

    router.push({ name: 'story-detail', params: { id: created.id } })
  } catch (err) {
    submitError.value = err.message
  } finally {
    isSubmitting.value = false
  }
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

.error-message {
  color: #d32f2f;
  background: #fce4ec;
  padding: var(--wf-spacing-sm);
  border: 1px solid #d32f2f;
  text-align: center;
  font-weight: bold;
  margin-bottom: var(--wf-spacing-md);
}

.create-story-form :deep(.wireframe-button) {
  width: auto;
  min-width: 200px;
}
</style>
