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
        :options="DateOfBirthOptions"
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

const router = useRouter()
const { t } = useI18n()
const { user } = useAuthStore()
const { setStory } = useStoryStore()
const isSubmitting = ref(false)
const submitError = ref('')
const uploadedFiles = ref([])

const countryOptions = computed(() => [
  { label: t('createStory.countryOptions.pais_vasco'), value: 'pais_vasco' },
  { label: t('createStory.countryOptions.europa'), value: 'europa' },
  { label: t('createStory.countryOptions.marruecos'), value: 'marruecos' },
  { label: t('createStory.countryOptions.africa'), value: 'africa' },
  { label: t('createStory.countryOptions.america_latina'), value: 'america_latina' },
  { label: t('createStory.countryOptions.otro'), value: 'otro' }
])

const professionOptions = computed(() => [
  { label: t('createStory.professionOptions.ama_de_casa'), value: 'ama de casa' },
  { label: t('createStory.professionOptions.cuidadora'), value: 'cuidadora' },
  { label: t('createStory.professionOptions.camarera'), value: 'camarera' },
  { label: t('createStory.professionOptions.servicio_de_limpieza'), value: 'servicio de limpieza' },
  { label: t('createStory.professionOptions.enfermera'), value: 'enfermera' },
  { label: t('createStory.professionOptions.otro'), value: 'otro' }
])

const DateOfBirthOptions = computed(() => [
  { label: t('createStory.ageOptions.1930_1960'), value: '1930-1960' },
  { label: t('createStory.ageOptions.1960_1970'), value: '1960-1970' },
  { label: t('createStory.ageOptions.1970_1980'), value: '1970-1980' },
  { label: t('createStory.ageOptions.1990_2000'), value: '1990-2000' },
  { label: t('createStory.ageOptions.2000_2010'), value: '2000-2010' },
])

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
.create-story-form {
  border: none;
  border-radius: var(--wf-radius);
  padding: var(--wf-spacing-lg);
  margin: var(--wf-spacing-lg) auto;
  background: var(--wf-bg);
  max-width: 800px; /* Assuming the form should match the template's max-width */
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
