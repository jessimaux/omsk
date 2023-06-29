import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import authApi from '@/api/auth'
import { setCookie, eraseCookie } from '@/tools/persistanceStorage'

export const useAuthStore = defineStore('auth', {
  state: () => {
    return {
      data: null,
      isLoading: false,
      currentUser: {},
      refreshTokenTimeout: 0,
      errors: {}
    }
  },

  actions: {
    async getCurrentUser() {
      this.errors = null
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
          this.errors = result.response.data
        })
    },

    async login(user) {
      this.currentUser = null
      this.errors = null
      this.isLoading = true
      await authApi
        .login(user)
        .then(async (response) => {
          localStorage.setItem('refresh', response.data.refresh)
          setCookie('access', response.data.access, 1000 * 60 * 15)
          await this.getCurrentUser()
          this.isLoading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.isLoading = false
          throw result.response.data
        })
      this.startRefreshTokenTimer()
    },

    async logout() {
      this.currentUser = null
      localStorage.removeItem('refresh')
      eraseCookie('access')
      this.stopRefreshTokenTimer()
    },

    async refreshToken() {
      this.errors = null
      this.isLoading = true
      const refreshToken = localStorage.getItem('refresh')
      if(refreshToken === null || refreshToken === '') throw new Error('Not refresh token');
      await authApi
        .refresh(refreshToken)
        .then(async (response) => {
          setCookie('access', response.data.access, 1000 * 60 * 15)
          this.isLoading = false
        })
        .catch((result) => {
          localStorage.removeItem('refresh')
          eraseCookie('access')
          this.errors = result.response.data
          this.isLoading = false
          throw result.response.data
        })
      this.startRefreshTokenTimer()
    },

    startRefreshTokenTimer() {
      // set a timeout to refresh the token a minute before it expires
      this.refreshTokenTimeout = setTimeout(this.refreshToken, 14 * 1000 * 60)
    },

    stopRefreshTokenTimer() {
      clearTimeout(this.refreshTokenTimeout)
    },

    async registration(email, username, password) {
      this.errors = null
      this.isLoading = true
      await authApi
        .registration(email, username, password)
        .then(() => {
          this.isLoading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.isLoading = false
          throw result.response.data
        })
    }
  }
})
