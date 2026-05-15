<template>
  <div id="app">
    <LoginPage v-if="currentPage === 'login'" @switch="currentPage = $event" />
    <RegisterPage v-else @switch="currentPage = $event" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LoginPage from './views/LoginPage.vue'
import RegisterPage from './views/RegisterPage.vue'

const currentPage = ref('login')
</script>

<style>
@import './style.css';
</style>
