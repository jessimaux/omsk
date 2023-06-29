import { defineStore } from 'pinia'

import usersApi from '@/api/logs'

export const useLogsStore = defineStore('logs', {
  state: () => {
    return {
      data: null,
      loading: true,
      errors: null,
      status: null,
    }
  },

  actions:{
    async getLogs(page, field, search) {
      this.data = null
      this.errors = null
      this.loading = true
      await usersApi.getLogs(page, field, search)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    }
  }
})