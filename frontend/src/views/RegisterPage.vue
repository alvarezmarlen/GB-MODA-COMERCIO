<template>
  <AuthTemplate title="Crear Cuenta">
    <RegisterForm />
    <template #footer>
      <p>¿Ya tienes una cuenta? <a href="#" @click.prevent="$emit('switch', 'login')">Inicia sesión</a></p>
    </template>
  </AuthTemplate>
</template>

<script setup>
import AuthTemplate from '../components/templates/AuthTemplate.vue'
import RegisterForm from '../components/organisms/RegisterForm.vue'

defineEmits(['switch'])
</script>
