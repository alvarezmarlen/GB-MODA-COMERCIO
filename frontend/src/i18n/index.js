import { createI18n } from 'vue-i18n'
import ar from './locales/ar.json'
import es from './locales/es.json'
import en from './locales/en.json'
import eu from './locales/eu.json'
import fr from './locales/fr.json'
import ro from './locales/ro.json'


const savedLocale = localStorage.getItem('locale') || 'es'

const i18n = createI18n({
  legacy: false,
  locale: savedLocale,
  fallbackLocale: 'es',
  messages: { ar, es, en, eu, fr, ro }
})

export default i18n
