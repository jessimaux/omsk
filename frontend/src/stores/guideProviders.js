import { defineStore } from 'pinia'
import guideApi from '@/api/guide'

export const useGuideProvidersStore = defineStore('guideProviders', {
  state: () => {
    return {
      data: null,
      errors: null,
    }
  },

  actions:{
    async getProviders() {
      this.data = null
      this.errors = null
      await guideApi
        .getProviders()
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },
  }
})