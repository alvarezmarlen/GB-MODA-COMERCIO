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

    <p v-if="authStore.error" class="error-text">{{ authStore.error }}</p>
    <BaseButton type="submit" :disabled="!isFormValid || authStore.loading">
      {{ authStore.loading ? 'Registrando...' : 'Registrarse' }}
    </BaseButton>
  </form>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import FormField from '../molecules/FormField.vue'
import BaseButton from '../atoms/BaseButton.vue'
import BaseCheckbox from '../atoms/BaseCheckbox.vue'
import BaseLabel from '../atoms/BaseLabel.vue'
import { useForm } from '../../composables/useForm'
import { useAuthStore } from '../../composables/useAuthStore'

const router = useRouter()
const authStore = useAuthStore()
const { register } = authStore
const { formData, handleSubmit, isValidEmail } = useForm({
  username: '',
  email: '',
  password: '',
  terms: false
})

const isFormValid = computed(() => {
  const hasValidUsername = formData.username.trim().length >= 3
  const hasValidEmail = isValidEmail(formData.email)
  const hasValidPassword = formData.password.length >= 6
  const hasAcceptedTerms = formData.terms === true

  return hasValidUsername && hasValidEmail && hasValidPassword && hasAcceptedTerms
})

const onFormSubmit = () => {
  handleSubmit(async (data) => {
    const cleanData = {
      nombre_usuario: data.username.trim(),
      email: data.email.trim(),
      password: data.password
    }
    const success = await register(cleanData)
    if (success) {
      router.push('/login')
    }
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

.error-text {
  color: #ff4d4d;
  font-size: 0.85rem;
  margin: 10px 0;
}
</style>
