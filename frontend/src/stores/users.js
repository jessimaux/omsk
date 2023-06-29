import { defineStore } from 'pinia'

import usersApi from '@/api/users'

export const useUsersStore = defineStore('users', {
  state: () => {
    return {
      data: null,
      loading: true,
      errors: null,
      status: null,
    }
  },

  actions:{
    async getUsers(page, field, search) {
      this.data = null
      this.errors = null
      this.loading = true
      await usersApi.getUsers(page, field, search)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async getUser(id) {
      this.data = null
      this.errors = null
      this.loading = true
      this.status = null
      await usersApi.getUser(id)
        .then((response) => {
          this.data = response.data
          this.status = response.status
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.status = result.response.status
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
          throw result.response.data
        })
    },

    async editUser(id, credentials) {
      this.data = null
      this.errors = null
      this.loading = true
      await usersApi.editUser(id, credentials)
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

    async deleteUser(id) {
      this.data = null
      this.errors = null
      this.loading = true
      await usersApi.deleteUser(id)
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
  }
})