<template>
  <CreateStoryTemplate title="EDITAR HISTORIA">
    <template #form>
      <EditStoryForm :storyId="Number($route.params.id)" />
    </template>
  </CreateStoryTemplate>
</template>

<script setup>
import { useRoute } from 'vue-router'
import CreateStoryTemplate from '../components/templates/CreateStoryTemplate.vue'
import EditStoryForm from '../components/organisms/EditStoryForm.vue'

const route = useRoute()
</script>
