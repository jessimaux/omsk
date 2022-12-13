<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Продукты</h1>
    </div>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <div class="row justify-content-between">

                <div class="col-auto search-bar">
                  <form class="search-form d-flex align-items-center" method="GET" @submit.prevent="onSearch">
                    <input type="text" class="form-control" name="search" v-model="search" placeholder="Поиск...">
                    <button v-if="search" type="button" class="btn" @click="resetSearch"><i
                        class="bi bi-x-lg"></i></button>
                  </form>
                </div>

                <div class="col-auto">
                  <div class="row">
                    <div class="col-auto">
                      <router-link class="btn btn-primary me-2" :to="{ name: 'guide-products-create' }">
                        <i class="bi bi-plus-square"></i>&nbspДобавить
                      </router-link>
                    </div>

                    <div class="col-auto">
                      <button class="btn btn-primary me-2" @click="exportProducts">
                        <i class="bi bi-download"></i>&nbspЭкспорт
                      </button>
                    </div>

                    <div class="col-auto">
                      <div class="btn-import">
                        <label for="btn-import" class="btn btn-primary"><i class="bi bi-upload"></i>&nbspИмпорт</label>
                        <input type="file" id="btn-import" @change="importProducts" ref="file" hidden>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div v-if="!guideProductsStore.loading" class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col" @click="onOrderingChanged('id')">
                        #
                        <i v-if="ordering == 'id'" class="bi bi-sort-up-alt"></i>
                        <i v-if="ordering == '-id'" class="bi bi-sort-down"></i>
                      </th>
                      <th scope="col">№</th>
                      <th scope="col">Артикул</th>
                      <th scope="col" @click="onOrderingChanged('name')">
                        Наименование
                        <i v-if="ordering == 'name'" class="bi bi-sort-up-alt"></i>
                        <i v-if="ordering == '-name'" class="bi bi-sort-down"></i>
                      </th>
                      <th scope="col">РРЦ</th>
                      <th scope="col">Закупочная стоимость</th>
                      <th scope="col">Ссылка</th>
                      <th scope="col">Страна происхождения</th>
                      <th scope="col">Описание</th>
                      <th scope="col">ТЗ</th>
                      <th scope="col">Заявка</th>
                      <th scope="col">Рекомендации</th>
                      <th scope="col">Поставщик</th>
                      <th scope="col">НДС</th>
                      <th scope="col">Наличие</th>
                      <th scope="col">Операция</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in guideProductsStore.data.results" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.str_by_order }}</td>
                      <td>{{ item.article }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.price_rrc }}</td>
                      <td>{{ item.price_buy }}</td>
                      <td>{{ item.link }}</td>
                      <td>{{ item.country }}</td>
                      <td>{{ item.description }}</td>
                      <td>{{ item.description_tech }}</td>
                      <td>{{ item.description_add }}</td>
                      <td>{{ item.recommendation }}</td>
                      <td>{{ item.provider }}</td>
                      <td>{{ item.nds }}</td>
                      <td>{{ item.available }}</td>
                      <td>
                        <div class="d-flex flex-row">
                          <button type="button" class="btn btn-primary me-2"><i class="bi bi-x-square"
                              @click="onClickProductDelete(item.id)"></i></button>
                          <router-link class="btn btn-primary"
                            :to="{ name: 'guide-products-edit', params: { id: item.id } }"><i
                              class="bi bi-pencil-square"></i></router-link>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { useGuideProductsStore } from '@/stores/guideProducts.js'

export default {
  name: 'Products',
  setup() {
    const guideProductsStore = useGuideProductsStore()
    return { guideProductsStore }
  },
  data() {
    return {
      file: null,
      search: this.$route.query.search ? this.$route.query.search : '',
      ordering: this.$route.query.ordering ? this.$route.query.ordering : 'id',
      currentPage: Number(this.$route.query.page) ? Number(this.$route.query.page) : 1,
      perPage: 25
    }
  },
  methods: {
    onSearch() {
      this.$router.push({ path: this.$route.fullPath, query: { page: 1, ordering: this.ordering, search: this.search } })
      this.guideProductsStore.getProducts(1, this.ordering, this.search)
    },

    resetSearch() {
      this.search = ''
      this.$router.push({ path: this.$route.fullPath, query: { page: 1, ordering: this.ordering, search: this.search } })
      this.guideProductsStore.getProducts(1, this.ordering, this.search)
    },

    onOrderingChanged(field) {
      this.ordering = this.ordering === field ? '-' + field : field
      this.$router.push({ path: this.$route.fullPath, query: { page: this.currentPage, ordering: this.ordering, search: this.search } })
      this.guideProductsStore.getProducts(this.currentPage, this.ordering, this.search)
    },

    onPageChanged(page) {
      this.currentPage = page
      this.$router.push({ path: this.$route.fullPath, query: { page: page, ordering: this.ordering, search: this.search } })
      this.guideProductsStore.getProducts(page, this.ordering, this.search)
    },

    onClickProductDelete(id) {
      this.guideProductsStore.deleteProduct(id)
        .then(() => {
          this.guideProductsStore.getProducts()
        })
    },

    exportProducts() {
      this.guideProductsStore.exportProducts()
    },

    importProducts() {
      this.file = this.$refs.file.files[0]
      const formData = new FormData()
      formData.append('file', this.file)
      this.guideProductsStore.importProducts(formData)
        .then(() => {
          this.guideProductsStore.getProducts()
        })
      this.$refs.file.value = null;
    }
  },
  created() {
    this.guideProductsStore.getProducts()
  }
}
</script>