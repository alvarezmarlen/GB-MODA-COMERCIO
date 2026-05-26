<template>
  <div class="create-story-template">
    <header class="template-header">
      <h1 class="template-title">CREAR HISTORIA</h1>
    </header>
    <main class="template-content">
      <slot name="form"></slot>
    </main>
  </div>
</template>

<script setup>
</script>

<style scoped>
.create-story-template {
  max-width: 800px;
  margin: 0 auto;
}

.template-header {
  text-align: center;
  margin-bottom: var(--wf-spacing-lg);
  border-bottom: 5px solid var(--color-red);
  padding-bottom: var(--wf-spacing-sm);
}

h1.template-title {
  font-size: 1.5rem;
  letter-spacing: 2px;
  color: var(--color-yellow);
}

.template-content {
  margin-top: var(--wf-spacing-lg);
}
</style>
