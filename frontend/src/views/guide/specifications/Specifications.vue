<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Спецификации</h1>
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
                  <router-link class="btn btn-primary me-2" :to="{ name: 'guide-specifications-create' }">
                    <i class="bi bi-plus-square"></i>&nbspДобавить
                  </router-link>
                </div>
              </div>

              <div v-if="!guideSpecificationsStore.loading" class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col" @click="onOrderingChanged('id')">
                        #
                        <i v-if="ordering == 'id'" class="bi bi-sort-up-alt"></i>
                        <i v-if="ordering == '-id'" class="bi bi-sort-down"></i>
                      </th>
                      <th scope="col" @click="onOrderingChanged('name')">
                        Наименование
                        <i v-if="ordering == 'name'" class="bi bi-sort-up-alt"></i>
                        <i v-if="ordering == '-name'" class="bi bi-sort-down"></i>
                      </th>
                      <th scope="col">Описание</th>
                      <th scope="col">Операция</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in guideSpecificationsStore.data.results" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.description }}</td>
                      <td>
                        <div class="d-flex flex-row">
                          <router-link class="btn btn-primary me-2"
                            :to="{ name: 'guide-specifications-edit', params: { id: item.id } }"><i
                              class="bi bi-pencil-square"></i></router-link>

                          <button type="button" class="btn btn-primary"><i class="bi bi-x-square"
                              @click="onClickSpecificationDelete(item.id)"></i></button>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <pagination v-if="guideSpecificationsStore.data.count > perPage" :currentPage="currentPage"
                  :perPage="perPage" :total="guideSpecificationsStore.data.count" @pageChanged="onPageChanged">
                </pagination>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { useGuideSpecificationsStore } from '@/stores/guideSpecifications.js'
import Pagination from '@/components/Pagination.vue'

export default {
  name: 'Specifications',
  components: {
    Pagination
  },
  setup() {
    const guideSpecificationsStore = useGuideSpecificationsStore()
    return { guideSpecificationsStore }
  },
  data() {
    return {
      search: this.$route.query.search ? this.$route.query.search : '',
      ordering: this.$route.query.ordering ? this.$route.query.ordering : 'id',
      currentPage: Number(this.$route.query.page) ? Number(this.$route.query.page) : 1,
      perPage: 25
    }
  },
  methods: {
    onSearch() {
      this.$router.push({ path: this.$route.fullPath, query: { page: 1, ordering: this.ordering, search: this.search } })
      this.guideSpecificationsStore.getSpecifications(1, this.ordering, this.search)
    },

    resetSearch() {
      this.search = ''
      this.$router.push({ path: this.$route.fullPath, query: { page: 1, ordering: this.ordering, search: this.search } })
      this.guideSpecificationsStore.getSpecifications(1, this.ordering, this.search)
    },

    onOrderingChanged(field) {
      this.ordering = this.ordering === field ? '-' + field : field
      this.$router.push({ path: this.$route.fullPath, query: { page: this.currentPage, ordering: this.ordering, search: this.search } })
      this.guideSpecificationsStore.getSpecifications(this.currentPage, this.ordering, this.search)
    },

    onPageChanged(page) {
      this.currentPage = page
      this.$router.push({ path: this.$route.fullPath, query: { page: page, ordering: this.ordering, search: this.search } })
      this.guideSpecificationsStore.getSpecifications(page, this.ordering, this.search)
    },

    onClickSpecificationDelete(id) {
      this.guideSpecificationsStore.deleteSpecification(id)
        .then(() => {
          this.guideSpecificationsStore.getSpecifications()
        })
    },
  },
  created() {
    this.guideSpecificationsStore.getSpecifications()
  }
}
</script>