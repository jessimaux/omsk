<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Спецификация</h1>
    </div>

    <section class="section">
      <form @submit.prevent="onSubmit">
        <div class="row">
          <div class="col-lg-6">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Общее</h5>
                <div class="col-12">
                  <label class="form-label">Название спецификации</label>
                  <input type="text" class="form-control" v-model="specification.name" />
                </div>

                <div class="col-12">
                  <label class="form-label">Описание спецификации</label>
                  <textarea class="form-control" style="resize:none" rows="5" v-model="specification.description" />
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
  name: 'SpecificationCreate',
  components: {
    Specification,
  },
  setup() {
    const guideSpecificationsStore = useGuideSpecificationsStore()
    return { guideSpecificationsStore }
  },
  data() {
    return {
      specification: {
        name: '',
        description: '',
        guide: true,
        requests: [
        {
          str_by_order: '',
          name: '',
          tx: '',
          amount: '',
          price: '',
          offers: [{
            article: '',
            name: '',
            price: '',
            count: '',
          }],
        },
      ],
      },
    }
  },

  methods: {
    onSubmit() {
      this.guideSpecificationsStore.addSpecification(this.specification)
      .then(()=>{
        this.$router.push({ name: 'guide-specifications' })
      })
    }
  }
}
</script>