<template>
  <main id="main" class="main">
    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <product-form :initialValues="initialValues" @productSubmit="onSubmit"></product-form>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { useGuideStore } from '@/stores/guide'

import ProductForm from '@/components/Guide/ProductForm.vue'

export default {
  name: 'ProductsCreate',
  components: {
    ProductForm,
  },
  setup() {
    const guideStore = useGuideStore()
    return { guideStore }
  },
  data() {
    return {
      initialValues: {
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
    onSubmit(productFormInput) {
      this.guideStore
        .addProduct(productFormInput)
        .then(() => {
          this.$router.push({ name: 'guide-products' })
        })
    }
  }

}
</script>