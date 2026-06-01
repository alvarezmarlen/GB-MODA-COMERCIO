import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import LoginPage from '../LoginPage.vue'

// Mock useI18n
vi.mock('vue-i18n', () => ({
  useI18n: () => ({
    t: (key) => key
  })
}))

describe('LoginPage.vue', () => {
  it('renders login form and links', () => {
    const wrapper = mount(LoginPage, {
      global: {
        stubs: {
          'router-link': { template: '<a><slot/></a>' },
          AuthTemplate: {
            template: '<div><slot/><slot name="footer"/></div>'
          },
          LoginForm: {
            template: '<form class="login-form"></form>'
          }
        }
      }
    })
    
    expect(wrapper.find('form.login-form').exists()).toBe(true)
    expect(wrapper.text()).toContain('auth.noAccount')
    expect(wrapper.text()).toContain('auth.registerLink')
  })
})
