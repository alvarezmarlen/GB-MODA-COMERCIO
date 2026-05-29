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

    <!-- Legal Modal -->
    <LegalModal :isOpen="legalModalOpen" :section="legalModalSection" @close="legalModalOpen = false" />
  </div>
</template>

<script setup>
import { computed, ref, provide } from 'vue'
import { useRoute } from 'vue-router'
import BaseNavbar from './components/organisms/BaseNavbar.vue'
import BaseFooter from './components/organisms/BaseFooter.vue'
import LegalModal from './components/organisms/LegalModal.vue'

const route = useRoute()
const showNavAndFooter = computed(() => {
  // Nav and Footer are excluded on login and register screens
  return route.name && route.name !== 'login' && route.name !== 'register'
})

const legalModalOpen = ref(false)
const legalModalSection = ref('')
const openLegalModal = (section) => {
  legalModalSection.value = section
  legalModalOpen.value = true
}
provide('openLegalModal', openLegalModal)
</script>

<style>
@import './style.css';

.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100%;
  background-color: #2D6A8B;
  /* sin padding para que el fondo llegue a los bordes */
}

.app-main-content {
  flex: 1 0 auto;
  padding-top: 80px; /* espacio para el nav fijo flotante */
}
</style>
