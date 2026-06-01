import { describe, it, expect, vi, beforeEach } from 'vitest'
import { mount } from '@vue/test-utils'
import HomeView from '../HomeView.vue'
import { useAuthStore } from '../../composables/useAuthStore'

vi.mock('vue-i18n', () => ({
  useI18n: () => ({
    t: (key) => key
  })
}))

vi.mock('../../composables/useAuthStore', () => ({
  useAuthStore: vi.fn()
}))

describe('HomeView.vue', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('renders login prompt when not authenticated', () => {
    useAuthStore.mockReturnValue({ isAuthenticated: false })

    const wrapper = mount(HomeView, {
      global: {
        stubs: {
          'router-link': true,
          InteractiveMap: true,
          ChronicleList: true
        }
      }
    })

    expect(wrapper.find('.login-prompt').exists()).toBe(true)
    expect(wrapper.text()).toContain('home.loginPromptTitle')
    expect(wrapper.findComponent({ name: 'ChronicleList' }).exists()).toBe(false)
  })

  it('renders ChronicleList when authenticated', () => {
    useAuthStore.mockReturnValue({ isAuthenticated: true })

    const wrapper = mount(HomeView, {
      global: {
        stubs: {
          'router-link': true,
          InteractiveMap: true,
          ChronicleList: {
            template: '<div class="chronicle-list-mock"></div>'
          }
        }
      }
    })

    expect(wrapper.find('.login-prompt').exists()).toBe(false)
    expect(wrapper.find('.chronicle-list-mock').exists()).toBe(true)
  })
})
