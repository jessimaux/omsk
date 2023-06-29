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
                  <label class="form-label" name="name">Название спецификации</label>
                  <input type="text" class="form-control" v-model="specification.name" required />
                </div>

                <div class="col-12">
                  <label class="form-label" name="description">Описание спецификации</label>
                  <textarea class="form-control" style="resize:none" rows="5" v-model="specification.description"
                    required />
                </div>
              </div>
            </div>
          </div>
        </div>

        <specification :specification="specification"></specification>

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
    Specification
  },

  setup() {
    const guideSpecificationsStore = useGuideSpecificationsStore()
    return { guideSpecificationsStore }
  },

  computed: {
    specification() {
      return this.guideSpecificationsStore.data
    }
  },

  methods: {
    onSubmit() {
      this.guideSpecificationsStore.editSpecification(this.specification.id, this.specification)
        .then(() => {
          this.$router.push({ name: 'guide-specifications' })
        })
    }
  },

  created() {
    const id = this.$route.params.id
    this.guideSpecificationsStore.getSpecification(id)
      .then(() => {
        if (this.guideSpecificationsStore.status === 404) this.$router.push({ name: '404' })
      })
  },

}
</script>