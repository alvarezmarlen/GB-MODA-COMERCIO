import { describe, it, expect, vi, beforeEach } from 'vitest'
import { getStories, getStoryById, createStory, updateStory, deleteStory, uploadStoryImage } from '../stories'

describe('Stories API', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('getStories fetches stories with query params', async () => {
    const mockData = [{ id: 1, title: 'Story 1' }]
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockData
    })

    const result = await getStories({ profession: 'Dev', age_range: '20-30' })
    expect(global.fetch).toHaveBeenCalledWith('/stories?profession=Dev&age_range=20-30')
    expect(result).toEqual(mockData)
  })

  it('getStoryById fetches a single story', async () => {
    const mockData = { id: 1, title: 'Story 1' }
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockData
    })

    const result = await getStoryById(1)
    expect(global.fetch).toHaveBeenCalledWith('/stories/1')
    expect(result).toEqual(mockData)
  })

  it('createStory sends POST request', async () => {
    const payload = { title: 'New Story' }
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ id: 1, ...payload })
    })

    const result = await createStory(payload)
    expect(global.fetch).toHaveBeenCalledWith('/stories', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    expect(result.id).toBe(1)
  })

  it('updateStory sends PUT request', async () => {
    const payload = { title: 'Updated' }
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ id: 1, ...payload })
    })

    const result = await updateStory(1, payload)
    expect(global.fetch).toHaveBeenCalledWith('/stories/1', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    expect(result.title).toBe('Updated')
  })

  it('deleteStory sends DELETE request', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ message: 'Deleted' })
    })

    const result = await deleteStory(1)
    expect(global.fetch).toHaveBeenCalledWith('/stories/1', { method: 'DELETE' })
    expect(result.message).toBe('Deleted')
  })

  it('throws an error when fetch fails', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: false,
      status: 500,
      text: async () => ''
    })

    await expect(getStories()).rejects.toThrow('Error de conexión con el servidor')
  })
})
