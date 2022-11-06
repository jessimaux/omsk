import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import authApi from '@/api/auth'
import { setItem } from '@/tools/persistanceStorage'

export const useAuthStore = defineStore('auth', {
  state: () => {
    return {
      isLoading: false,
      currentUser: {},
      errors: null,
    }
  },

  getters: {
    getIsLoading() {
      return this.isLoading
    }
  },

  actions: {
    async getCurrentUser() {
      this.isLoading = true
      await authApi
        .getCurrentUser()
        .then((response) => {
          this.isLoading = false
          this.currentUser = response.data
        })
        .catch((result) => {
          this.isLoading = false
          this.currentUser = null
        })
    },

    async login(credentials) {
      this.errors = null
      await authApi
        .login(credentials)
        .then((response) => {
          this.getCurrentUser()
          setItem('accessToken', response.data.auth_token)
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },

    async logout(context) {
      await authApi
        .logout()
        .then(() => {
          this.currentUser = {}
        })
      localStorage.removeItem('accessToken')
    },
  }
})
