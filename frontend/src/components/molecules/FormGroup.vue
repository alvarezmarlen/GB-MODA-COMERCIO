<template>
  <div class="form-group">
    <BaseLabel v-if="label">{{ label }}</BaseLabel>
    <slot></slot>
  </div>
</template>

<script setup>
import BaseLabel from '../atoms/BaseLabel.vue'

defineProps({
  label: String
})
</script>

<style scoped>
.form-group {
  margin-bottom: var(--wf-spacing-md);
}
</style>
