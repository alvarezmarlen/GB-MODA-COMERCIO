<template>
  <div class="auth-template">
    <div class="wireframe-container auth-card">
      <header class="auth-header">
        <h1>{{ title }}</h1>
      </header>
      <main class="auth-content">
        <slot />
      </main>
      <footer class="auth-footer">
        <slot name="footer" />
      </footer>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: String
})
</script>

<style scoped>
.auth-template {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f9f9f9;
}

.auth-card {
  width: 100%;
  max-width: 400px;
}

.auth-header {
  margin-bottom: 24px;
  text-align: center;
}

.auth-header h1 {
  font-size: 24px;
  text-transform: uppercase;
}

.auth-footer {
  margin-top: 16px;
  text-align: center;
  font-size: 14px;
}
</style>
