import { defineStore } from 'pinia'
import guideApi from '@/api/guide'

export const useGuidePartnersStore = defineStore('guidePartners', {
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

  actions: {
    async getPartners() {
      this.data = null
      this.errors = null
      await guideApi
        .getPartners()
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },
  }
})