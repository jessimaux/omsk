import { defineStore } from 'pinia'
import guideProvidersApi from '@/api/guideProviders'

export const useGuideProvidersStore = defineStore('guideProviders', {
  state: () => {
    return {
      data: null,
      errors: null,
    }
  },

  actions: {
    async getProviders() {
      this.data = null
      this.errors = null
      await guideProvidersApi.getProviders()
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },
  }
})