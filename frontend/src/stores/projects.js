import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import projectsApi from '@/api/projects'
import projects from '../api/projects'

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
      this.project = null
      this.specification = null
      this.errors = null
      this.loading = true
      await projectsApi
        .getProject(id)
        .then((response) => {
          this.data = response.data
          this.project = response.data.id
          this.specification = response.data.specification.id
          this.loading = false
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

    async editProject(credentialsProject, credentialsRequestOffer, deleteRequests, deleteOffers) {
      this.errors = null
      this.loading = true
      await projectsApi.editProject(this.project, credentialsProject)
        .catch((result) => {
          this.errors = result.response.data
        })

      // add or edit(if exists) requestOffer
      for (const request of credentialsRequestOffer) {
        var request_id = null
        if ('id' in request) {
          request_id = request.id
          await projectsApi.editRequest(request.id, request)
            .catch((result) => {
              this.errors = result.response.data
            })
        }
        else {
          request.specification = this.specification
          await projectsApi.addRequest(request)
            .then((response) => {
              request_id = response.data.id
            })
            .catch((result) => {
              this.errors = result.response.data
            })
        }

        for (const offer of request.offer) {
          if ('id' in offer)
            await projectsApi.editOffer(offer.id, offer)
              .catch((result) => {
                this.errors = result.response.data
              })
          else {
            offer.request = request_id
            await projectsApi.addOffer(offer)
              .catch((result) => {
                this.errors = result.response.data
              })
          }
        }
      }

      // delete exists offers and requests if they have been deleted from table
      for (const offer_id of deleteOffers)
        await projectsApi.deleteOffer(offer_id)
          .catch((result) => {
            this.errors = result.response.data
          })

      for (const request_id of deleteRequests)
        await projectsApi.deleteRequest(request_id)
          .catch((result) => {
            this.errors = result.response.data
          })

      this.loading = false
    },

    async addSpecification() {
      this.errors = null
      this.data = null
      this.specification = null
      await projectsApi
        .addSpecification({ project: this.project.id })
        .then((response) => {
          this.data = response.data
          this.specification = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
        })
    },

    // TODO: rewrite with property add
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
                  product: offer.product,
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