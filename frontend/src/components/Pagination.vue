<template>
  <div class="d-flex justify-content-center">
    <ul class="pagination">
      <li class="page-item">
        <a class="page-link" href="#" @click.prevent="pageChanged(1)">В начало</a>
      </li>

      <li class="page-item">
        <a class="page-link" href="#" @click.prevent="pageChanged(currentPage - 1)">Предыдущее</a>
      </li>

      <li class="page-item">
        <a class="page-link" href="#" @click.prevent="pageChanged(currentPage + 1)">Следующее</a>
      </li>

      <li class="page-item">
        <a class="page-link" href="#" @click.prevent="pageChanged(Math.ceil(total / perPage))">В
          конец</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    currentPage: {
      type: Number,
      default: 1
    },
    perPage: {
      type: Number,
      default: 50
    },
    total: {
      type: Number,
      default: 0
    },
  },
  methods: {
    pageChanged(page) {
      if (page < 1) page = 1
      else if (page > Math.ceil(this.total / this.perPage)) page = Math.ceil(this.total / this.perPage)
      this.$emit('pageChanged', page)
    }
  }
}
</script>