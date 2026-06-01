import { describe, it, expect, beforeEach, vi } from 'vitest'
import { mount, RouterLinkStub } from '@vue/test-utils'
import { createI18n } from 'vue-i18n'
import es from '../../src/i18n/locales/es.json'
import en from '../../src/i18n/locales/en.json'
import eu from '../../src/i18n/locales/eu.json'
import fr from '../../src/i18n/locales/fr.json'
import ro from '../../src/i18n/locales/ro.json'
import BaseNavbar from '../../src/components/organisms/BaseNavbar.vue'

vi.mock('vue-router', () => ({
  useRouter: () => ({
    push: vi.fn(),
  }),
  useRoute: () => ({
    path: '/',
  }),
}))

function createTestI18n(locale = 'es') {
  return createI18n({
    legacy: false,
    locale,
    fallbackLocale: 'es',
    messages: { es, en, eu, fr, ro }
  })
}

function mountNavbar(locale = 'es') {
  const i18n = createTestI18n(locale)
  return mount(BaseNavbar, {
    global: {
      plugins: [i18n],
      stubs: {
        RouterLink: RouterLinkStub,
      },
    }
  })
}

describe('BaseNavbar language selector', () => {
  beforeEach(() => {
    localStorage.clear()
  })

  it('should render a select with 5 language options', () => {
    const wrapper = mountNavbar()
    const select = wrapper.find('select.lang-select')
    expect(select.exists()).toBe(true)
    const options = select.findAll('option')
    expect(options).toHaveLength(5)
    const values = options.map(o => o.attributes('value'))
    expect(values).toEqual(['es', 'en', 'eu', 'fr', 'ro'])
  })

  it('should show correct option labels for each language', () => {
    const wrapper = mountNavbar()
    const options = wrapper.findAll('option')
    const labels = options.map(o => o.text())
    expect(labels).toContain('Español')
    expect(labels).toContain('English')
    expect(labels).toContain('Euskera')
    expect(labels).toContain('Français')
    expect(labels).toContain('Română')
  })

  it('should have the correct initial locale selected', () => {
    const wrapper = mountNavbar('en')
    const select = wrapper.find('select.lang-select')
    expect(select.element.value).toBe('en')
  })

  it('should change displayed locale when selecting a different language', async () => {
    const wrapper = mountNavbar('es')
    const select = wrapper.find('select.lang-select')

    await select.setValue('en')

    const navLinks = wrapper.findAllComponents(RouterLinkStub)
    const homeLink = navLinks.find(s => s.text().includes('Home'))
    expect(homeLink).toBeTruthy()
  })

  it('should persist the selected locale in localStorage', async () => {
    const wrapper = mountNavbar('es')
    const select = wrapper.find('select.lang-select')

    await select.setValue('fr')
    expect(localStorage.getItem('locale')).toBe('fr')

    await select.setValue('ro')
    expect(localStorage.getItem('locale')).toBe('ro')
  })

  it('should start with default "es" locale if nothing in localStorage', () => {
    const wrapper = mountNavbar()
    const select = wrapper.find('select.lang-select')
    expect(select.element.value).toBe('es')
  })
})
