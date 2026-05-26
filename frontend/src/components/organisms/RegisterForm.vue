<template>
  <form @submit.prevent="onFormSubmit" class="register-form">
    <div v-if="errorMessage" class="error-banner">{{ errorMessage }}</div>
    <div v-if="successMessage" class="success-banner">{{ successMessage }}</div>
    <FormField
      :label="t('auth.usernameLabel')"
      v-model="formData.username"
      :placeholder="t('auth.usernameMinPlaceholder')"
      :disabled="isLoading"
    />
    
    <FormField
      :label="t('auth.emailLabel')"
      type="email"
      v-model="formData.email"
      :placeholder="t('auth.emailPlaceholder')"
      :disabled="isLoading"
    />
    
    <FormField
      :label="t('auth.passwordLabel')"
      type="password"
      v-model="formData.password"
      :placeholder="t('auth.passwordMinPlaceholder')"
      :disabled="isLoading"
    />

    <div class="checkbox-container">
      <BaseCheckbox v-model="formData.terms" :disabled="isLoading" />
      <BaseLabel>{{ t('auth.termsLabel') }}</BaseLabel>
    </div>

    <BaseButton type="submit" :disabled="!isFormValid || isLoading">
      {{ isLoading ? '...' : t('auth.registerButton') }}
    </BaseButton>
  </form>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import FormField from '../molecules/FormField.vue'
import BaseButton from '../atoms/BaseButton.vue'
import BaseCheckbox from '../atoms/BaseCheckbox.vue'
import BaseLabel from '../atoms/BaseLabel.vue'
import { useForm } from '../../composables/useForm'

const { t } = useI18n()
const router = useRouter()
const { formData, handleSubmit, isValidEmail } = useForm({
  username: '',
  email: '',
  password: '',
  terms: false
})

const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

const isFormValid = computed(() => {
  const hasValidUsername = formData.username.trim().length >= 3
  const hasValidEmail = isValidEmail(formData.email)
  const hasValidPassword = formData.password.length >= 6
  const hasAcceptedTerms = formData.terms === true

  return hasValidUsername && hasValidEmail && hasValidPassword && hasAcceptedTerms
})

const onFormSubmit = () => {
  handleSubmit(async (data) => {
    errorMessage.value = ''
    successMessage.value = ''
    isLoading.value = true
    try {
      const res = await fetch('/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          nombre_usuario: data.username.trim(),
          email: data.email.trim(),
          password: data.password
        })
      })
      if (!res.ok) {
        const err = await res.json().catch(() => ({}))
        throw new Error(err.error || 'Error al registrar el usuario')
      }
      successMessage.value = t('auth.registerSuccess') || 'Usuario registrado con éxito'
      setTimeout(() => {
        router.push('/login')
      }, 1500)
    } catch (err) {
      errorMessage.value = err.message || 'Error al registrar el usuario'
    } finally {
      isLoading.value = false
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
.success-banner {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 15px;
  font-size: 0.9rem;
  text-align: center;
}
</style>
