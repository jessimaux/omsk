<template>
  <div class="autocomplete">
    <input type="text" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"
      @keyup="searchProducts" @blur="fieldUnfocus" />
    <div v-if="state" class="autocomplete__result">
      <div class="list-group">
        <button v-for="(product, index) in guideProductsStore.data" :key="product.id" type="button"
          class="list-group-item list-group-item-action" @click="setProduct(index)">
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
      if (this.row.article) {
        this.state = true
        this.guideProductsStore.getProducts(this.row.article)
      }
      else this.state = false
    },

    fieldUnfocus() {
      setTimeout(() => this.state = false, 100)
    },

    setProduct(index) {
      this.row.product = this.guideProductsStore.data[index].id
      this.row.article = this.guideProductsStore.data[index].article
      this.row.name = this.guideProductsStore.data[index].name
      this.row.price = this.guideProductsStore.data[index].price_rrc
      this.row.available = this.guideProductsStore.data[index].available
    }
  }
};
</script>