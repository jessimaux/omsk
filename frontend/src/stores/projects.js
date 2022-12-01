import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import projectsApi from '@/api/projects'
import projects from '../api/projects'

export const useProjectsStore = defineStore('projects', {
  state: () => {
    return {
      data: null,
      loading: false,
      errors: null
    }
  },

  actions: {
    async getProjects() {
      this.errors = null
      this.data = null
      await projectsApi
        .getProjects()
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },

    async getProject(id) {
      this.data = null
      this.errors = null
      this.loading = true
      await projectsApi
        .getProject(id)
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async addProject(credentials) {
      this.errors = null
      this.data = null
      this.loading = true
      await projectsApi.addProject(credentials)
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

    async editProject(id, credentials) {
      this.data = null
      this.errors = null
      this.loading = true
      await projectsApi.editProject(id, credentials)
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


    async deleteProject(id) {
      this.errors = null
      this.data = null
      await projectsApi.deleteProject(id)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },
  }
})