<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Общее</h5>
          <div class="col-12">
            <label class="form-label">Название проекта</label>
            <input type="text" class="form-control" v-model="project.name" />
          </div>

          <div class="col-12">
            <label class="form-label">Статус проекта</label>
            <select class="form-select" v-model="project.status">
              <option v-for="attribute in statusSelect" :value="attribute">
                {{ attribute }}
              </option>
            </select>
          </div>

          <div class="col-12">
            <label class="form-label">Партнер</label>
            <select class="form-select" v-model="project.partner">
              <option v-for="partner in guidePartnersStore.data" :key="partner.id" :value="partner.id">
                {{ partner.name }}
              </option>
            </select>
          </div>

          <div class="col-12">
            <label class="form-label">Номер регистрации проекта</label>
            <input type="text" class="form-control" v-model="project.reg_no" />
          </div>

          <div class="col-12">
            <label class="form-label">Скидка</label>
            <input type="text" class="form-control" :value="getDiscount" disabled />
          </div>

          <div class="col-12">
            <label class="col-form-label">НДС</label>
            <div class="form-check">
              <input type="checkbox" class="form-check-input" v-model="project.nds" />
            </div>
          </div>
        </div>
      </div>
    </div>


    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">О заказчике</h5>
          <div class="col-12">
            <label class="form-label">Наименование</label>
            <input type="text" class="form-control" v-model="project.company_name" />
          </div>

          <div class="col-12">
            <label class="form-label">ИНН</label>
            <input type="text" class="form-control" v-model="project.company_inn" />
          </div>

          <div class="col-12">
            <label class="form-label">Город</label>
            <input type="text" class="form-control" v-model="project.company_city" />
          </div>

          <div class="col-12">
            <label class="form-label">Область</label>
            <input type="text" class="form-control" v-model="project.company_region" />
          </div>

          <div class="col-12">
            <label class="form-label">Количество детей в классе</label>
            <input type="text" class="form-control" v-model="project.company_children" />
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Комментарий</h5>
          <textarea class="form-control" style="resize:none" rows="5" v-model="project.commentary"></textarea>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useGuidePartnersStore } from '@/stores/guidePartners'

export default {
  name: 'projectForm',

  props: {
    project: {
      type: Object,
      required: true,
    },
  },

  setup() {
    const guidePartnersStore = useGuidePartnersStore()
    return { guidePartnersStore }
  },

  data() {
    return {
      statusSelect: ['В работе', 'На согласовании', 'Согласована спека', 'Выдали ТЗ', 'Разместили аукцион', 'Закуп', 'Доставка', 'Оплатили', 'Закрыт', 'Не состоялся'],
    }
  },

  computed: {
    getDiscount() {
      if (typeof this.project.partner === 'number' && this.guidePartnersStore.data) {
        for (const object of this.guidePartnersStore.data) {
          if (object.id === this.project.partner) return object.discount
        }
      }
    },
  },

  methods: {
  },

  created() {
    this.guidePartnersStore.getPartners()
  },
}
</script>
