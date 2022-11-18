import { defineStore } from 'pinia'
import guideApi from '@/api/guide'

export const useGuideSpecificationsStore = defineStore('guideSpecifications', {
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
    async getSpecifications() {
      this.data = null
      this.errors = null
      await guideApi
        .getSpecifications()
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },
  } 
})