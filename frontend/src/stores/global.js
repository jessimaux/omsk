import { defineStore } from 'pinia'

export const useGlobalStore = defineStore('global', {
  state: () => {
    return {
      showSidebar: true,
      showNavbar: true
    }
  },

  getters: {
    getShowSidebar() {
      return this.showSidebar
    },
    getShowNavbar() {
      return this.showNavbar
    }
  }
})