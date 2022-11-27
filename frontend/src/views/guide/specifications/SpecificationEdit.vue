<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Спецификация</h1>
    </div>

    <section class="section">
      <form v-if="!guideSpecificationsStore.loading" @submit.prevent="onSubmit">
        <div class="row">
          <div class="col-lg-6">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Общее</h5>
                <div class="col-12">
                  <label class="form-label">Название спецификации</label>
                  <input type="text" class="form-control" v-model="specification.name" />
                </div>
              </div>
            </div>
          </div>
        </div>

        <specification :requestOffer="requestOffer" :deleteRequests="deleteRequests" :deleteOffers="deleteOffers"></specification>

        <div class="text-end mb-3">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>
    </section>
  </main>
</template>

<script>
import { useGuideSpecificationsStore } from '@/stores/guideSpecifications'
import Specification from '@/components/specifications/Specification.vue'


export default {
  name: 'SpecificationEdit',
  components: {
    Specification,
  },

  setup() {
    const guideSpecificationsStore = useGuideSpecificationsStore()
    return { guideSpecificationsStore }
  },

  data() {
    return {
      deleteRequests: [],
      deleteOffers: []
    }
  },

  computed: {
    specification() {
      return {
        name: this.guideSpecificationsStore.data.name
      }
    },
    requestOffer(){
      return this.guideSpecificationsStore.data.requestOffer
    }
  },

  methods: {
    onSubmit() {
      this.guideSpecificationsStore.editSpecification(this.specification, this.requestOffer, this.deleteRequests, this.deleteOffers)
        // .then(() => {
        //   this.$router.push({ name: 'guide-specifications' })
        // })
    }
  },

  created() {
    const id = this.$route.params.id
    this.guideSpecificationsStore.getSpecification(id)
  },

}
</script>