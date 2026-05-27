<template>
  <form @submit.prevent="onFormSubmit" class="login-form">
    <FormField
      :label="t('auth.emailLabel')"
      type="email"
      v-model="formData.email"
      :placeholder="t('auth.emailPlaceholder')"
    />
    <FormField
      :label="t('auth.passwordLabel')"
      type="password"
      v-model="formData.password"
      :placeholder="t('auth.passwordPlaceholder')"
    />
    <p v-if="authStore.error" class="error-text">{{ authStore.error }}</p>
    <BaseButton type="submit" :disabled="!isFormValid || authStore.loading">
      {{ authStore.loading ? 'Verificando...' : t('auth.loginButton')}}
    </BaseButton>
  </form>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import FormField from '../molecules/FormField.vue'
import BaseButton from '../atoms/BaseButton.vue'
import { useForm } from '../../composables/useForm'
import { useAuthStore } from '../../composables/useAuthStore'

const { t } = useI18n()
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
