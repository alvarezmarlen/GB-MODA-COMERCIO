<template>
  <AuthTemplate title="Crear Cuenta">
    <RegisterForm />
    <template #footer>
      <p>¿Ya tienes una cuenta? <router-link to="/login">Inicia sesión</router-link></p>
    </template>
  </AuthTemplate>
</template>

<script setup>
import AuthTemplate from '../components/templates/AuthTemplate.vue'
import RegisterForm from '../components/organisms/RegisterForm.vue'
</script>
