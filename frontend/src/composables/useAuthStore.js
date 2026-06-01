import { reactive, computed } from 'vue'

// Reactive singleton: state persists across all component instances
// Token and user data are persisted in localStorage for session continuity
const state = reactive({
  user: JSON.parse(localStorage.getItem('user')) || null,
  isAuthenticated: !!localStorage.getItem('token'),
  token: localStorage.getItem('token') || null,
  loading: false,
  error: null
})

export function useAuthStore() {
  const user = computed(() => state.user)
  const isAuthenticated = computed(() => state.isAuthenticated)
  const isAdmin = computed(() => state.user?.role === 'admin')
  const loading = computed(() => state.loading)
  const error = computed(() => state.error)
  const token = computed(() => state.token)

  const login = async (email, password) => {
    state.loading = true
    state.error = null
    try {
      const response = await fetch('/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      })

      if (!response.ok) {
        const errorData = await response.json()
        state.error = errorData.error || 'Error al iniciar sesión'
        return false
      }

      const data = await response.json()
      state.user = data.user
      state.token = data.access_token
      state.isAuthenticated = true
      localStorage.setItem('token', data.access_token)
      localStorage.setItem('user', JSON.stringify(data.user))
      alert('Inicio de sesión exitoso')
      return true
    } catch (err) {
      state.error = 'Error de conexión'
      return false
    } finally {
      state.loading = false
    }
  }

  const register = async (userData) => {
    state.loading = true
    state.error = null
    try {
      const response = await fetch('/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData)
      })

      if (!response.ok) {
        const errorData = await response.json()
        state.error = errorData.errors || 'Error en el registro'
        return false
      }

      return true
    } catch (err) {
      state.error = 'Error de conexión'
      return false
    } finally {
      state.loading = false
    }
  }

  const logout = () => {
    state.user = null
    state.token = null
    state.isAuthenticated = false
    localStorage.removeItem('token')
    localStorage.removeItem('user')
  }

  const updateUser = (data) => {
    if (state.user) {
      if (data.username !== undefined) state.user.username = data.username
      if (data.email !== undefined) state.user.email = data.email
      if (data.password !== undefined) state.user.password = data.password
      localStorage.setItem('user', JSON.stringify(state.user))
    }
  }

  return reactive({
    user,
    isAuthenticated,
    isAdmin,
    loading,
    error,
    token,
    login,
    register,
    logout,
    updateUser
  })
}
