<template>
  <form @submit.prevent="onFormSubmit" class="login-form">
    <FormField
      label="Email"
      type="email"
      v-model="formData.email"
      placeholder="correo@ejemplo.com"
    />
    <FormField
      label="Contraseña"
      type="password"
      v-model="formData.password"
      placeholder="********"
    />
    <p v-if="authStore.error" class="error-text">{{ authStore.error }}</p>
    <BaseButton type="submit" :disabled="!isFormValid || authStore.loading">
      {{ authStore.loading ? 'Verificando...' : 'Iniciar sesión' }}
    </BaseButton>
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
const authStore = useAuthStore()
const { login } = authStore
const { formData, handleSubmit } = useForm({
  email: '',
  password: ''
})

const isFormValid = computed(() => {
  return formData.email.trim().length > 0 && formData.password.length > 0
})

const onFormSubmit = () => {
  handleSubmit(async (data) => {
    const cleanEmail = data.email.trim()
    const success = await login(cleanEmail, data.password)
    if (success) {
      router.push('/')
    }
  })
}
</script>
