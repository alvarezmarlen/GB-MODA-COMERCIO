import { describe, it, expect, beforeEach } from 'vitest'
import { useStoryStore } from '../useStoryStore'

describe('useStoryStore', () => {
  let store

  beforeEach(() => {
    store = useStoryStore()
    // Reset stories array for consistent testing
    // Since it's a shared reactive array, we need to splice it
    store.stories.splice(0, store.stories.length)
  })

  it('addStory adds a new story', () => {
    const newStory = { title: 'Test', originCountry: 'Spain' }
    store.addStory(newStory)
    
    expect(store.stories.length).toBe(1)
    expect(store.stories[0].title).toBe('Test')
    expect(store.stories[0].id).toBeDefined()
  })

  it('deleteStory removes a story by id', () => {
    store.addStory({ title: 'Story to delete' })
    const storyId = store.stories[0].id
    
    store.deleteStory(storyId)
    expect(store.stories.length).toBe(0)
  })

  it('updateStory modifies existing story', () => {
    store.addStory({ title: 'Original' })
    const storyId = store.stories[0].id
    
    store.updateStory(storyId, { title: 'Updated' })
    expect(store.stories[0].title).toBe('Updated')
  })

  it('setStory updates currentStory', () => {
    store.setStory({ title: 'Current', originCountry: 'Italy' })
    expect(store.currentStory.title).toBe('Current')
    expect(store.currentStory.originCountry).toBe('Italy')
  })
})
