async function parseJson(res) {
  try {
    return await res.json()
  } catch {
    const text = await res.text().catch(() => '')
    throw new Error(
      `Error de conexión con el servidor (${res.status}). Asegúrate de que el backend esté corriendo en http://localhost:5000`
    )
  }
}

export async function getStories(filters = {}) {
  const params = new URLSearchParams()
  if (filters.profession) params.append('profession', filters.profession)
  if (filters.age_range) params.append('age_range', filters.age_range)
  if (filters.origin_country) params.append('origin_country', filters.origin_country)
  if (filters.user_id) params.append('user_id', filters.user_id)
  const query = params.toString()
  const res = await fetch(`/stories${query ? '?' + query : ''}`)
  if (!res.ok) {
    await parseJson(res)
    throw new Error('Error al cargar historias')
  }
  return parseJson(res)
}

export async function getStoryById(id) {
  const res = await fetch(`/stories/${id}`)
  if (!res.ok) {
    await parseJson(res)
    throw new Error('Historia no encontrada')
  }
  return parseJson(res)
}

export async function createStory(data) {
  const res = await fetch('/stories', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) {
    const err = await parseJson(res)
    throw new Error(err.errors?._schema || JSON.stringify(err.errors || err))
  }
  return parseJson(res)
}

export async function updateStory(id, data) {
  const res = await fetch(`/stories/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) {
    const err = await parseJson(res)
    throw new Error(JSON.stringify(err.errors || err))
  }
  return parseJson(res)
}

export async function deleteStory(id) {
  const res = await fetch(`/stories/${id}`, { method: 'DELETE' })
  if (!res.ok) {
    const err = await parseJson(res)
    throw new Error(err.error || 'Error al eliminar')
  }
  return parseJson(res)
}

export async function uploadStoryImage(storyId, file) {
  const formData = new FormData()
  formData.append('image', file)
  const res = await fetch(`/stories/${storyId}/images`, {
    method: 'POST',
    body: formData,
  })
  if (!res.ok) {
    const err = await parseJson(res)
    throw new Error(err.error || 'Error al subir imagen')
  }
  return parseJson(res)
}
