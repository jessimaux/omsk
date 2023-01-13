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

    async exportPurchases(id) {
      await purchaseApi.exportPurchases(id)
        .then((response) => {
          const blob = new Blob([response.data], { type: response.data.type })
          const url = window.URL.createObjectURL(blob)
          const link = document.createElement('a')
          link.href = url
          const contentDisposition = response.headers['content-disposition']
          if (contentDisposition) {
            const fileNameMatch = contentDisposition.match(/filename="(.+)"/)
            if (fileNameMatch.length === 2) var fileName = fileNameMatch[1]
          }
          link.setAttribute('download', fileName)
          document.body.appendChild(link)
          link.click()
          link.remove()
          window.URL.revokeObjectURL(url)
        })
    },
  }
})