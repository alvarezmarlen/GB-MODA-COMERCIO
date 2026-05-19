<template>
  <AuthTemplate title="Iniciar Sesión">
    <LoginForm />
    <template #footer>
      <p>¿No tienes cuenta? <router-link to="/register">Regístrate</router-link></p>
    </template>
  </AuthTemplate>
</template>

<script setup>
import AuthTemplate from '../components/templates/AuthTemplate.vue'
import LoginForm from '../components/organisms/LoginForm.vue'
</script>
