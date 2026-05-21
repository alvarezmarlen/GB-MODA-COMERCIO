<template>
  <form @submit.prevent="onFormSubmit" class="create-story-form">
    <FormGroup label="Título de la historia">
      <BaseInput
        v-model="formData.title"
        placeholder="Escribe el título aquí..."
      />
    </FormGroup>

    <FormGroup label="País de origen o continente">
      <BaseSelect
        v-model="formData.countryOrigin"
        :options="countryOptions"
        placeholder="▼ Seleccionar país o continente"
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
      <BaseFileUpload :disabled="!formData.acceptedTerms" :max-files="2" />
    </FormGroup>

    <div class="actions">
      <BaseButton type="submit" :disabled="!isFormValid">PUBLICAR</BaseButton>
    </div>
  </form>
</template>

<script setup>
import { computed } from 'vue'
import FormGroup from '../molecules/FormGroup.vue'
import BaseInput from '../atoms/BaseInput.vue'
import BaseSelect from '../atoms/BaseSelect.vue'
import BaseTextarea from '../atoms/BaseTextarea.vue'
import BaseCheckbox from '../atoms/BaseCheckbox.vue'
import BaseLabel from '../atoms/BaseLabel.vue'
import BaseFileUpload from '../atoms/BaseFileUpload.vue'
import BaseButton from '../atoms/BaseButton.vue'
import { useForm } from '../../composables/useForm'

const countryOptions = [
  { label: 'País Vasco', value: 'pais_vasco' },
  { label: 'Europa', value: 'europa' },
  { label: 'Marruecos', value: 'marruecos' },
  { label: 'África', value: 'africa' },
  { label: 'America Latina', value: 'america_latina' },
  { label: 'Otro', value: 'otro' }
]

const professionOptions = [
  { label: 'Ama de casa', value: 'ama de casa' },
  { label: 'Cuidadora', value: 'cuidadora' },
  { label: 'Camarera', value: 'camarera' },
  { label: 'Servicio de Limpieza', value: 'servicio de limpieza' },
  { label: 'Enfermera', value: 'enfermera' },
  { label: 'Otro', value: 'otro' }
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
  countryOrigin: '',
  profession: '',
  birthYearRange: '',
  description: '',
  acceptedTerms: false
})

const isFormValid = computed(() => {
  return (
    formData.title.trim().length > 0 &&
    formData.countryOrigin !== '' &&
    formData.profession !== '' &&
    formData.ageRange !== '' &&
    formData.description.trim().length > 0 &&
    formData.acceptedTerms
  )
})

const onFormSubmit = () => {
  handleSubmit((data) => {
    console.log('Publishing story:', data)
    alert('Historia publicada con éxito')
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
