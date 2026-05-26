import { reactive, computed } from 'vue'

const state = reactive({
  user: {
    username: '',
    email: '',
    password: '',
    role: 'user'
  },
  isAuthenticated: false
})

export function useAuthStore() {
  const user = computed(() => state.user)
  const isAuthenticated = computed(() => state.isAuthenticated)
  const isAdmin = computed(() => state.user.role === 'admin')

  const login = (username, role = 'user') => {
    state.user.username = username || ''
    state.user.role = role
    state.isAuthenticated = true
  }

  const logout = () => {
    state.user.username = ''
    state.user.email = ''
    state.user.password = ''
    state.user.role = 'user'
    state.isAuthenticated = false
  }

  const updateUser = (data) => {
    if (data.username !== undefined) state.user.username = data.username
    if (data.email !== undefined) state.user.email = data.email
    if (data.password !== undefined) state.user.password = data.password
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
