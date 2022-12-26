<template>
    <div v-for="errorMessage in errorMessages" :key="errorMessage" class="alert alert-danger alert-dismissible fade show" role="alert">
      <i class="bi bi-exclamation-octagon me-1"></i>
      {{ errorMessage }}
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
  computed: {
    errorMessages() {
      return Object.keys(this.validationErrors).map(name => {
        const messages = this.validationErrors[name]
        if(name==='non_field_errors') name = ''
        else {
          name = document.getElementsByName(name)[0].textContent + ':'
        }

        return `${name} ${messages}`
      })
    }
  }
}
</script>