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
      this.loading = true
      await projectsApi.getProjects()
        .then((response) => {
          this.data = response.data
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
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

    async exportSpecification(id, params) {
      await projectsApi.exportSpecification(id, params)
        .then((response) => {
          const blob = new Blob([response.data], { type: response.data.type })
          const url = window.URL.createObjectURL(blob)
          const link = document.createElement('a')
          link.href = url
          const contentDisposition = response.headers['content-disposition']
          if (contentDisposition) {
            const fileNameMatch = contentDisposition.match(/filename="(.+)"/)
            if (fileNameMatch.length === 2) var fileName = fileNameMatch[1]
          }
          link.setAttribute('download', fileName)
          document.body.appendChild(link)
          link.click()
          link.remove()
          window.URL.revokeObjectURL(url)
        })
    },

    async exportRegistrationForm(id) {
      await projectsApi.exportRegistrationForm(id)
        .then((response) => {
          const blob = new Blob([response.data], { type: response.data.type })
          const url = window.URL.createObjectURL(blob)
          const link = document.createElement('a')
          link.href = url
          const contentDisposition = response.headers['content-disposition']
          if (contentDisposition) {
            const fileNameMatch = contentDisposition.match(/filename="(.+)"/)
            if (fileNameMatch.length === 2) var fileName = fileNameMatch[1]
          }
          link.setAttribute('download', fileName)
          document.body.appendChild(link)
          link.click()
          link.remove()
          window.URL.revokeObjectURL(url)
        })
    },
  }
})