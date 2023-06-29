<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Логи действий</h1>
    </div>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <!-- Default Table -->
              <div v-if="!logsStore.loading" class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col" @click="onOrderingChanged('id')">
                        #
                        <i v-if="ordering == 'id'" class="bi bi-sort-up-alt"></i>
                        <i v-if="ordering == '-id'" class="bi bi-sort-down"></i>
                      </th>
                      <th scope="col" @click="onOrderingChanged('created_at')">
                        Время
                        <i v-if="ordering == 'created_at'" class="bi bi-sort-up-alt"></i>
                        <i v-if="ordering == '-created_at'" class="bi bi-sort-down"></i>
                      </th>
                      <th scope="col">Тип объекта</th>
                      <th scope="col">ID объекта</th>
                      <th scope="col">Действие</th>
                      <th scope="col">Инициатор</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in logsStore.data.results" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.created_at }}</td>
                      <td>{{ item.object_type }}</td>
                      <td>{{ item.object_id }}</td>
                      <td>{{ item.action }}</td>
                      <td>{{ item.created_by }}</td>
                    </tr>
                  </tbody>
                </table>
                <pagination v-if="logsStore.data.count > perPage" :currentPage="currentPage" :perPage="perPage"
                  :total="logsStore.data.count" @pageChanged="onPageChanged"></pagination>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { useLogsStore } from '@/stores/logs.js'
import Pagination from '@/components/Pagination.vue'

export default {
  name: 'Logs',
  components: {
    Pagination
  },
  setup() {
    const logsStore = useLogsStore()
    return { logsStore }
  },
  data() {
    return {
      search: this.$route.query.search ? this.$route.query.search : '',
      ordering: this.$route.query.ordering ? this.$route.query.ordering : '-id',
      currentPage: Number(this.$route.query.page) ? Number(this.$route.query.page) : 1,
      perPage: 25
    }
  },
  methods: {
    onSearch() {
      this.$router.push({ path: this.$route.fullPath, query: { page: 1, ordering: this.ordering, search: this.search } })
      this.logsStore.getLogs(1, this.ordering, this.search)
    },

    resetSearch() {
      this.search = ''
      this.$router.push({ path: this.$route.fullPath, query: { page: 1, ordering: this.ordering, search: this.search } })
      this.logsStore.getLogs(1, this.ordering, this.search)
    },

    onOrderingChanged(field) {
      this.ordering = this.ordering === field ? '-' + field : field
      this.$router.push({ path: this.$route.fullPath, query: { page: this.currentPage, ordering: this.ordering, search: this.search } })
      this.logsStore.getLogs(this.currentPage, this.ordering, this.search)
    },

    onPageChanged(page) {
      this.currentPage = page
      this.$router.push({ path: this.$route.fullPath, query: { page: page, ordering: this.ordering, search: this.search } })
      this.logsStore.getLogs(page, this.ordering, this.search)
    },
  },
  created() {
    this.logsStore.getLogs()
  }
}
</script>