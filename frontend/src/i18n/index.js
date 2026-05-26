import { createI18n } from 'vue-i18n'
import { watch } from 'vue'
import es from './locales/es.json'
import en from './locales/en.json'
import eu from './locales/eu.json'
import fr from './locales/fr.json'
import ro from './locales/ro.json'
import ar from './locales/ar.json'


const savedLocale = localStorage.getItem('locale') || 'es'

const i18n = createI18n({
  legacy: false,
  locale: savedLocale,
  fallbackLocale: 'es',
  messages: { es, en, eu, fr, ro, ar }
})

// Watch changes on the global locale to save to localStorage and toggle text direction (RTL/LTR)
watch(i18n.global.locale, (newLocale) => {
  localStorage.setItem('locale', newLocale)
  if (typeof document !== 'undefined') {
    if (newLocale === 'ar') {
      document.documentElement.setAttribute('dir', 'rtl')
    } else {
      document.documentElement.setAttribute('dir', 'ltr')
    }
  }
}, { immediate: true })

export default i18n
