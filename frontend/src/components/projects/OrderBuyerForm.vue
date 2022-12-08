<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Формирование заказа покупателя</h5>
          <form @submit.prevent="onSubmit">
            <div class="col-12">
              <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-model="params.str_by_order">
                <label class="form-check-label" for="flexSwitchCheckDefault">Включить номер по приказу</label>
              </div>
              <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" v-model="params.link">
                <label class="form-check-label" for="flexSwitchCheckChecked">Включить ссылку на товар</label>
              </div>
              <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckDisabled" v-model="params.country">
                <label class="form-check-label" for="flexSwitchCheckDisabled">Включить страну происхождения</label>
              </div>
              <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckCheckedDisabled"
                  v-model="params.description">
                <label class="form-check-label" for="flexSwitchCheckCheckedDisabled">Включить описание</label>
              </div>
              <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckCheckedDisabled"
                  v-model="params.description_tech">
                <label class="form-check-label" for="flexSwitchCheckCheckedDisabled">Включить техническое
                  задание</label>
              </div>
              <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckCheckedDisabled"
                  v-model="params.description_add">
                <label class="form-check-label" for="flexSwitchCheckCheckedDisabled">Включить заявку</label>
              </div>
              <div class="text-end mt-3">
                <button type="submit" class="btn btn-primary">Сформировать</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import { useProjectsStore } from '@/stores/projects'

export default {
  name: 'OrderBuyerForm',
  props:{
    specification_id: {
      type: Number,
      required: true,
    },
  },
  setup() {
    const projectsStore = useProjectsStore()
    return { projectsStore }
  },
  data() {
    return {
      params: {
        str_by_order: false,
        link: false,
        country: false,
        description: false,
        description_tech: false,
        description_add: false
      }
    }
  },
  methods: {
    onSubmit() {
      this.projectsStore.exportSpecification(this.specification_id, this.params)
    }
  }
}
</script>