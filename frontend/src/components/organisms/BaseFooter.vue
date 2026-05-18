<template>
  <footer class="base-footer">
    <div class="footer-divider"></div>
    <div class="footer-content">
      <div class="copyright">
        © 2026 GB-MODA-COMERCIO. Todos los derechos reservados.
      </div>
      <div class="footer-links">
        <a href="#" class="footer-link">Términos</a>
        <span class="divider">│</span>
        <a href="#" class="footer-link">Privacidad</a>
        <span class="divider">│</span>
        <a href="#" class="footer-link">Contacto</a>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.base-footer {
  margin-top: var(--wf-spacing-lg);
  padding-bottom: var(--wf-spacing-lg);
  font-family: 'Courier New', Courier, monospace;
}

.footer-divider {
  border-top: 2px solid var(--wf-border);
  margin-bottom: var(--wf-spacing-md);
  width: 100%;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: var(--wf-text);
  gap: var(--wf-spacing-md);
}

.footer-links {
  display: flex;
  align-items: center;
  gap: 8px;
}

.footer-link {
  color: var(--wf-text);
  text-decoration: none;
  border-bottom: 1px dashed transparent;
  transition: all 0.2s ease;
}

.footer-link:hover {
  border-bottom: 1px dashed var(--wf-border);
}

.divider {
  color: var(--wf-placeholder);
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
