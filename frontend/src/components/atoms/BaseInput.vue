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
