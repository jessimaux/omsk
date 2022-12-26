<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Продукт</h1>
    </div>

    <section class="section">
      <form v-if="!guideProductsStore.loading" @submit.prevent="onSubmit">
        <validation-errors v-if="guideProductsStore.errors" :validationErrors="guideProductsStore.errors"></validation-errors>
        <product-form :product="product"></product-form>
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
import ValidationErrors from '@/components/ValidationErrors.vue'

export default {
  name: 'ProductEdit',
  components: {
    ProductForm,
    ValidationErrors
  },
  setup() {
    const guideProductsStore = useGuideProductsStore()
    return { guideProductsStore }
  },
  computed: {
    product() {
      return {
        str_by_order: this.guideProductsStore.data.str_by_order,
        article: this.guideProductsStore.data.article,
        name: this.guideProductsStore.data.name,
        price_rrc: this.guideProductsStore.data.price_rrc,
        price_buy: this.guideProductsStore.data.price_buy,
        link: this.guideProductsStore.data.link,
        country: this.guideProductsStore.data.country,
        description: this.guideProductsStore.data.description,
        description_tech: this.guideProductsStore.data.description_tech,
        description_add: this.guideProductsStore.data.description_add,
        recommendation: this.guideProductsStore.data.recommendation,
        provider: this.guideProductsStore.data.provider,
        nds: this.guideProductsStore.data.nds,
        available: this.guideProductsStore.data.available
      }
    }
  },

  methods: {
    onSubmit() {
      const id = this.$route.params.id
      this.guideProductsStore
        .editProduct(id, this.product)
        .then(() => {
          this.$router.push({ name: 'guide-products' })
        })
    }
  },

  created() {
    const id = this.$route.params.id
    this.guideProductsStore.getProduct(id)
  },

}
</script>