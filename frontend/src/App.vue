<template>
  <div id="app" class="app-layout">
    <!-- Reusable Navbar: only shown for authenticated screens -->
    <BaseNavbar v-if="showNavAndFooter" />
    
    <!-- Main router view -->
    <main class="app-main-content">
      <router-view />
    </main>

    <!-- Reusable Footer: only shown for authenticated screens -->
    <BaseFooter v-if="showNavAndFooter" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import BaseNavbar from './components/organisms/BaseNavbar.vue'
import BaseFooter from './components/organisms/BaseFooter.vue'

const route = useRoute()
const showNavAndFooter = computed(() => {
  // Nav and Footer are excluded on login and register screens
  return route.name && route.name !== 'login' && route.name !== 'register'
})
</script>

<style>
@import './style.css';

.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  max-width: 1000px;
  margin: 0 auto;
  padding: var(--wf-spacing-md);
}

.app-main-content {
  flex: 1 0 auto;
}
</style>
