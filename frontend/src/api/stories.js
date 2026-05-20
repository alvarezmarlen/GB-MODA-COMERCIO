export async function createStory(data) {
  const res = await fetch('/stories', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) {
    const err = await res.json()
    throw new Error(err.errors?._schema || JSON.stringify(err.errors || err))
  }
  return res.json()
}

export async function uploadStoryImage(storyId, file) {
  const formData = new FormData()
  formData.append('image', file)
  const res = await fetch(`/stories/${storyId}/images`, {
    method: 'POST',
    body: formData,
  })
  if (!res.ok) {
    const err = await res.json()
    throw new Error(err.error || 'Error al subir imagen')
  }
  return res.json()
}
