<template>
  <form @submit.prevent="onFormSubmit" class="register-form">
    <FormField
      label="Nombre de usuario"
      v-model="formData.username"
      placeholder="Mínimo 3 caracteres"
    />
    
    <FormField
      label="Email"
      type="email"
      v-model="formData.email"
      placeholder="ejemplo@correo.com"
    />
    
    <FormField
      label="Contraseña"
      type="password"
      v-model="formData.password"
      placeholder="Mínimo 6 caracteres"
    />

    <div class="checkbox-container">
      <BaseCheckbox v-model="formData.terms" />
      <BaseLabel>Acepto los términos y condiciones</BaseLabel>
    </div>

    <!-- The button remains disabled until all data is "clean" -->
    <BaseButton type="submit" :disabled="!isFormValid">Registrarse</BaseButton>
  </form>
</template>

<script setup>
import { useRouter } from 'vue-router'
import FormField from '../molecules/FormField.vue'
import BaseButton from '../atoms/BaseButton.vue'
import BaseCheckbox from '../atoms/BaseCheckbox.vue'
import BaseLabel from '../atoms/BaseLabel.vue'
import { useForm } from '../../composables/useForm'

const router = useRouter()
const { formData, handleSubmit, isValidEmail } = useForm({
  username: '',
  email: '',
  password: '',
  terms: false
})

// Validation logic to ensure clean data for the backend
const isFormValid = computed(() => {
  const hasValidUsername = formData.username.trim().length >= 3
  const hasValidEmail = isValidEmail(formData.email)
  const hasValidPassword = formData.password.length >= 6
  const hasAcceptedTerms = formData.terms === true

  return hasValidUsername && hasValidEmail && hasValidPassword && hasAcceptedTerms
})

const onFormSubmit = () => {
  handleSubmit((data) => {
    // Trim data before sending to backend for extra cleanliness
    const cleanData = {
      ...data,
      username: data.username.trim(),
      email: data.email.trim()
    }
    console.log('Sending clean data to backend:', cleanData)
    alert('Usuario registrado con éxito')
    router.push('/login')
  })
}
</script>


<style scoped>
.checkbox-container {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 20px;
}
</style>
