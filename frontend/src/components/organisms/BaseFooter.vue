<template>
  <footer class="base-footer">
    <div class="footer-divider"></div>
    <div class="footer-content">
      <div class="copyright">
        {{ t('footer.copyright') }}
      </div>
      <div class="footer-links">
        <a href="#" @click.prevent="openLegalModal('terminos')" class="footer-link">{{ t('footer.terms') }}</a>
        <span class="divider">│</span>
        <a href="#" @click.prevent="openLegalModal('privacidad')" class="footer-link">{{ t('footer.privacy') }}</a>
        <span class="divider">│</span>
        <a href="#" @click.prevent="openLegalModal('contacto')" class="footer-link">{{ t('footer.contact') }}</a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { inject } from 'vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
const openLegalModal = inject('openLegalModal')
</script>

<style scoped>
.base-footer {
  margin-top: var(--wf-spacing-lg);
  padding: calc(var(--wf-spacing-lg) * 1.2) var(--wf-spacing-lg);
  font-family: var(--font-body);
  background: #FCD015;
}


.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: #000000;
  gap: var(--wf-spacing-md);
}

.footer-links {
  display: flex;
  align-items: center;
  gap: 8px;
}

.footer-link {
  color: #000000;
  text-decoration: none;
  border-bottom: 1px dashed transparent;
  transition: all 0.2s ease;
}

.footer-link:hover {
  border-bottom: 1px dashed rgba(0, 0, 0, 0.45);
}

.divider {
  color: rgba(0, 0, 0, 0.6);
  font-size: 0.8rem;
}

@media (max-width: 600px) {
  .footer-content {
    flex-direction: column;
    text-align: center;
    gap: var(--wf-spacing-sm);
  }
}
</style>
