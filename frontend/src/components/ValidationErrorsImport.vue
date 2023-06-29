<template>
    <div class="alert alert-danger alert-dismissible fade show" role="alert">
      <i class="bi bi-exclamation-octagon me-1"></i>
      {{ validationErrors.non_field_errors }}
      <ul v-if="validationErrors.details">
        <li v-for="errorRow in validationErrors.details" :key="errorRow">Ошибка в строке {{ errorRow[0] }}</li>
      </ul>
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
</template>

<script>
export default {
  name: 'ValidationErrors',
  props: {
    validationErrors: {
      type: Object,
      required: true
    },
  },
}
</script>