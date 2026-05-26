import { describe, it, expect, beforeEach } from 'vitest'

describe('i18n instance', () => {
  beforeEach(() => {
    localStorage.clear()
  })

  it('should use "es" as default locale when nothing is stored', async () => {
    const i18n = (await import('../../src/i18n/index.js')).default
    expect(i18n.global.locale.value).toBe('es')
  })

  it('should read locale from localStorage', async () => {
    localStorage.setItem('locale', 'en')
    const i18n = (await import('../../src/i18n/index.js?version=1')).default
    expect(i18n.global.locale.value).toBe('en')
  })

  it('should have fallback locale set to "es"', async () => {
    const i18n = (await import('../../src/i18n/index.js?version=2')).default
    expect(i18n.global.fallbackLocale.value).toBe('es')
  })

  it('should have messages for all 6 locales', async () => {
    const i18n = (await import('../../src/i18n/index.js?version=3')).default
    const messages = i18n.global.messages.value
    expect(messages).toHaveProperty('es')
    expect(messages).toHaveProperty('en')
    expect(messages).toHaveProperty('eu')
    expect(messages).toHaveProperty('fr')
    expect(messages).toHaveProperty('ro')
    expect(messages).toHaveProperty('ar')
  })

  it('should translate a known key in Spanish', async () => {
    const i18n = (await import('../../src/i18n/index.js?version=4')).default
    expect(i18n.global.t('nav.home')).toBe('Inicio')
    expect(i18n.global.t('footer.copyright')).toContain('GB-MODA-COMERCIO')
  })

  it('should fallback to Spanish for missing keys', async () => {
    localStorage.setItem('locale', 'en')
    const i18n = (await import('../../src/i18n/index.js?version=5')).default
    const translated = i18n.global.t('nav.home')
    expect(translated).toBe('Home')
  })
})
