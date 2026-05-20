import { reactive } from 'vue'

export function useForm(initialState) {
  const formData = reactive({ ...initialState })

  const resetForm = () => {
    Object.assign(formData, initialState)
  }

  // Basic email validation regex
  const isValidEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return re.test(email)
  }

  const handleSubmit = async (callback) => {
    await callback(formData)
  }

  return {
    formData,
    resetForm,
    handleSubmit,
    isValidEmail
  }
}
