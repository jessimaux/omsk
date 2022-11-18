import { defineStore } from 'pinia'
import guideApi from '@/api/guide'

export const useGuideProductsStore = defineStore('guideProducts', {
  state: () => {
    return {
      data: null,
      errors: null,
    }
  },

  getters: {
    getData(state) {
      return state.data
    },
  },

  actions:{
    async getProducts(query=null) {
      this.data = null
      this.errors = null
      await guideApi
        .getProducts(query)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },

    // TODO: add then/catch
    async exportProducts() {
      await guideApi.exportProducts().then((response) => {
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
      await guideApi.importProducts(file)
    },

    async getProduct(id) {
      this.data = null
      this.errors = null
      await guideApi
        .getProduct(id)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },

    async addProduct(credentials) {
      this.data = null
      this.errors = null
      await guideApi
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
      await guideApi
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
      await guideApi
        .deleteProduct(id)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },
  }
})