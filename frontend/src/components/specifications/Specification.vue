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
              <td :rowspan="row.offers.length">
                <i @click="addRow(requestOffer)" class="bi bi-plus-square"></i>
                <i v-show="requestOffer.length > 1" @click="removeRow(index, requestOffer)"
                  class="bi bi-dash-square"></i>
              </td>
              <td :rowspan="row.offers.length">{{ index }}</td>
              <td :rowspan="row.offers.length"><input type="text" v-model="row.str_by_order" /></td>
              <td :rowspan="row.offers.length"><input type="text" v-model="row.name" /></td>
              <td :rowspan="row.offers.length"><input type="text" v-model="row.tx" /></td>
              <td :rowspan="row.offers.length"><input type="text" v-model="row.amount" /></td>
              <td :rowspan="row.offers.length"><input type="text" v-model="row.price" /></td>
              <td :rowspan="row.offers.length">{{ row.price * row.amount }}</td>
              <td>
                <product-search-field :row="row.offers[0]" v-model="row.offers[0].article"></product-search-field>
              </td>
              <td>
                <product-search-field :row="row.offers[0]" v-model="row.offers[0].name"></product-search-field>
              </td>
              <td><input type="text" v-model="row.offers[0].count" /></td>
              <td>{{ row.offers[0].product ? row.offers[0].product.price_buy : '' }}</td>
              <td>{{ row.offers[0].product && row.offers[0].count ? row.offers[0].count * row.offers[0].product.price_buy : '' }}</td>
              <td>{{ row.offers[0].product ? row.offers[0].product.available : '' }}</td>
              <td>
                <i @click="addSubRow(row.offers)" class="bi bi-plus-square"></i>
                <i v-show="row.offers.length > 1" @click="removeSubRow(0, row.offers)" class="bi bi-dash-square"></i>
              </td>
            </tr>

            <tr v-if="row.offers.length > 1" v-for="(subrow, subindex) in row.offers.slice(1, row.offers.length)"
              :key="`subrow-${subindex}`">
              <td>
                <product-search-field :row="subrow" v-model="subrow.article"></product-search-field>
              </td>
              <td>
                <product-search-field :row="subrow" v-model="subrow.name"></product-search-field>
              </td>
              <td><input type="text" v-model="subrow.count" /></td>
              <td>{{ subrow.product ? subrow.product.price_buy : '' }}</td>
              <td>{{ subrow.product && subrow.count ? subrow.count * subrow.product.price_buy : '' }}</td>
              <td>{{ subrow.product ? subrow.product.available : '' }}</td>
              <td>
                <i @click="addSubRow(row.offers)" class="bi bi-plus-square"></i>
                <i v-show="row.offers.length > 1" @click="removeSubRow(subindex + 1, row.offers)"
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
import ProductSearchField from '@/components/projects/ProductSearchField.vue'

export default {
  name: 'Specification',
  components: {
    ProductSearchField,
  },
  props: {
    requestOffer: {
      type: Object,
      required: true,
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
        offers: [{
          product: '',
          article: '',
          name: '',
          count: '',
        }],
      })
    },

    removeRow(index, fieldType) {
      fieldType.splice(index, 1)
    },

    addSubRow(fieldType) {
      fieldType.push({
        product: '',
        article: '',
        name: '',
        count: '',
      })
    },

    removeSubRow(index, fieldType) {
      fieldType.splice(index, 1)
    },
  },
}
</script>
