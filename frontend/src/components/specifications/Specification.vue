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

          <tbody v-for="(row, index) in specification.requests" :key="`row-${index}`">
            <tr>
              <td :rowspan="row.offers.length">
                <i @click="addRow(specification.requests)" class="bi bi-plus-square"></i>
                <i v-show="specification.requests.length > 1" @click="removeRow(index, specification.requests)"
                  class="bi bi-dash-square"></i>
              </td>
              <td :rowspan="row.offers.length">{{ index }}</td>
              <td :rowspan="row.offers.length"><input type="text" v-model="row.str_by_order" required /></td>
              <td :rowspan="row.offers.length"><input type="text" v-model="row.name" required /></td>
              <td :rowspan="row.offers.length"><input type="text" v-model="row.tx" /></td>
              <td :rowspan="row.offers.length"><input type="number" min="0" v-model="row.amount" required /></td>
              <td :rowspan="row.offers.length"><input type="number" min="0" step="any" v-model="row.price" required /></td>
              <td :rowspan="row.offers.length">{{ row.price * row.amount }}</td>
              <td>
                <product-search-field :row="row.offers[0]" v-model="row.offers[0].article"></product-search-field>
              </td>
              <td>
                <product-search-field :row="row.offers[0]" v-model="row.offers[0].name"></product-search-field>
              </td>
              <td><input type="number" min="0" v-model="row.offers[0].count" required /></td>
              <td><input type="number" min="0" step="any" v-model="row.offers[0].price" required /></td>
              <td>{{ row.offers[0].count ? row.offers[0].count * row.offers[0].price : '' }}</td>
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
              <td><input type="number" min="0" v-model="subrow.count" /></td>
              <td><input type="number" min="0" step="any" v-model="subrow.price" /></td>
              <td>{{ subrow.count ? subrow.count * subrow.price : '' }}</td>
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

  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Спецификация - Итог</h5>
          <div class="row">
            <div class="col-lg-6 label ">Итого(Запросы):</div>
            <div class="col-lg-6">{{ totalRequest }}</div>
          </div>

          <div class="row">
            <div class="col-lg-6 label ">Итого(Предложения):</div>
            <div class="col-lg-6">{{ totalOffers }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductSearchField from '@/components/projects/ProductSearchField.vue'

export default {
  name: 'Specification',
  components: {
    ProductSearchField,
  },
  props: {
    specification: {
      type: Object,
      required: true,
    }
  },
  computed: {
    totalRequest() {
      let total = 0
      this.specification.requests.forEach(request => {
        if (request.price && request.amount) total += Number(request.price*request.amount)
      })
      return total
    },

    totalOffers() {
      let total = 0
      this.specification.requests.forEach(request => {
        request.offers.forEach(offer => {
          if (offer.price && offer.count) total += Number(offer.price*offer.count)
        })
      })
      return total
    }
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
          article: '',
          name: '',
          price: '',
          count: '',
        }],
      })
    },

    removeRow(index, fieldType) {
      fieldType.splice(index, 1)
    },

    addSubRow(fieldType) {
      fieldType.push({
        article: '',
        name: '',
        price: '',
        count: '',
      })
    },

    removeSubRow(index, fieldType) {
      fieldType.splice(index, 1)
    },
  },
}
</script>
