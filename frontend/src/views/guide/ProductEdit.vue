<template>
  <main id="main" class="main">
    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <product-form v-if="initialValues" :initialValues="initialValues" @productSubmit="onSubmit"></product-form>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { useGuideStore } from '@/stores/guide'

import ProductForm from '@/components/Guide/ProductForm.vue'

export default {
  name: 'ProductEdit',
  components: {
    ProductForm,
  },
  setup() {
    const guideStore = useGuideStore()
    return { guideStore }
  },
  computed: {
    initialValues() {
      if (!this.guideStore.data) {
        return null
      }
      return {
        str_by_order: this.guideStore.data.str_by_order,
        article: this.guideStore.data.article,
        name: this.guideStore.data.name,
        price_rrc: this.guideStore.data.price_rrc,
        price_buy: this.guideStore.data.price_buy,
        link: this.guideStore.data.link,
        country: this.guideStore.data.country,
        description: this.guideStore.data.description,
        description_tech: this.guideStore.data.description_tech,
        description_add: this.guideStore.data.description_add,
        recommendation: this.guideStore.data.recommendation,
        provider: this.guideStore.data.provider,
        nds: this.guideStore.data.nds,
        available: this.guideStore.data.available
      }
    }
  },

  methods: {
    onSubmit(productFormInput) {
      const id = this.$route.params.id
      this.guideStore
        .editProduct(id, productFormInput)
        .then(() => {
          this.$router.push({ name: 'guide-products' })
        })
    }
  },

  created() {
    const id = this.$route.params.id
    this.guideStore.getProduct(id)
  },

}
</script>