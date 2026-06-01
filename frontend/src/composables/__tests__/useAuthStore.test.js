import { describe, it, expect, beforeEach, vi } from 'vitest'
import { useAuthStore } from '../useAuthStore'

describe('useAuthStore', () => {
  let authStore

  beforeEach(() => {
    // Clear localStorage and fetch mock
    localStorage.clear()
    vi.clearAllMocks()
    
    // Create fresh instance
    authStore = useAuthStore()
    
    // Reset state to initial manually since it uses a shared reactive object outside the function
    authStore.logout()
  })

  it('login success sets user, token, and localStorage', async () => {
    const mockUser = { email: 'test@estudioenpenascal.com', role: 'customer' }
    const mockToken = 'fake-jwt-token'
    
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        user: mockUser,
        access_token: mockToken
      })
    })

    const result = await authStore.login('test@estudioenpenascal.com', 'password123')
    
    expect(result).toBe(true)
    expect(authStore.isAuthenticated).toBe(true)
    expect(authStore.user).toEqual(mockUser)
    expect(authStore.token).toBe(mockToken)
    expect(localStorage.setItem).toHaveBeenCalledWith('token', mockToken)
    expect(localStorage.setItem).toHaveBeenCalledWith('user', JSON.stringify(mockUser))
  })

  it('login failure sets error', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: false,
      json: async () => ({ error: 'Invalid credentials' })
    })

    const result = await authStore.login('test@test.com', 'wrong')
    
    expect(result).toBe(false)
    expect(authStore.isAuthenticated).toBe(false)
    expect(authStore.error).toBe('Invalid credentials')
  })

  it('logout clears state and localStorage', async () => {
    // Set some state first
    authStore.login('test', 'test') // We don't await, just to force some state changes or mock it
    
    authStore.logout()
    
    expect(authStore.isAuthenticated).toBe(false)
    expect(authStore.user).toBe(null)
    expect(authStore.token).toBe(null)
    expect(localStorage.removeItem).toHaveBeenCalledWith('token')
    expect(localStorage.removeItem).toHaveBeenCalledWith('user')
  })

  it('register success', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ id: 1, email: 'new@test.com' })
    })

    const result = await authStore.register({ email: 'new@test.com', password: 'pass' })
    expect(result).toBe(true)
  })

  it('register failure sets error', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: false,
      json: async () => ({ errors: 'Email already exists' })
    })

    const result = await authStore.register({ email: 'existing@test.com', password: 'pass' })
    expect(result).toBe(false)
    expect(authStore.error).toBe('Email already exists')
  })
})
