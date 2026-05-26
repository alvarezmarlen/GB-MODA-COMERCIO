<template>
  <form @submit.prevent="onFormSubmit" class="login-form">
    <div v-if="errorMessage" class="error-banner">{{ errorMessage }}</div>
    <FormField
      :label="t('auth.emailLabel')"
      v-model="formData.email"
      type="email"
      name="email"
      autocomplete="username"
      :placeholder="t('auth.emailPlaceholder')"
      :disabled="isLoading"
    />
    <FormField
      :label="t('auth.passwordLabel')"
      type="password"
      v-model="formData.password"
      name="password"
      autocomplete="current-password"
      :placeholder="t('auth.passwordPlaceholder')"
      :disabled="isLoading"
    />
    <BaseButton type="submit" :disabled="!isFormValid || isLoading">
      {{ isLoading ? '...' : t('auth.loginButton') }}
    </BaseButton>
  </form>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import FormField from '../molecules/FormField.vue'
import BaseButton from '../atoms/BaseButton.vue'
import { useForm } from '../../composables/useForm'
import { useAuthStore } from '../../composables/useAuthStore'

const { t } = useI18n()
const router = useRouter()
const { login } = useAuthStore()
const { formData, resetForm, handleSubmit } = useForm({
  email: '',
  password: ''
})

onMounted(resetForm)

const errorMessage = ref('')
const isLoading = ref(false)

const isFormValid = computed(() => {
  return formData.email.trim().length > 0 && 
         formData.password.length > 0
})

const onFormSubmit = () => {
  handleSubmit(async (data) => {
    errorMessage.value = ''
    isLoading.value = true
    try {
      const cleanEmail = data.email.trim()
      await login(cleanEmail, data.password)
      router.push('/')
    } catch (err) {
      errorMessage.value = err.message || 'Error al iniciar sesión'
    } finally {
      isLoading.value = false
    }
  })
}
</script>

<style scoped>
.error-banner {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 15px;
  font-size: 0.9rem;
  text-align: center;
}
</style>
