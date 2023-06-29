<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Продукт</h1>
    </div>

    <section class="section">
      <form v-if="!guideProductsStore.loading" @submit.prevent="onSubmit">
        <product-form v-if="guideProductsStore.data" :product="guideProductsStore.data"></product-form>
        <div class="text-end mb-3">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>
    </section>
  </main>
</template>

<script>
import { useGuideProductsStore } from '@/stores/guideProducts'
import ProductForm from '@/components/guide/ProductForm.vue'

export default {
  name: 'ProductEdit',
  components: {
    ProductForm,
  },
  setup() {
    const guideProductsStore = useGuideProductsStore()
    return { guideProductsStore }
  },

  methods: {
    onSubmit() {
      const id = this.$route.params.id
      this.guideProductsStore
        .editProduct(id, this.guideProductsStore.data)
        .then(() => {
          this.$router.push({ name: 'guide-products' })
        })
    }
  },

  created() {
    const id = this.$route.params.id
    this.guideProductsStore.getProduct(id)
    .then(() => {
        if (this.guideProductsStore.status === 404) this.$router.push({ name: '404' })
      })
  },

}
</script>