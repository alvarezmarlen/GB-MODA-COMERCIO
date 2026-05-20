import { reactive } from 'vue'

const currentStory = reactive({
  id: null,
  title: '',
  countryOrigin: '',
  profession: '',
  age: null,
  description: '',
  images: []
})

export function useStoryStore() {
  const setStory = (storyData) => {
    Object.assign(currentStory, {
      id: storyData.id !== undefined ? storyData.id : null,
      title: storyData.title || '',
      countryOrigin: storyData.countryOrigin || '',
      profession: storyData.profession || '',
      age: storyData.age || null,
      description: storyData.description || '',
      images: storyData.images || []
    })
  }

  return {
    currentStory,
    setStory
  }
}
