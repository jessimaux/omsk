import { defineStore } from 'pinia'
import guideProductsApi from '@/api/guideProducts'

export const useGuideProductsStore = defineStore('guideProducts', {
  state: () => {
    return {
      data: null,
      errors: null,
      loading: false
    }
  },

  actions: {
    async searchProducts(query = null) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideProductsApi.searchProducts(query)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async getProducts(page, field, search) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideProductsApi.getProducts(page, field, search)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async getProduct(id) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideProductsApi.getProduct(id)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async addProduct(credentials) {
      this.data = null
      this.errors = null
      await guideProductsApi
        .addProduct(credentials)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
        })
    },

    async editProduct(id, credentials) {
      this.data = null
      this.errors = null
      await guideProductsApi
        .editProduct(id, credentials)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
        })
    },

    async deleteProduct(id) {
      this.data = null
      this.errors = null
      await guideProductsApi
        .deleteProduct(id)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },

    // TODO: add then/catch
    async exportProducts() {
      await guideProductsApi.exportProducts().then((response) => {
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

    // TODO: add than / catch
    async importProducts(file) {
      await guideProductsApi.importProducts(file)
    },
  }
})