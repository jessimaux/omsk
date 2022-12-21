<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Проекты</h1>
    </div>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div v-if="!projectsStore.loading" class="card">
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
                      <router-link :to="{ name: 'project-create' }"><button class="btn btn-primary"><i
                            class="bi bi-plus-square"></i>Добавить</button></router-link>
                    </div>
                  </div>
                </div>
              </div>
              <!-- Default Table -->
              <div v-if="!projectsStore.loading" class="table-responsive">
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
                      <th scope="col">№ счета</th>
                      <th scope="col">Статус проекта</th>
                      <th scope="col">Контрагент</th>
                      <th scope="col">Компания</th>
                      <th scope="col">Общая сумма счета</th>
                      <th scope="col">Отгружено на сумму</th>
                      <th scope="col">Товары</th>
                      <th scope="col">Срок поставки</th>
                      <th scope="col">Комментарии</th>
                      <th scope="col">Наличие договора</th>
                      <th scope="col">Операция</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in projectsStore.data.results" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.purchase.bill }}</td>
                      <td>{{ item.status }}</td>
                      <td>{{ item.partner.name }}</td>
                      <td>{{ item.company_name }}</td>
                      <td>{{ totalBill(item.purchase.purchases) }}</td>
                      <td>{{ deliveryBill(item.purchase.purchases) }}</td>
                      <td>{{ getProducts(item.purchase.purchases) }}</td>
                      <td><input type="date" class="form-control" v-model="item.delivery_date" @change="onChangeDeliveryDateUpdate(item.id, item.delivery_date)"></td>
                      <td>{{ item.commentary }}</td>
                      <td><input type="checkbox" class="form-check-input" v-model="item.contract" @change="onChangeContractUpdate(item.id, item.contract)"></td>
                      <td>
                        <div class="d-flex flex-row">
                          <router-link class="btn btn-primary me-2"
                            :to="{ name: 'project-purchase', params: { id: item.id } }">
                            <i class="bi bi-bag"></i>
                          </router-link>

                          <button type="button" class="btn btn-primary me-2"
                            @click="onClickExportRegistrationForm(item.id)"><i
                              class="bi bi-layout-text-window-reverse"></i></button>

                          <router-link class="btn btn-primary me-2"
                            :to="{ name: 'project-edit', params: { id: item.id } }">
                            <i class="bi bi-pencil-square"></i>
                          </router-link>

                          <button type="button" class="btn btn-primary"><i class="bi bi-x-square"
                              @click="onClickProjectDelete(item.id)"></i></button>
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
import { useProjectsStore } from '@/stores/projects.js'
export default {
  name: 'Projects',
  setup() {
    const projectsStore = useProjectsStore()
    return { projectsStore }
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
      this.projectsStore.getProjects(1, this.ordering, this.search)
    },

    resetSearch(){
      this.search = ''
      this.$router.push({ path: this.$route.fullPath, query: { page: 1, ordering: this.ordering, search: this.search } })
      this.projectsStore.getProjects(1, this.ordering, this.search)
    },

    onOrderingChanged(field) {
      this.ordering = this.ordering === field ? '-' + field : field
      this.$router.push({ path: this.$route.fullPath, query: { page: this.currentPage, ordering: this.ordering, search: this.search } })
      this.projectsStore.getProjects(this.currentPage, this.ordering, this.search)
    },

    onPageChanged(page) {
      this.currentPage = page
      this.$router.push({ path: this.$route.fullPath, query: { page: page, ordering: this.ordering, search: this.search } })
      this.projectsStore.getProjects(page, this.ordering, this.search)
    },

    totalBill(purchases){
      let total = 0
      purchases.forEach(item => total+=item.offer.price)
      return total
    },

    deliveryBill(purchases){
      let total = 0
      purchases.forEach(item => {
        if(item.status === 'Отгружен') total+=item.offer.price
      })
      return total
    },

    getProducts(purchases){
      let products = ''
      let max_products = purchases.length > 3 ? 3 : purchases.length
      for(let i = 0; i < max_products; i++) products += purchases[i].offer.request.name + ';'
      return products
    },

    onChangeDeliveryDateUpdate(id, value){
      this.projectsStore.patchProject(id, { delivery_date: value })
    },

    onChangeContractUpdate(id, value){
      this.projectsStore.patchProject(id, { contract: value })
    },

    onClickProjectDelete(id) {
      this.projectsStore.deleteProject(id)
        .then(() => {
          this.projectsStore.getProjects()
        })
    },

    onClickExportRegistrationForm(id) {
      this.projectsStore.exportRegistrationForm(id)
    }
  },
  created() {
    this.projectsStore.getProjects()
  }
}
</script>