<template>
  <div class="auth-template">
    <div class="auth-card">
      <header class="auth-header">
        <h1 class="auth-title">{{ title }}</h1>
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
  position: relative;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: var(--color-primary);
}

.auth-template::before,
.auth-template::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  width: 70px;
  background-repeat: repeat-y;
  background-position: top center;
  background-size: 70px auto;
  opacity: 0.96;
  pointer-events: none;
  z-index: 0;
}

.auth-template::before {
  left: 0;
  background-image: url('../../assets/1.png');
}

.auth-template::after {
  right: 0;
  background-image: url('../../assets/2.png');
}

@media (max-width: 900px) {
  .auth-template::before,
  .auth-template::after {
    display: none;
  }
}

.auth-card {
  position: relative;
  z-index: 1;
  width: calc(100% - 32px);
  max-width: 400px;
  padding: 40px;
  background-color: var(--color-white);
  border: 2px solid var(--color-red);
  border-radius: 20px;
}

@media (max-width: 480px) {
  .auth-card {
    padding: 24px 20px;
    width: calc(100% - 24px);
  }

  .auth-title {
    font-size: 20px;
  }
}

.auth-header {
  margin-bottom: 24px;
  text-align: center;
}

.auth-title {
  font-size: 24px;
  text-transform: uppercase;
  color: var(--color-primary);
}

.auth-footer {
  margin-top: 16px;
  text-align: center;
  font-size: 14px;
}
</style>
