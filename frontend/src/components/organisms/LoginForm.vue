<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../composables/useAuthStore'

// 1. Instanciamos las herramientas una sola vez
const authStore = useAuthStore()
const router = useRouter()

// 2. Estado reactivo para tus inputs (comprueba si en tu HTML usas formData o campos sueltos)
const formData = ref({
  email: '',
  password: ''
})

// 3. Función de envío limpia y conectada al backend
const handleSubmit = async () => {
  if (!formData.value.email || !formData.value.password) return

  // Llamamos al store que conecta con Docker (puerto 5001)
  const success = await authStore.login(formData.value.email, formData.value.password)
  
  if (success) {
    // Si la base de datos dice que OK, viajamos a la página de inicio
    router.push('/') 
  }
}
</script>

<template>
  <div class="login-organism">
    <form @submit.prevent="handleSubmit" class="form-container">
      
      <div class="field">
        <label>Email</label>
        <input type="email" v-model="formData.email" required placeholder="correo@ejemplo.com" />
      </div>

      <div class="field">
        <label>Contraseña</label>
        <input type="password" v-model="formData.password" required placeholder="********" />
      </div>

      <p v-if="authStore.error" class="error-text">{{ authStore.error }}</p>

      <button type="submit" :disabled="authStore.loading">
        {{ authStore.loading ? 'Verificando...' : 'Iniciar sesión' }}
      </button>
    </form>
  </div>
</template>

<style scoped>
.error-text {
  color: #ff4d4d;
  font-size: 0.85rem;
  margin: 10px 0;
}
.form-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>