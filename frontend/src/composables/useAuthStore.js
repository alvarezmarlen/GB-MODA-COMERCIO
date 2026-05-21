import { ref } from 'vue'

// Estado global (en la memoria de la app)
const token = ref(localStorage.getItem('user_token') || null)
const user = ref(JSON.parse(localStorage.getItem('user_data')) || null)
const error = ref(null)
const loading = ref(false)

export function useAuthStore() {
    
    const login = async (email, password) => {
        loading.value = true
        error.value = null
        
        try {
            // Apuntamos al puerto 5001 que configuramos en Docker Compose
            const response = await fetch('http://127.0.0.1:5001/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            })

            const data = await response.json()

            if (!response.ok) {
                throw new Error(data.message || 'Error al iniciar sesión')
            }

            // 1. Guardar en las variables reactivas de Vue
            token.value = data.token
            user.value = data.user

            // 2. Persistir en el navegador (para que no se desloguee al refrescar)
            localStorage.setItem('user_token', data.token)
            localStorage.setItem('user_data', JSON.stringify(data.user))

            return true // Login exitoso
        } catch (err) {
            error.value = err.message
            return false // Login fallido
        } finally {
            loading.value = false
        }
    }

    const logout = () => {
        token.value = null
        user.value = null
        localStorage.removeItem('user_token')
        localStorage.removeItem('user_data')
    }

    return {
        token,
        user,
        error,
        loading,
        login,
        logout
    }
}
