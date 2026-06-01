<template>
  <form @submit.prevent="onFormSubmit" class="create-story-form">
    <FormGroup :label="t('createStory.titleLabel')">
      <BaseInput
        v-model="formData.title"
        :placeholder="t('createStory.titlePlaceholder')"
      />
    </FormGroup>

    <FormGroup label="Continente">
      <BaseSelect
        v-model="formData.originCountry"
        :options="countryOptions"
        placeholder="▼ Seleccionar continente"
      />
    </FormGroup>

    <FormGroup :label="t('createStory.professionLabel')">
      <BaseSelect
        v-model="formData.profession"
        :options="professionOptions"
        :placeholder="t('createStory.professionPlaceholder')"
      />
    </FormGroup>

    <FormGroup :label="t('createStory.ageLabel')">
      <BaseSelect
        v-model="formData.ageRange"
        :options="ageRangeOptions"
        :placeholder="t('createStory.agePlaceholder')"
      />
    </FormGroup>

    <FormGroup :label="t('createStory.descriptionLabel')">
      <BaseTextarea
        v-model="formData.description"
        :placeholder="t('createStory.descriptionPlaceholder')"
      />
    </FormGroup>

    <div class="checkbox-container">
      <BaseCheckbox v-model="formData.acceptedTerms" />
      <BaseLabel>{{ t('createStory.termsLabel') }}</BaseLabel>
    </div>

    <FormGroup :label="t('createStory.uploadLabel')">
      <BaseFileUpload :disabled="!formData.acceptedTerms" :max-files="2" @update:files="handleFilesUpdate" />
    </FormGroup>

    <div v-if="submitError" class="error-message">{{ submitError }}</div>

    <div class="actions">
      <BaseButton type="submit" :disabled="!isFormValid || isSubmitting">
        {{ isSubmitting ? t('createStory.publishing') : t('createStory.publish') }}
      </BaseButton>
    </div>
  </form>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
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

const { t } = useI18n()

const countryOptions = [
  { label: 'Norteamérica', value: 'Norteamerica' },
  { label: 'Sudamérica', value: 'Suramerica' },
  { label: 'Centroamérica', value: 'Centroamerica' },
  { label: 'Europa', value: 'Europa' },
  { label: 'África', value: 'Africa' },
  { label: 'Asia', value: 'Asia' },
  { label: 'Oceanía', value: 'Oceania' },
  { label: 'Otras regiones', value: 'Otros 1' }
]

const professionOptions = [
  { label: 'Hosteleria y turismo', value: 'hosteleria_turismo' },
  { label: 'Administracion y oficina', value: 'administracion_oficina' },
  { label: 'Ventas y comercio', value: 'ventas_comercio' },
  { label: 'Limpieza y mantenimiento', value: 'limpieza_mantenimiento' },
  { label: 'Educacion y formacion', value: 'educacion_formacion' },
  { label: 'Sanidad y cuidados', value: 'sanidad_cuidados' },
  { label: 'Belleza y estetica', value: 'belleza_estetica' },
  { label: 'Moda y confeccion', value: 'moda_confeccion' },
  { label: 'Cocina y alimentacion', value: 'cocina_alimentacion' },
  { label: 'Entre Otros', value: 'otros' }
]

const ageRangeOptions = [
  { label: '1930-1960', value: '1930-1960' },
  { label: '1960-1970', value: '1960-1970' },
  { label: '1970-1980', value: '1970-1980' },
  { label: '1990-2000', value: '1990-2000' },
  { label: '2000-2010', value: '2000-2010' }
]


const professionMap = {
  hosteleria_turismo: 'Hostelería y Turismo',
  administracion_oficina: 'Administración y Oficina',
  ventas_comercio: 'Ventas y Comercio',
  limpieza_mantenimiento: 'Limpieza y Mantenimiento',
  educacion_formacion: 'Educación y Formación',
  sanidad_cuidados: 'Sanidad y Cuidados',
  belleza_estetica: 'Belleza y Estética',
  moda_confeccion: 'Moda y Confección',
  cocina_alimentacion: 'Cocina y Alimentación',
  otros: 'Otros'
}

const yearRangeToAgeRange = {
  '1930-1960': '60+',
  '1960-1970': '50-60',
  '1970-1980': '40-50',
  '1990-2000': '25-35',
  '2000-2010': '18-25'
}

const router = useRouter()
const authStore = useAuthStore()
const { setStory } = useStoryStore()
const uploadedFiles = ref([])
const isSubmitting = ref(false)
const submitError = ref('')
const { formData, handleSubmit } = useForm({
  title: '',
  originCountry: '',
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
    formData.originCountry !== '' &&
    formData.description.trim().length > 0 &&
    formData.acceptedTerms
  )
})

const onFormSubmit = async () => {
  if (!isFormValid.value) {
    submitError.value = 'Por favor, completa todos los campos requeridos'
    return
  }

  isSubmitting.value = true
  submitError.value = ''

  try {
    // Obtener user ID de forma segura
    let userId = 1
    if (authStore.user && authStore.user.value) {
      userId = authStore.user.value.id || 1
    } else if (authStore.user && authStore.user.id) {
      userId = authStore.user.id || 1
    }

    const storyData = {
      user_id: userId,
      title: formData.title,
      content: formData.description,
      origin_country: formData.originCountry,
      profession: professionMap[formData.profession] || formData.profession,
      age_range: yearRangeToAgeRange[formData.ageRange] || formData.ageRange
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
      originCountry: formData.originCountry,
      ageRange: created.age_range,
      description: created.content,
      images: imageUrls.length > 0 ? imageUrls : []
    })

    router.push({ name: 'story-detail', params: { id: created.id } })
  } catch (err) {
    submitError.value = err.message || 'Error al publicar la historia'
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
.create-story-form {
  border: none;
  border-radius: var(--wf-radius);
  padding: var(--wf-spacing-lg);
  margin: var(--wf-spacing-lg) auto;
  background: var(--wf-bg);
  max-width: 800px;
}

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
