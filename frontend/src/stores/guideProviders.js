import { defineStore } from 'pinia'
import guideProvidersApi from '@/api/guideProviders'

export const useGuideProvidersStore = defineStore('guideProviders', {
  state: () => {
    return {
      data: null,
      errors: null,
      loading: false,
    }
  },

  actions: {
    async getProviders(page, field, search) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideProvidersApi.getProviders(page, field, search)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async getProvider(id) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideProvidersApi.getProvider(id)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async addProvider(credentials) {
      this.data = null
      this.errors = null
      await guideProvidersApi.addProvider(credentials)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
        })
    },

    async editProvider(id, credentials) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideProvidersApi.editProvider(id, credentials)
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

    async deleteProvider(id) {
      this.data = null
      this.errors = null
      await guideProvidersApi.deleteProvider(id)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },

    // TODO: add then/catch
    async exportProviders() {
      await guideProvidersApi.exportProviders().then((response) => {
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
    async importProviders(file) {
      await guideProvidersApi.importProviders(file)
    },
  }
})