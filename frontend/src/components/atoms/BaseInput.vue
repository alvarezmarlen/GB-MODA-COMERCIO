<template>
  <input
    :type="type"
    :placeholder="placeholder"
    class="wireframe-input"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  />
</template>

<script setup>
defineProps({
  modelValue: String,
  type: {
    type: String,
    default: 'text'
  },
  placeholder: String
})
defineEmits(['update:modelValue'])
</script>

<style scoped>
.wireframe-input {
  border: 1px solid var(--color-primary);
  border-radius: var(--wf-radius);
  transition: border-color 0.2s ease;
}

.wireframe-input:focus {
  border-color: var(--color-red);
  outline: none;
}
</style>
