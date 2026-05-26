import { reactive } from 'vue'

const currentStory = reactive({
  title: '',
  countryOrigin: '',
  profession: '',
  ageRange: '',
  description: '',
  images: []
})

// All stories (prepared for backend connection)
const stories = reactive([])

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
