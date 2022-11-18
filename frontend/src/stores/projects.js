import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import projectsApi from '@/api/projects'

export const useProjectsStore = defineStore('projects', {
  state: () => {
    return {
      data: null,
      project: null,
      specification: null,
      loading: false,
      errors: null
    }
  },

  getters: {
    getData(state) {
      return state.data
    },
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
      this.errors = null
      this.data = null
      this.loading = true
      await projectsApi
        .getProject(id)
        .then((response) => {
          this.loading = false
          this.data = response.data
        })
        .catch((result) => {
          this.loading = false
          this.errors = result.response.data
          throw result.response.data
        })
    },

    async addProject(credentials) {
      this.errors = null
      this.data = null
      this.project = null
      await projectsApi
        .addProject(credentials)
        .then((response) => {
          this.data = response.data
          this.project = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
        })
    },

    async addSpecification() {
      this.errors = null
      this.data = null
      this.specification = null
      await projectsApi
        .addSpecification({project: this.project.id})
        .then((response) => {
          this.data = response.data
          this.specification = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
        })
    },

    async addRequestOffer(credentials) {
      this.errors = null
      this.data = null
      for (const request of credentials) {
        await projectsApi
          .addRequest({
            str_by_order: request.str_by_order,
            name: request.name,
            tx: request.tx,
            amount: request.amount,
            price: request.price,
            specification: this.specification.id,
          })
          .then(async (response) => {
            for (const offer of request.offer) {
              await projectsApi
                .addOffer({
                  article: offer.article,
                  name: offer.name,
                  count: offer.count,
                  price: offer.price,
                  available: offer.available,
                  request: response.data.id
                })
                .catch((result) => {
                  this.errors = result.response.data
                })
            }
          })
          .catch((result) => {
            this.errors = result.response.data
          })
      }
    },
  }
})