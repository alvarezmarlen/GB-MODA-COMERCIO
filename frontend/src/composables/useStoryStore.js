import { reactive } from 'vue'

const currentStory = reactive({
  id: null,
  title: '',
  countryOrigin: '',
  profession: '',
  ageRange: '',
  description: '',
  images: []
})

// All stories (mock data simulating a database)
const stories = reactive([
  {
    id: 1,
    title: 'El oficio de la costura artesanal',
    countryOrigin: 'España',
    profession: 'casa',
    ageRange: '46_60',
    description: 'Una historia sobre el arte de la costura transmitido de generación en generación en los hogares españoles.',
    images: [],
    author: 'Juan Pérez'
  },
  {
    id: 2,
    title: 'Comercio local en el mercado central',
    countryOrigin: 'México',
    profession: 'industria',
    ageRange: '36_45',
    description: 'La vida cotidiana de los comerciantes que mantienen viva la tradición del mercado central.',
    images: [],
    author: 'María García'
  },
  {
    id: 3,
    title: 'Tejidos de la sierra',
    countryOrigin: 'Perú',
    profession: 'campo',
    ageRange: '26_35',
    description: 'Los tejidos andinos representan siglos de tradición cultural y artesanía local.',
    images: [],
    author: 'Juan Pérez'
  }
])

let nextId = 4

export function useStoryStore() {
  const setStory = (storyData) => {
    Object.assign(currentStory, {
      title: storyData.title || '',
      countryOrigin: storyData.countryOrigin || '',
      profession: storyData.profession || '',
      ageRange: storyData.ageRange || '',
      description: storyData.description || '',
      images: storyData.images || []
    })
  }

  const addStory = (storyData) => {
    stories.push({
      id: nextId++,
      ...storyData
    })
  }

  const deleteStory = (storyId) => {
    const index = stories.findIndex(s => s.id === storyId)
    if (index !== -1) {
      stories.splice(index, 1)
    }
  }

  const updateStory = (storyId, updatedData) => {
    const index = stories.findIndex(s => s.id === storyId)
    if (index !== -1) {
      Object.assign(stories[index], updatedData)
    }
  }

  return {
    currentStory,
    stories,
    setStory,
    addStory,
    deleteStory,
    updateStory
  }
}
