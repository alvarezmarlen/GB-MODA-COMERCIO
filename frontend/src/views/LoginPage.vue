<template>
  <AuthTemplate title="Iniciar Sesión">
    <LoginForm />
    <template #footer>
      <p>¿No tienes cuenta? <a href="#" @click.prevent="$emit('switch', 'register')">Regístrate</a></p>
    </template>
  </AuthTemplate>
</template>

<script setup>
import AuthTemplate from '../components/templates/AuthTemplate.vue'
import LoginForm from '../components/organisms/LoginForm.vue'

defineEmits(['switch'])
</script>
