<template>
  <CreateStoryTemplate>
    <template #form>
      <CreateStoryForm />
    </template>
  </CreateStoryTemplate>
</template>

<script setup>
import CreateStoryTemplate from '../components/templates/CreateStoryTemplate.vue'
import CreateStoryForm from '../components/organisms/CreateStoryForm.vue'
</script>
