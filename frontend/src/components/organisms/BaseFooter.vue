<template>
  <footer class="base-footer">
    <div class="footer-divider"></div>
    <div class="footer-content">
      <div class="copyright">
        © 2026 GB-MODA-COMERCIO. Todos los derechos reservados.
      </div>
      <div class="footer-links">
        <a href="#" class="footer-link" @click.prevent="openLegalModal('terminos')">Términos y Condiciones</a>
        <span class="divider">│</span>
        <a href="#" class="footer-link" @click.prevent="openLegalModal('privacidad')">Politicas de Privacidad</a>
        <span class="divider">│</span>
        <a href="#" class="footer-link" @click.prevent="openLegalModal('contacto')">Contacto</a>
      </div>
    </div>
    
    <LegalModal 
      :isOpen="isLegalModalOpen" 
      :section="currentSection"
      @close="isLegalModalOpen = false"
    />
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import LegalModal from './LegalModal.vue'

const isLegalModalOpen = ref(false)
const currentSection = ref('')

const openLegalModal = (section) => {
  currentSection.value = section
  isLegalModalOpen.value = true
}
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

/* Responsive design */
@media (max-width: 600px) {
  .footer-content {
    flex-direction: column;
    text-align: center;
    gap: var(--wf-spacing-sm);
  }
}
</style>
