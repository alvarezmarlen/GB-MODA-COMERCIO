<template>
  <form @submit.prevent="onFormSubmit" class="create-story-form">
    <FormGroup :label="t('createStory.titleLabel')">
      <BaseInput
        v-model="formData.title"
        :placeholder="t('createStory.titlePlaceholder')"
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
        :options="ageOptions"
        :placeholder="t('createStory.agePlaceholder')"
      />
    </FormGroup>

    <FormGroup :label="t('createStory.countryLabel')">
      <BaseSelect
        v-model="formData.originCountry"
        :options="countryOptions"
        :placeholder="t('createStory.countryPlaceholder')"
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
const router = useRouter()
const { setStory } = useStoryStore()
const { user } = useAuthStore()
const uploadedFiles = ref([])
const isSubmitting = ref(false)
const submitError = ref('')

const professionOptions = [
  { label: t('professions.casa'), value: 'casa' },
  { label: t('professions.campo'), value: 'campo' },
  { label: t('professions.industria'), value: 'industria' },
  { label: t('professions.limpieza'), value: 'limpieza' },
  { label: t('professions.otro'), value: 'otro' }
]

const countryOptions = [
  { label: t('countries.Brasil'), value: 'Brasil' },
  { label: t('countries.Portugal'), value: 'Portugal' },
  { label: t('countries.España'), value: 'España' },
  { label: t('countries.Argentina'), value: 'Argentina' },
  { label: t('countries.México'), value: 'México' },
  { label: t('countries.Colombia'), value: 'Colombia' },
  { label: t('countries.Chile'), value: 'Chile' },
  { label: t('countries.Perú'), value: 'Perú' },
  { label: t('countries.Venezuela'), value: 'Venezuela' },
  { label: t('countries.Uruguay'), value: 'Uruguay' },
  { label: t('countries.Paraguay'), value: 'Paraguay' },
  { label: t('countries.Otro'), value: 'Otro' }
]

const ageOptions = [
  { label: t('ages.under_18'), value: 'under_18' },
  { label: t('ages.18_25'), value: '18_25' },
  { label: t('ages.26_35'), value: '26_35' },
  { label: t('ages.36_45'), value: '36_45' },
  { label: t('ages.46_60'), value: '46_60' },
  { label: t('ages.over_60'), value: 'over_60' }
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
