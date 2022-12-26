<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Продукт</h1>
    </div>

    <section class="section">
      <form @submit.prevent="onSubmit">
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
  name: 'ProductsCreate',
  components: {
    ProductForm,
    ValidationErrors,
  },
  setup() {
    const guideProductsStore = useGuideProductsStore()
    return { guideProductsStore }
  },
  data() {
    return {
      product: {
        str_by_order: '',
        article: '',
        name: '',
        price_rrc: '',
        price_buy: '',
        link: '',
        country: '',
        description: '',
        description_tech: '',
        description_add: '',
        recommendation: '',
        provider: '',
        nds: '',
        available: ''
      }
    }
  },

  methods: {
    onSubmit() {
      this.guideProductsStore
        .addProduct(this.product)
        .then(() => {
          this.$router.push({ name: 'guide-products' })
        })
    }
  }

}
</script>