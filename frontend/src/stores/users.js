import { defineStore } from 'pinia'

import usersApi from '@/api/users'

export const useUsersStore = defineStore('users', {
  state: () => {
    return {
      data: null,
      loading: true,
      errors: null
    }
  },

  actions:{
    async getUsers() {
      this.data = null
      this.errors = null
      this.loading = true
      await usersApi.getUsers()
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async createUser(credentials) {
      this.data = null
      this.errors = null
      this.loading = true
      await usersApi.createUser(credentials)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },
  }
})