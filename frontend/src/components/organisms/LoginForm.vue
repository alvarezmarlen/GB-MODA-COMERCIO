<template>
  <form @submit.prevent="onFormSubmit" class="login-form">
    <FormField
      :label="t('auth.usernameLabel')"
      v-model="formData.username"
      :placeholder="t('auth.usernamePlaceholder')"
    />
    <FormField
      :label="t('auth.passwordLabel')"
      type="password"
      v-model="formData.password"
      :placeholder="t('auth.passwordPlaceholder')"
    />
    <BaseButton type="submit" :disabled="!isFormValid">{{ t('auth.loginButton') }}</BaseButton>
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
const { login } = useAuthStore()
const { formData, handleSubmit } = useForm({
  username: '',
  password: ''
})

const isFormValid = computed(() => {
  return formData.username.trim().length > 0 && 
         formData.password.length > 0
})

const onFormSubmit = () => {
  handleSubmit((data) => {
    const cleanUsername = data.username.trim()
    login(cleanUsername)
    router.push('/')
  })
}
</script>
