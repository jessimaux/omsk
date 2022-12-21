<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Партнеры</h1>
    </div>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div v-if="!guidePartnersStore.loading" class="card">
            <div class="card-body">
              <div class="row justify-content-between">

                <div class="col-auto search-bar">
                    <form class="search-form d-flex align-items-center" method="GET" @submit.prevent="onSearch">
                      <input type="text" class="form-control" name="search" v-model="search" placeholder="Поиск...">
                      <button v-if="search" type="button" class="btn" @click="resetSearch"><i class="bi bi-x-lg"></i></button>
                    </form>
                </div>

                <div class="col-auto">
                  <div class="row">
                    <div class="col-auto">
                      <router-link class="btn btn-primary me-2" :to="{ name: 'guide-partners-create' }">
                        <i class="bi bi-plus-square"></i>&nbspДобавить
                      </router-link>
                    </div>

                    <div class="col-auto">
                      <button class="btn btn-primary me-2" @click="exportPartners">
                        <i class="bi bi-download"></i>&nbspЭкспорт
                      </button>
                    </div>

                    <div class="col-auto">
                      <div class="btn-import">
                        <label for="btn-import" class="btn btn-primary"><i class="bi bi-upload"></i>&nbspИмпорт</label>
                        <input type="file" id="btn-import" @change="importPartners" ref="file" hidden>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="table-responsive">
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
                      <th scope="col">ИНН</th>
                      <th scope="col">Регион</th>
                      <th scope="col">Базовая скидка</th>
                      <th scope="col">Операция</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in guidePartnersStore.data.results" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.inn }}</td>
                      <td>{{ item.region }}</td>
                      <td>{{ item.discount }}</td>
                      <td>
                        <div class="d-flex flex-row">
                          <router-link class="btn btn-primary me-2"
                            :to="{ name: 'guide-partners-edit', params: { id: item.id } }">
                            <i class="bi bi-pencil-square"></i>
                          </router-link>

                          <button type="button" class="btn btn-primary" @click="onClickPartnerDelete(item.id)">
                            <i class="bi bi-x-square"></i>
                          </button>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <pagination v-if="guidePartnersStore.data.count > perPage" :currentPage="currentPage" :perPage="perPage"
                :total="guidePartnersStore.data.count" @pageChanged="onPageChanged"></pagination>

            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { useGuidePartnersStore } from '@/stores/guidePartners.js'
import Pagination from '@/components/Pagination.vue'

export default {
  name: 'Partners',
  components: {
    Pagination
  },
  setup() {
    const guidePartnersStore = useGuidePartnersStore()
    return { guidePartnersStore }
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
      this.guidePartnersStore.getPartners(1, this.ordering, this.search)
    },

    resetSearch(){
      this.search = ''
      this.$router.push({ path: this.$route.fullPath, query: { page: 1, ordering: this.ordering, search: this.search } })
      this.guidePartnersStore.getPartners(1, this.ordering, this.search)
    },

    onOrderingChanged(field) {
      this.ordering = this.ordering === field ? '-' + field : field
      this.$router.push({ path: this.$route.fullPath, query: { page: this.currentPage, ordering: this.ordering, search: this.search } })
      this.guidePartnersStore.getPartners(this.currentPage, this.ordering, this.search)
    },

    onPageChanged(page) {
      this.currentPage = page
      this.$router.push({ path: this.$route.fullPath, query: { page: page, ordering: this.ordering, search: this.search } })
      this.guidePartnersStore.getPartners(page, this.ordering, this.search)
    },

    onClickPartnerDelete(id) {
      this.guidePartnersStore.deletePartner(id)
        .then(() => {
          this.guidePartnersStore.getPartners()
        })
    },

    exportPartners() {
      this.guidePartnersStore.exportPartners()
    },

    importPartners() {
      this.file = this.$refs.file.files[0]
      const formData = new FormData()
      formData.append('file', this.file)
      this.guidePartnersStore.importPartners(formData)
        .then(() => {
          this.guidePartnersStore.getPartners()
        })
      this.$refs.file.value = null;
    }
  },
  created() {
    this.guidePartnersStore.getPartners()
  }
}
</script>