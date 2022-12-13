import { defineStore } from 'pinia'

import purchaseApi from '@/api/purchase'

export const usePurchasesStore = defineStore('purchases', {
  state: () => {
    return {
      data: null,
      loading: true,
      errors: null
    }
  },

  actions:{
    async getPurchase(id) {
      this.data = null
      this.errors = null
      this.loading = true
      await purchaseApi.getPurchase(id)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async editPurchase(id, credentials) {
      this.data = null
      this.errors = null
      this.loading = true
      await purchaseApi.editPurchase(id, credentials)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
          throw result.response.data
        })
    },
  }
})