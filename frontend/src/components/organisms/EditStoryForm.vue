<template>
  <form @submit.prevent="onFormSubmit" class="create-story-form">
    <FormGroup :label="t('editStory.titleLabel')">
      <BaseInput
        v-model="formData.title"
        :placeholder="t('editStory.titlePlaceholder')"
      />
    </FormGroup>

    <FormGroup :label="t('editStory.continentLabel')">
      <BaseSelect
        v-model="formData.originCountry"
        :options="countryOptions"
        :placeholder="t('editStory.continentPlaceholder')"
      />
    </FormGroup>

    <FormGroup :label="t('editStory.professionLabel')">
      <BaseSelect
        v-model="formData.profession"
        :options="professionOptions"
        :placeholder="t('editStory.professionPlaceholder')"
      />
    </FormGroup>

    <FormGroup :label="t('editStory.ageLabel')">
      <BaseSelect
        v-model="formData.ageRange"
        :options="ageRangeOptions"
        :placeholder="t('editStory.agePlaceholder')"
      />
    </FormGroup>

    <FormGroup :label="t('editStory.descriptionLabel')">
      <BaseTextarea
        v-model="formData.description"
        :placeholder="t('editStory.descriptionPlaceholder')"
      />
    </FormGroup>

    <div class="checkbox-container">
      <BaseCheckbox v-model="formData.acceptedTerms" />
      <BaseLabel>{{ t('editStory.termsLabel') }}</BaseLabel>
    </div>

    <FormGroup :label="t('editStory.uploadLabel')">
      <BaseFileUpload :disabled="!formData.acceptedTerms" :max-files="2" @update:files="handleFilesUpdate" />
    </FormGroup>

    <div v-if="submitError" class="error-message">{{ submitError }}</div>

    <div class="actions">
      <BaseButton type="submit" :disabled="!isFormValid || isSubmitting">
        {{ isSubmitting ? t('editStory.publishing') : t('editStory.publish') }}
      </BaseButton>
    </div>
  </form>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
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
import { getStoryById, updateStory, uploadStoryImage } from '../../api/stories'

const { t } = useI18n()

const props = defineProps({
  storyId: {
    type: Number,
    required: true
  }
})

const countryOptions = computed(() => [
  { label: t('continents.Norteamerica'), value: 'Norteamerica' },
  { label: t('continents.Suramerica'), value: 'Suramerica' },
  { label: t('continents.Centroamerica'), value: 'Centroamerica' },
  { label: t('continents.Europa'), value: 'Europa' },
  { label: t('continents.Africa'), value: 'Africa' },
  { label: t('continents.Asia'), value: 'Asia' },
  { label: t('continents.Oceania'), value: 'Oceania' },
  { label: t('continents.Otros 1'), value: 'Otros 1' }
])

const professionOptions = computed(() => [
  { label: t('professionOptions.Hostelería y Turismo'), value: 'hosteleria_turismo' },
  { label: t('professionOptions.Administración y Oficina'), value: 'administracion_oficina' },
  { label: t('professionOptions.Ventas y Comercio'), value: 'ventas_comercio' },
  { label: t('professionOptions.Limpieza y Mantenimiento'), value: 'limpieza_mantenimiento' },
  { label: t('professionOptions.Educación y Formación'), value: 'educacion_formacion' },
  { label: t('professionOptions.Sanidad y Cuidados'), value: 'sanidad_cuidados' },
  { label: t('professionOptions.Belleza y Estética'), value: 'belleza_estetica' },
  { label: t('professionOptions.Moda y Confección'), value: 'moda_confeccion' },
  { label: t('professionOptions.Cocina y Alimentación'), value: 'cocina_alimentacion' },
  { label: t('professionOptions.Otros'), value: 'otros' }
])

const ageRangeOptions = computed(() => [
  { label: '1930-1960', value: '1930-1960' },
  { label: '1960-1970', value: '1960-1970' },
  { label: '1970-1980', value: '1970-1980' },
  { label: '1990-2000', value: '1990-2000' },
  { label: '2000-2010', value: '2000-2010' }
])

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

onMounted(async () => {
  try {
    const story = await getStoryById(props.storyId)
    formData.title = story.title
    formData.description = story.content
    formData.acceptedTerms = true
    
    const reverseProf = Object.keys(professionMap).find(k => professionMap[k] === story.profession) || story.profession
    const reverseAge = Object.keys(yearRangeToAgeRange).find(k => yearRangeToAgeRange[k] === story.age_range) || story.age_range

    formData.originCountry = story.origin_country
    formData.profession = reverseProf
    formData.ageRange = reverseAge
  } catch (err) {
    submitError.value = t('editStory.loadError')
  }
})

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
    submitError.value = t('editStory.submitErrorRequired')
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

    const updated = await updateStory(props.storyId, storyData)

    const imageUrls = []
    if (uploadedFiles.value.length > 0) {
      for (const file of uploadedFiles.value) {
        const img = await uploadStoryImage(props.storyId, file)
        imageUrls.push(img.url)
      }
    }

    setStory({
      id: props.storyId,
      title: updated.title || formData.title,
      profession: updated.profession || professionMap[formData.profession],
      ageRange: updated.age_range || yearRangeToAgeRange[formData.ageRange],
      description: updated.content || formData.description,
      images: imageUrls.length > 0 ? imageUrls : []
    })

    router.push({ name: 'story-detail', params: { id: props.storyId } })
  } catch (err) {
    submitError.value = err.message || t('editStory.updateError')
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
