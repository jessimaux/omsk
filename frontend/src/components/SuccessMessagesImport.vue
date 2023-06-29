<template>
  <div class="alert alert-success alert-dismissible fade show" role="alert">
    <i class="bi bi-exclamation-octagon me-1"></i>
    {{ successMessages.message }}
    <ul v-if="successMessages.details">
      <li>Добавлено: {{ successMessages.details.new }};</li>
      <li>Изменено: {{ successMessages.details.update }};</li>
      <li>Удалено: {{ successMessages.details.delete }}.</li>
    </ul>
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
</template>

<script>
export default {
name: 'SuccessMessages',
props: {
  successMessages: {
    type: Object,
    required: true
  },
},
}
</script>