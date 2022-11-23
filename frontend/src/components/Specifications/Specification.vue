<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Спецификация</h5>
      <div class="table-responsive mb-3">
        <table class="table">
          <thead>
            <tr>
              <th scope="col" colspan="8" class="text-center">Запрос</th>
              <th scope="col" colspan="7" class="text-center">Предложение</th>
            </tr>
            <tr>
              <th scope="col"></th>
              <th scope="col">#</th>
              <th scope="col">Приказ</th>
              <th scope="col">Наименование</th>
              <th scope="col">ТХ</th>
              <th scope="col">Количество</th>
              <th scope="col">Цена</th>
              <th scope="col">Сумма</th>
              <th scope="col">Артикул</th>
              <th scope="col">Наименование</th>
              <th scope="col">Количество</th>
              <th scope="col">Цена</th>
              <th scope="col">Сумма</th>
              <th scope="col">Наличие</th>
              <th scope="col"></th>
            </tr>
          </thead>

          <tbody v-for="(row, index) in requestOffer" :key="`row-${index}`">
            <tr>
              <td :rowspan="row.offer.length">
                <i @click="addRow(requestOffer)" class="bi bi-plus-square"></i>
                <i v-show="requestOffer.length > 1" @click="removeRow(index, requestOffer)"
                  class="bi bi-dash-square"></i>
              </td>
              <td :rowspan="row.offer.length">{{ index }}</td>
              <td :rowspan="row.offer.length"><input type="text" v-model="row.str_by_order" /></td>
              <td :rowspan="row.offer.length"><input type="text" v-model="row.name" /></td>
              <td :rowspan="row.offer.length"><input type="text" v-model="row.tx" /></td>
              <td :rowspan="row.offer.length"><input type="text" v-model="row.amount" /></td>
              <td :rowspan="row.offer.length"><input type="text" v-model="row.price" /></td>
              <td :rowspan="row.offer.length">{{ row.price * row.amount }}</td>
              <td>
                <product-search-field :row="row.offer[0]" v-model="row.offer[0].article"></product-search-field>
              </td>
              <td>
                <product-search-field :row="row.offer[0]" v-model="row.offer[0].name"></product-search-field>
              </td>
              <td><input type="text" v-model="row.offer[0].count" /></td>
              <td>{{ row.offer[0].price }}</td>
              <td>{{ row.offer[0].count * row.offer[0].price }}</td>
              <td>{{ row.offer[0].available }}</td>
              <td>
                <i @click="addSubRow(row.offer)" class="bi bi-plus-square"></i>
                <i v-show="row.offer.length > 1" @click="removeSubRow(0, row.offer)" class="bi bi-dash-square"></i>
              </td>
            </tr>

            <tr v-if="row.offer.length > 1" v-for="(subrow, subindex) in row.offer.slice(1, row.offer.length)"
              :key="`subrow-${subindex}`">
              <td>
                <product-search-field :row="subrow" v-model="subrow.article"></product-search-field>
              </td>
              <td>
                <product-search-field :row="subrow" v-model="subrow.name"></product-search-field>
              </td>
              <td><input type="text" v-model="subrow.count" /></td>
              <td>{{ subrow.price }}</td>
              <td>{{ subrow.count * subrow.price }}</td>
              <td>{{ subrow.available }}</td>
              <td>
                <i @click="addSubRow(row.offer)" class="bi bi-plus-square"></i>
                <i v-show="row.offer.length > 1" @click="removeSubRow(subindex + 1, row.offer)"
                  class="bi bi-dash-square"></i>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { useProjectsStore } from '@/stores/projects'
import ProductSearchField from '@/components/Projects/ProductSearchField.vue'

export default {
  name: 'Specification',
  components: {
    ProductSearchField,
  },
  props: {
    requestOffer: {
      type: Object,
      required: true,
    },
    deleteRequests:{
      type: Object,
      required: false
    },
    deleteOffers: {
      type: Object,
      required: false
    }
  },
  setup() {
    const projectsStore = useProjectsStore()
    return { projectsStore }
  },

  methods: {
    addRow(fieldType) {
      fieldType.push({
        str_by_order: '',
        name: '',
        tx: '',
        amount: '',
        price: '',
        offer: [{
          product: '',
          article: '',
          name: '',
          count: '',
          price: '0',
          available: '0',
        }],
      })
    },

    removeRow(index, fieldType) {
      if(this.deleteRequests && 'id' in fieldType[index]){
        this.deleteRequests.push(fieldType[index].id)
      }
      fieldType.splice(index, 1)
    },

    addSubRow(fieldType) {
      fieldType.push({
        product: '',
        article: '',
        name: '',
        count: '',
        price: '0',
        available: '0',
      })
    },

    removeSubRow(index, fieldType) {
      if(this.deleteOffers && 'id' in fieldType[index]){
        this.deleteOffers.push(fieldType[index].id)
      }
      fieldType.splice(index, 1)
    },
  },
}
</script>
