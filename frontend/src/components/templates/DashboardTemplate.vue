<template>
  <div class="dashboard-template">
    <header class="dashboard-header">
      <button class="custom-button back-button" @click="goBack">
        ← Volver
      </button>
      <h1 class="dashboard-title">{{ title }}</h1>
      <div class="header-spacer"></div>
    </header>

    <main class="dashboard-body">
      <slot />
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

defineProps({
  title: {
    type: String,
    required: true
  }
})

const router = useRouter()

const goBack = () => {
  router.push('/')
}
</script>

<style scoped>
.custom-button {
  background: var(--color-red);
  color: var(--color-white);
  border: none;
  border-radius: var(--wf-radius);
  padding: 8px 16px;
  cursor: pointer;
  font-weight: bold;
}

.dashboard-template {
  max-width: 900px;
  margin: 0 auto;
  padding: var(--wf-spacing-md);
  animation: fadeIn 0.4s ease-out;
}

.dashboard-header {
  display: flex;
  align-items: center;
  gap: var(--wf-spacing-md);
  margin-bottom: var(--wf-spacing-lg);
  border-bottom: 5px solid var(--color-red);
  padding-bottom: var(--wf-spacing-md);
}

.dashboard-title {
  flex: 1;
  text-align: center;
  font-size: 1.5rem;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin: 0;
  color: var(--color-yellow);
}

.header-spacer {
  width: 80px;
}

.dashboard-body {
  display: flex;
  flex-direction: column;
  gap: var(--wf-spacing-lg);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 600px) {
  .dashboard-header {
    flex-direction: column;
    align-items: stretch;
  }
  .header-spacer {
    display: none;
  }
  .dashboard-title {
    font-size: 1.2rem;
  }
}
</style>
