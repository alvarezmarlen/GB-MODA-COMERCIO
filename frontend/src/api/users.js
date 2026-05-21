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

export async function updateUser(userId, data) {
  const res = await fetch(`/users/${userId}`, {
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

export async function getUserById(id) {
  const res = await fetch(`/users/${id}`)
  if (!res.ok) {
    await parseJson(res)
    throw new Error('Usuario no encontrado')
  }
  return parseJson(res)
}
