import { describe, it, expect, vi, beforeEach } from 'vitest'
import { updateUser, getUserById } from '../users'

describe('Users API', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    localStorage.clear()
  })

  it('updateUser sends PUT request with token if available', async () => {
    localStorage.setItem('token', 'fake-token')
    const payload = { username: 'newuser' }
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ id: 1, ...payload })
    })

    const result = await updateUser(1, payload)
    expect(global.fetch).toHaveBeenCalledWith('/users/1', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer fake-token'
      },
      body: JSON.stringify(payload)
    })
    expect(result.username).toBe('newuser')
  })

  it('getUserById fetches user data', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ id: 2, username: 'test' })
    })

    const result = await getUserById(2)
    expect(global.fetch).toHaveBeenCalledWith('/users/2')
    expect(result.id).toBe(2)
  })
})
