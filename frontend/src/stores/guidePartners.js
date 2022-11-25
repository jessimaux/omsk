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
    async getPartners() {
      this.data = null
      this.errors = null
      this.loading = true
      await guidePartnersApi.getPartners()
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
  }
})