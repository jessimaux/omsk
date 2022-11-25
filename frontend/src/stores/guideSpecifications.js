import { defineStore } from 'pinia'
import guideSpecificationsApi from '@/api/guideSpecifications'

export const useGuideSpecificationsStore = defineStore('guideSpecifications', {
  state: () => {
    return {
      data: null,
      errors: null,
    }
  },

  actions:{
    async getSpecifications() {
      this.data = null
      this.errors = null
      await guideSpecificationsApi.getSpecifications()
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },
  } 
})