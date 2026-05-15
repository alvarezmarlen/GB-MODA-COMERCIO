<template>
  <div class="form-field">
    <BaseLabel>{{ label }}</BaseLabel>
    <BaseInput
      :type="type"
      :placeholder="placeholder"
      :modelValue="modelValue"
      @update:modelValue="$emit('update:modelValue', $event)"
    />
  </div>
</template>

<script setup>
import BaseLabel from '../atoms/BaseLabel.vue'
import BaseInput from '../atoms/BaseInput.vue'

defineProps({
  label: String,
  modelValue: String,
  type: String,
  placeholder: String
})

defineEmits(['update:modelValue'])
</script>

<style scoped>
.form-field {
  margin-bottom: 16px;
}
</style>
