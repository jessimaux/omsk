import { defineStore } from 'pinia'
import projectsApi from '@/api/projects'
import guideSpecificationsApi from '@/api/guideSpecifications'

export const useGuideSpecificationsStore = defineStore('guideSpecifications', {
  state: () => {
    return {
      data: null,
      errors: null,
      loading: false,
    }
  },

  actions: {
    async getSpecifications(page, field, search) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideSpecificationsApi.getSpecifications(page, field, search)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async getSpecification(id) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideSpecificationsApi.getSpecification(id)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async addSpecification(credentials) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideSpecificationsApi.addSpecification(credentials)
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

    async editSpecification(id, credentials) {
      this.data = null
      this.errors = null
      this.loading = true
      await guideSpecificationsApi.editSpecification(id, credentials)
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

    async deleteSpecification(id) {
      this.data = null
      this.errors = null
      await guideSpecificationsApi.deleteSpecification(id)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },
  }
})