<template>
  <textarea
    class="wireframe-input"
    :placeholder="placeholder"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
    rows="6"
  ></textarea>
</template>

<script setup>
defineProps({
  modelValue: String,
  placeholder: String
})
defineEmits(['update:modelValue'])
</script>

<style scoped>
textarea.wireframe-input {
  resize: vertical;
  min-height: 120px;
}
</style>
