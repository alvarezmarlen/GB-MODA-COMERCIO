<template>
  <form @submit.prevent="onFormSubmit" class="create-story-form">
    <FormGroup label="Título de la historia">
      <BaseInput
        v-model="formData.title"
        placeholder="Escribe el título aquí..."
      />
    </FormGroup>

    <FormGroup label="Continente">
      <BaseSelect
        v-model="formData.countryOrigin"
        :options="countryOptions"
        placeholder="▼ Seleccionar continente"
      />
    </FormGroup>

    <FormGroup label="Profesión u oficio">
      <BaseSelect
        v-model="formData.profession"
        :options="professionOptions"
        placeholder="▼ Seleccionar profesión u oficio"
      />
    </FormGroup>

    <FormGroup label="Año de nacimiento">
      <BaseSelect
        v-model="formData.birthYearRange"
        :options="DateOfBirthOptions"
        placeholder="▼ Seleccionar año de nacimiento"
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

const countryOptions = [
  { label: 'America', value: 'america' },
  { label: 'Europa', value: 'europa' },
  { label: 'Africa', value: 'africa' },
  { label: 'Asia', value: 'asia' },
  { label: 'Oceania', value: 'oceania' },
]

const professionOptions = [
  { label: 'Hosteleria y turismo', value: 'hosteleria_turismo' },
  { label: 'Adminstracion y oficina', value: 'administracion_oficina' },
  { label: 'Ventas y comercio', value: 'ventas_comercio' },
  { label: 'Limpieza y mantenimiento', value: 'limpieza_mantenimiento' },
  { label: 'Educacion y formacion', value: 'educacion_formacion' },
  { label: 'Sanidad y cuidados', value: 'sanidad_cuidados' },
  { label: 'Belleza y estetica', value: 'belleza_estetica' },
  { label: 'Moda y confeccion', value: 'moda_confeccion' },
  { label: 'Cocina y alimentacion', value: 'cocina_alimentacion' },
  { label: 'Entre Otros', value: 'otros' }
]

const DateOfBirthOptions = [
  { label: '1930-1960', value: '1930-1960' },
  { label: '1960-1970', value: '1960-1970' },
  { label: '1970-1980', value: '1970-1980' },
  { label: '1990-2000', value: '1990-2000' },
  { label: '2000-2010', value: '2000-2010' },
]

const { formData, handleSubmit } = useForm({
  title: '',
  profession: '',
  birthYearRange: '',
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

.create-story-form :deep(.wireframe-button) {
  width: auto;
  min-width: 200px;
}
</style>
