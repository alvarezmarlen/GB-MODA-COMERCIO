<template>
  <div class="create-story-template">
    <div class="template-inner">
      <header class="template-header">
        <h1 class="template-title">CREAR HISTORIA</h1>
      </header>
      <main class="template-content">
        <slot name="form"></slot>
      </main>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.create-story-template {
  position: relative;
  min-height: 100vh;
  width: 100%;
  overflow: hidden; /* Prevent horizontal scroll from absolute elements if any */
}

.template-inner {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
  padding-top: 100px; /* Adjusted padding for desktop */
}

/* Side images */
.create-story-template::before,
.create-story-template::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 120px; /* Made it slightly wider to show more of the image */
  background-repeat: repeat-y;
  background-position: top center;
  background-size: cover; /* Changed to cover */
  opacity: 0.96;
  pointer-events: none;
  z-index: 0; /* Changed from -1 so they are visible over body background, but still behind content */
}

.create-story-template::before {
  left: 0;
  background-image: url('../../assets/1.png');
}

.create-story-template::after {
  right: 0;
  background-image: url('../../assets/2.png');
}

/* Ensure inner content is above the pseudo-elements */
.template-inner {
  position: relative;
  z-index: 1;
}

@media (max-width: 1100px) {
  .create-story-template::before,
  .create-story-template::after {
    opacity: 0.3; /* Fade out on smaller screens when overlapping starts */
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
    padding-top: 140px; /* More padding for mobile due to wrapped navbar */
  }
}
</style>
