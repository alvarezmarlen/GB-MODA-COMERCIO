<template>
  <AuthTemplate :title="t('auth.registerTitle')">
    <RegisterForm />
    <template #footer>
      <p>{{ t('auth.hasAccount') }} <router-link to="/login">{{ t('auth.loginLink') }}</router-link></p>
    </template>
  </AuthTemplate>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import AuthTemplate from '../components/templates/AuthTemplate.vue'
import RegisterForm from '../components/organisms/RegisterForm.vue'

const { t } = useI18n()
</script>
