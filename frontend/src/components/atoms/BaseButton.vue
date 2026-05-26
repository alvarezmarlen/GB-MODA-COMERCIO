<template>
  <button 
    class="wireframe-button" 
    :disabled="disabled"
    @click="$emit('click')"
  >
    <slot />
  </button>
</template>

<script setup>
defineProps({
  disabled: {
    type: Boolean,
    default: false
  }
})
defineEmits(['click'])
</script>

<style scoped>
.wireframe-button {
  border-radius: var(--wf-radius);
  background: var(--color-red);
  color: var(--color-white);
  border: none; /* Remove existing border if any */
}
</style>
