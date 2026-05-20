<template>
  <form @submit.prevent="onFormSubmit" class="login-form">
    <FormField
      label="Nombre de usuario"
      v-model="formData.username"
      placeholder="Tu nombre de usuario"
    />
    <FormField
      label="Contraseña"
      type="password"
      v-model="formData.password"
      placeholder="********"
    />
    <BaseButton type="submit" :disabled="!isFormValid">Iniciar sesión</BaseButton>
  </form>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import FormField from '../molecules/FormField.vue'
import BaseButton from '../atoms/BaseButton.vue'
import { useForm } from '../../composables/useForm'
import { useAuthStore } from '../../composables/useAuthStore'

const router = useRouter()
const { login } = useAuthStore()
const { formData, handleSubmit } = useForm({
  username: '',
  password: ''
})

// Validation for login: fields must not be empty (or just spaces)
const isFormValid = computed(() => {
  return formData.username.trim().length > 0 && 
         formData.password.length > 0
})

const onFormSubmit = () => {
  handleSubmit((data) => {
    const cleanUsername = data.username.trim()
    console.log('Login attempt with clean data:', {
      ...data,
      username: cleanUsername
    })
    login(cleanUsername)
    alert('Sesión iniciada con éxito')
    router.push('/')
  })
}
</script>

