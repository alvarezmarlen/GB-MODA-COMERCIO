<template>
  <select
    class="wireframe-input"
    :value="modelValue"
    @change="$emit('update:modelValue', $event.target.value)"
  >
    <option disabled value="">{{ placeholder }}</option>
    <option v-for="option in options" :key="option.value" :value="option.value">
      {{ option.label }}
    </option>
  </select>
</template>

<script setup>
defineProps({
  modelValue: [String, Number],
  options: {
    type: Array,
    required: true
  },
  placeholder: {
    type: String,
    default: 'Seleccionar opción'
  }
})
defineEmits(['update:modelValue'])
</script>

<style scoped>
select.wireframe-input {
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 8px center;
  background-size: 16px;
  padding-right: 32px;
  border: 1px solid var(--color-primary);
  border-radius: var(--wf-radius);
  transition: border-color 0.2s ease;
}

select.wireframe-input:focus {
  border-color: var(--color-red);
  outline: none;
}
</style>
