<template>
  <AuthTemplate :title="t('auth.loginTitle')">
    <LoginForm />
    <template #footer>
      <p>{{ t('auth.noAccount') }} <router-link to="/register">{{ t('auth.registerLink') }}</router-link></p>
    </template>
  </AuthTemplate>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
import AuthTemplate from '../components/templates/AuthTemplate.vue'
import LoginForm from '../components/organisms/LoginForm.vue'

const { t } = useI18n()
</script>
