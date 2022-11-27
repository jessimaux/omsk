import { defineStore } from 'pinia'
import projectsApi from '@/api/projects'
import guideSpecificationsApi from '@/api/guideSpecifications'

export const useGuideSpecificationsStore = defineStore('guideSpecifications', {
  state: () => {
    return {
      specification: null,
      data: null,
      errors: null,
      loading: false,
    }
  },

  actions: {
    async getSpecifications() {
      this.data = null
      this.errors = null
      await guideSpecificationsApi.getSpecifications()
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },

    async getSpecification(id) {
      this.data = null
      this.specification = null
      this.errors = null
      this.loading = true
      await guideSpecificationsApi.getSpecification(id)
        .then((response) => {
          this.data = response.data
          this.specification = response.data.id
          this.loading = false
        })
        .catch((result) => {
          this.errors = result.response.data
          this.loading = false
        })
    },

    async addSpecification(credentials) {
      this.data = null
      this.specification = null
      this.errors = null

      credentials.guide = true
      
      await guideSpecificationsApi.addSpecification(credentials)
        .then((response) => {
          this.specification = response.data.id
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
          throw result.response.data
        })
    },

    async editSpecification(credentialsSpecification, credentialsRequestOffer, deleteRequests, deleteOffers) {
      this.errors = null
      this.loading = true
      await guideSpecificationsApi.editSpecification(this.specification, credentialsSpecification)
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

    async deleteSpecification(id) {
      this.data = null
      this.errors = null
      await guideSpecificationsApi.deleteSpecification(id)
        .then((response) => {
          this.data = response.data
        })
        .catch((result) => {
          this.errors = result.response.data
        })
    },

    async addRequestOffer(credentials) {
      this.errors = null
      this.data = null
      for (const request of credentials) {
        await projectsApi.addRequest({
          str_by_order: request.str_by_order,
          name: request.name,
          tx: request.tx,
          amount: request.amount,
          price: request.price,
          specification: this.specification.id,
        })
          .then(async (response) => {
            for (const offer of request.offer) {
              await projectsApi.addOffer({
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