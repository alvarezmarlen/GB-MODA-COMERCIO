<template>
  <form @submit.prevent="onFormSubmit" class="register-form">
    <FormField
      :label="t('auth.usernameLabel')"
      v-model="formData.username"
      :placeholder="t('auth.usernameMinPlaceholder')"
    />
    
    <FormField
      :label="t('auth.emailLabel')"
      type="email"
      v-model="formData.email"
      :placeholder="t('auth.emailPlaceholder')"
    />
    <p v-if="emailDomainError" class="hint-error">
      Solo se permiten correos corporativos autorizados
    </p>
    
    <FormField
      :label="t('auth.passwordLabel')"
      type="password"
      v-model="formData.password"
      :placeholder="t('auth.passwordMinPlaceholder')"
    />

    <div class="checkbox-container">
      <BaseCheckbox v-model="formData.terms" />
      <BaseLabel>{{ t('auth.termsLabel') }}</BaseLabel>
    </div>

    <p v-if="authStore.error" class="error-text">{{ authStore.error }}</p>
    <BaseButton type="submit" :disabled="!isFormValid || authStore.loading">
      {{ authStore.loading ? t('auth.registering') : t('auth.registerButton') }}
    </BaseButton>
  </form>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import FormField from '../molecules/FormField.vue'
import BaseButton from '../atoms/BaseButton.vue'
import BaseCheckbox from '../atoms/BaseCheckbox.vue'
import BaseLabel from '../atoms/BaseLabel.vue'
import { useForm } from '../../composables/useForm'
import { useAuthStore } from '../../composables/useAuthStore'

const { t } = useI18n()
const router = useRouter()
const authStore = useAuthStore()
const { register } = authStore
const { formData, handleSubmit, isValidEmail } = useForm({
  username: '',
  email: '',
  password: '',
  terms: false
})

const emailDomainError = computed(() => {
  return formData.email.length > 0 &&
    isValidEmail(formData.email) &&
    !formData.email.trim().toLowerCase().endsWith('@estudioenpenascal.com')
})

const isFormValid = computed(() => {
  const hasValidUsername = formData.username.trim().length >= 3
  const hasValidEmail = isValidEmail(formData.email)
  const hasValidDomain = hasValidEmail && formData.email.trim().toLowerCase().endsWith('@estudioenpenascal.com')
  const hasValidPassword = formData.password.length >= 6
  const hasAcceptedTerms = formData.terms === true

  return hasValidUsername && hasValidDomain && hasValidPassword && hasAcceptedTerms
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

.hint-error{
  color: #ff4d4f;
  font-size: 0.8rem;
  margin: -10px 0 10px 0;
}
</style>
