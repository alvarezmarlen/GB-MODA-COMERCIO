import { reactive } from 'vue'

const currentStory = reactive({
  title: '',
  countryOrigin: '',
  profession: '',
  ageRange: '',
  description: '',
  images: []
})

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

  return {
    currentStory,
    setStory
  }
}
