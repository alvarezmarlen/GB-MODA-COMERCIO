import { describe, it, expect } from 'vitest'
import es from '../../src/i18n/locales/es.json'
import en from '../../src/i18n/locales/en.json'
import eu from '../../src/i18n/locales/eu.json'
import fr from '../../src/i18n/locales/fr.json'
import ro from '../../src/i18n/locales/ro.json'

const locales = { es, en, eu, fr, ro }
const localeNames = Object.keys(locales)
const ES_KEYS = getLeafKeys(es)

function getLeafKeys(obj, prefix = '') {
  return Object.keys(obj).reduce((keys, key) => {
    const fullKey = prefix ? `${prefix}.${key}` : key
    if (typeof obj[key] === 'object' && obj[key] !== null && !Array.isArray(obj[key])) {
      keys.push(...getLeafKeys(obj[key], fullKey))
    } else {
      keys.push(fullKey)
    }
    return keys
  }, [])
}

describe('Locale files structure', () => {
  it.each(localeNames)('%s should have the same leaf keys as es.json', (name) => {
    const keys = getLeafKeys(locales[name])
    expect(keys.sort()).toEqual([...ES_KEYS].sort())
  })

  it.each(localeNames)('all values in %s should be strings', (name) => {
    const locale = locales[name]
    const checkStrings = (obj, path = '') => {
      Object.entries(obj).forEach(([key, value]) => {
        const fullPath = path ? `${path}.${key}` : key
        if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
          checkStrings(value, fullPath)
        } else {
          expect(typeof value, `Expected string at ${fullPath} in ${name}.json`).toBe('string')
        }
      })
    }
    checkStrings(locale)
  })

  it('es.json should have all required top-level keys', () => {
    const topKeys = ['nav', 'footer', 'home', 'auth', 'dashboard', 'admin', 'createStory', 'storyDetail', 'chronicles', 'map', 'professions', 'ages', 'ages_full', 'countries', 'fileUpload', 'lang']
    expect(Object.keys(es).sort()).toEqual(topKeys.sort())
  })

  it('should have no empty string values in any locale', () => {
    localeNames.forEach((name) => {
      const checkEmpty = (obj, path = '') => {
        Object.entries(obj).forEach(([key, value]) => {
          const fullPath = path ? `${path}.${key}` : key
          if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
            checkEmpty(value, fullPath)
          } else {
            expect(value, `Empty string at ${fullPath} in ${name}.json`).not.toBe('')
          }
        })
      }
      checkEmpty(locales[name])
    })
  })
})
