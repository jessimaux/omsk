import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import projectsApi from '@/api/projects'

export const useProjectsStore = defineStore('projects', {
  state: () => {
    return {
      data: null,
      errors: null
    }
  },

  getters: {
    getData(state) {
      return state.data
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

    async addFullProject(credentials) {
      this.errors = null
      this.data = null
      await projectsApi
        .addProject(credentials.project)
        .then(async (response) => {
          await projectsApi
            .addSpecification({ project: response.data.id })
            .then(async (response) => {
              for (const request of credentials.requestOffer) {
                await projectsApi
                  .addRequest({
                    str_by_order: request.str_by_order,
                    name: request.name,
                    tx: request.tx,
                    amount: request.amount,
                    price: request.price,
                    specification: response.data.id,
                  })
                  .then(async (response) => {
                    for (const offer in request.offer) {
                      projectsApi
                        .addOffer({
                          article: offer.article,
                          name: offer.name,
                          count: offer.count,
                          price: offer.price,
                          available: offer.available,
                          request: response.data.id
                        })
                    }
                  })
              }
            })
        })
    }
  }
})
