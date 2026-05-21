import { reactive } from 'vue'

const currentStory = reactive({
  id: null,
  title: '',
  countryOrigin: '',
  origin_country: '',
  profession: '',
  age: null,
  description: '',
  content: '',
  images: []
})

export function useStoryStore() {
  const setStory = (storyData) => {
    Object.assign(currentStory, {
      id: storyData.id !== undefined ? storyData.id : null,
      title: storyData.title || '',
      countryOrigin: storyData.countryOrigin || storyData.origin_country || '',
      origin_country: storyData.origin_country || storyData.countryOrigin || '',
      profession: storyData.profession || '',
      age: storyData.age || null,
      description: storyData.description || '',
      content: storyData.content || storyData.description || '',
      images: storyData.images || []
    })
  }

  return {
    currentStory,
    setStory
  }
}
