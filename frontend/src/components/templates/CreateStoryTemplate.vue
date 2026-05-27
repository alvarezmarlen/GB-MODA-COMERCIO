<template>
  <div class="create-story-template">
    <div class="template-inner">
      <header class="template-header">
        <h1 class="template-title">{{ t('createStory.pageTitle') }}</h1>
      </header>
      <main class="template-content">
        <slot name="form"></slot>
      </main>
    </div>
  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>

<style scoped>
.create-story-template {
  position: relative;
  min-height: 100vh;
  width: 100%;
  overflow: hidden;
}

.template-inner {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
  padding-top: 100px;
}

.create-story-template::before,
.create-story-template::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 120px;
  background-repeat: repeat-y;
  background-position: top center;
  background-size: cover;
  opacity: 0.96;
  pointer-events: none;
  z-index: 0;
}

.create-story-template::before {
  left: 0;
  background-image: url('../../assets/1.png');
}

.create-story-template::after {
  right: 0;
  background-image: url('../../assets/2.png');
}

.template-inner {
  position: relative;
  z-index: 1;
}

@media (max-width: 1100px) {
  .create-story-template::before,
  .create-story-template::after {
    opacity: 0.3;
  }
}

@media (max-width: 900px) {
  .create-story-template::before,
  .create-story-template::after {
    display: none;
  }
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

@media (max-width: 680px) {
  .create-story-template {
    padding-top: 140px;
  }
}
</style>
