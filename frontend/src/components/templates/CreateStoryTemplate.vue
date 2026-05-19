<template>
  <div class="create-story-template">
    <header class="template-header">
      <h1>CREAR HISTORIA</h1>
    </header>
    <main class="template-content">
      <div class="wireframe-container">
        <slot name="form"></slot>
      </div>
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
  border-bottom: 2px solid var(--wf-border);
  padding-bottom: var(--wf-spacing-sm);
}

h1 {
  font-size: 1.5rem;
  letter-spacing: 2px;
}

.template-content {
  margin-top: var(--wf-spacing-lg);
}
</style>
