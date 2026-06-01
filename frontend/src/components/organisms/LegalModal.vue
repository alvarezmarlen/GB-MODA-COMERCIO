<template>
  <div v-if="isOpen" class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <button class="close-btn" @click="close">✕</button>
      <div class="modal-body" ref="modalBody">
        <h1 id="title">{{ t('legal.title') }}</h1>
        <p class="last-update">{{ t('legal.lastUpdate') }}</p>
        
        <p>{{ t('legal.intro') }}</p>
        
        <h2 id="terminos">{{ t('legal.section1Title') }}</h2>
        <p>{{ t('legal.section1Text') }}</p>
        
        <h2>{{ t('legal.section2Title') }}</h2>
        <p>{{ t('legal.section2Intro') }}</p>
        <ul>
          <li>{{ t('legal.section2Item1') }}</li>
          <li>{{ t('legal.section2Item2') }}</li>
          <li>{{ t('legal.section2Item3') }}</li>
        </ul>
        
        <h2 id="privacidad">{{ t('legal.section3Title') }}</h2>
        <p>{{ t('legal.section3Intro') }}</p>
        <ul>
          <li><strong>{{ t('legal.section3Item1Label') }}</strong> {{ t('legal.section3Item1Text') }}</li>
          <li><strong>{{ t('legal.section3Item2Label') }}</strong> {{ t('legal.section3Item2Text') }}</li>
          <li><strong>{{ t('legal.section3Item3Label') }}</strong> {{ t('legal.section3Item3Text') }}</li>
        </ul>
        
        <h2>{{ t('legal.section4Title') }}</h2>
        <p>{{ t('legal.section4Text') }}</p>
        
        <h2>{{ t('legal.section5Title') }}</h2>
        <p>{{ t('legal.section5Text') }}</p>
        
        <h2 id="contacto">{{ t('legal.section6Title') }}</h2>
        <p>{{ t('legal.section6Text') }} <a href="mailto:info@grupopenascal.com">info@grupopenascal.com</a>.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, nextTick } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true
  },
  section: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['close'])

const modalBody = ref(null)

const close = () => {
  emit('close')
}

watch(() => props.isOpen, async (newVal) => {
  if (newVal && props.section) {
    await nextTick()
    scrollToSection(props.section)
  }
})

watch(() => props.section, async (newVal) => {
  if (props.isOpen && newVal) {
    await nextTick()
    scrollToSection(newVal)
  }
})

const scrollToSection = (id) => {
  const element = document.getElementById(id)
  if (element && modalBody.value) {
    modalBody.value.scrollTo({
      top: element.offsetTop - 20,
      behavior: 'smooth'
    })
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: var(--color-white);
  width: 90%;
  max-width: 800px;
  height: 80vh;
  border-radius: var(--wf-radius);
  position: relative;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--color-red);
}

.modal-body {
  padding: 40px;
  overflow-y: auto;
  flex: 1;
}

.modal-body h1 {
  font-size: 1.8rem;
  color: var(--color-yellow);
  margin-bottom: 5px;
  border-bottom: 2px solid var(--color-red);
  padding-bottom: 10px;
}

.last-update {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 20px;
}

.modal-body h2 {
  font-size: 1.3rem;
  color: var(--color-primary);
  margin-top: 30px;
  margin-bottom: 10px;
}

.modal-body p, .modal-body ul {
  line-height: 1.6;
  margin-bottom: 15px;
  color: #333;
}

.modal-body ul {
  padding-left: 20px;
}

.modal-body li {
  margin-bottom: 8px;
}
</style>
