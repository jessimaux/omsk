import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import projectsApi from '@/api/projects'

export const useProjectsStore = defineStore('projects', {
  state: () => {
    return {
      project: null,
      data: {},
      loading: false,
      errors: null
    }
  },

  actions: {
    async getProjects(page, field, search) {
      this.errors = null
      this.data = null
      this.loading = true
      await projectsApi.getProjects(page, field, search)
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
      this.data = {}
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

    async fileUploadProject(files) {
      this.errors = null
      await projectsApi.fileUploadProject(files)
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
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
          this.project = response.data.id
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

    async patchProject(id, credentials) {
      // this.data = null
      this.errors = null
      this.loading = true
      await projectsApi.patchProject(id, credentials)
        .then((response) => {
          // this.data = response.data
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