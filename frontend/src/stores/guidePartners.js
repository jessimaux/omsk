import { defineStore } from 'pinia'
import guidePartnersApi from '@/api/guidePartners'

export const useGuidePartnersStore = defineStore('guidePartners', {
  state: () => {
    return {
      data: null,
      errors: null,
      loading: false,
    }
  },

  actions: {
    async getPartners(page, field) {
      this.data = null
      this.errors = null
      this.loading = true
      await guidePartnersApi.getPartners(page, field)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async getPartner(id) {
      this.data = null
      this.errors = null
      this.loading = true
      await guidePartnersApi.getPartner(id)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async addPartner(credentials) {
      this.data = null
      this.errors = null
      await guidePartnersApi.addPartner(credentials)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
        })
    },

    async editPartner(id, credentials) {
      this.data = null
      this.errors = null
      await guidePartnersApi.editPartner(id, credentials)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
        })
    },

    async deletePartner(id) {
      this.data = null
      this.errors = null
      await guidePartnersApi.deletePartner(id)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },

    // TODO: add then/catch
    async exportPartners() {
      await guidePartnersApi.exportPartners().then((response) => {
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
    async importPartners(file) {
      await guidePartnersApi.importPartners(file)
    },
  }
})