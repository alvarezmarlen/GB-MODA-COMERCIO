import { reactive, computed } from 'vue'

const savedUser = localStorage.getItem('user')
const savedToken = localStorage.getItem('access_token')

const initialState = savedUser && savedToken ? {
  user: JSON.parse(savedUser),
  isAuthenticated: true
} : {
  user: {
    id: null,
    username: '',
    email: '',
    role: 'customer'
  },
  isAuthenticated: false
}

const state = reactive(initialState)

export function useAuthStore() {
  const user = computed(() => state.user)
  const isAuthenticated = computed(() => state.isAuthenticated)
  const isAdmin = computed(() => state.user.role === 'admin')

  const login = async (emailOrUsername, password) => {
    const res = await fetch('/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: emailOrUsername, password })
    })
    if (!res.ok) {
      const err = await res.json().catch(() => ({}))
      throw new Error(err.error || 'Error al iniciar sesión')
    }
    const data = await res.json()
    
    // Store tokens and user details
    localStorage.setItem('access_token', data.access_token)
    localStorage.setItem('refresh_token', data.refresh_token)
    localStorage.setItem('user', JSON.stringify(data.user))
    
    // Update state
    state.user = data.user
    state.isAuthenticated = true
    return data
  }

  const logout = async () => {
    const token = localStorage.getItem('access_token')
    if (token) {
      try {
        await fetch('/auth/logout', {
          method: 'POST',
          headers: { 'Authorization': `Bearer ${token}` }
        })
      } catch (e) {
        console.error('Error logging out from server:', e)
      }
    }
    // Clear everything from storage and state
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')
    
    state.user = {
      id: null,
      username: '',
      email: '',
      role: 'customer'
    }
    state.isAuthenticated = false
  }

  const updateUser = (data) => {
    if (data.username !== undefined) state.user.username = data.username
    if (data.email !== undefined) state.user.email = data.email
    if (data.role !== undefined) state.user.role = data.role
    localStorage.setItem('user', JSON.stringify(state.user))
  }

  return {
    user,
    isAuthenticated,
    isAdmin,
    login,
    logout,
    updateUser
  }
}
