<template>
  <div v-for="successMessage in successMessages" :key="successMessage" class="alert alert-success alert-dismissible fade show" role="alert">
    <i class="bi bi-exclamation-octagon me-1"></i>
    {{ successMessage }}
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
computed: {
  successMessages() {
    return Object.keys(this.successMessages).map(name => {
      const messages = this.successMessages[name]
      return `${messages}`
    })
  }
}
}
</script>