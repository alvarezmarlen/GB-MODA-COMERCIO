import { reactive, computed } from 'vue'

const state = reactive({
  user: {
    id: 1,
    username: 'Juan Pérez',
    email: 'juan.perez@example.com'
  },
  isAuthenticated: true
})

export function useAuthStore() {
  const user = computed(() => state.user)
  const isAuthenticated = computed(() => state.isAuthenticated)

  const login = (username) => {
    state.user.username = username || 'Juan Pérez'
    state.isAuthenticated = true
  }

  const logout = () => {
    state.user.username = ''
    state.isAuthenticated = false
  }

  return {
    user,
    isAuthenticated,
    login,
    logout
  }
}
