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
