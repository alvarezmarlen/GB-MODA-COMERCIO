<template>
  <input
    :type="type"
    :placeholder="placeholder"
    :name="name"
    :autocomplete="autocomplete"
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
  placeholder: String,
  name: String,
  autocomplete: String
})
defineEmits(['update:modelValue'])
</script>

<style scoped>
.wireframe-input {
  border: 1px solid var(--color-red);
  border-radius: var(--wf-radius);
}
</style>
