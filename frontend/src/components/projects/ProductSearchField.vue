<template>
  <div class="autocomplete">
    <input type="text" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"
      @keyup="searchProducts" @blur="fieldUnfocus" required />
    <div v-if="state && !guideProductsStore.loading" class="autocomplete_result">
      <div class="list-group">
        <button v-for="(product, index) in guideProductsStore.data.results" type="button"
          class="list-group-item list-group-item-action autocomplete_button" @click="setProduct(index)">
          {{ product.article }} {{ product.name }}
        </button>
      </div>
    </div>
  </div>
</template>
 
<script>
import { useGuideProductsStore } from '@/stores/guideProducts'

export default {
  name: "ProductSearchField",
  props: ['row', 'modelValue'],
  emits: ['update:modelValue'],
  data() {
    return {
      state: false
    }
  },
  setup() {
    const guideProductsStore = useGuideProductsStore()
    return { guideProductsStore }
  },
  methods: {
    searchProducts() {
      if (this.modelValue) {
        this.state = true
        this.row.product = ''
        this.row.product_id = null
        this.guideProductsStore.searchProducts(this.modelValue)
      }
      else this.state = false
    },

    fieldUnfocus() {
      setTimeout(() => this.state = false, 250)
    },

    setProduct(index) {
      this.row.product_id = this.guideProductsStore.data.results[index].id
      this.row.article = this.guideProductsStore.data.results[index].article
      this.row.name = this.guideProductsStore.data.results[index].name
      this.row.price = this.guideProductsStore.data.results[index].price_rrc
      this.row.product = this.guideProductsStore.data.results[index]
    }
  }
};
</script>