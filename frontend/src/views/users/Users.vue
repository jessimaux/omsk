<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Пользователи</h1>
    </div>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div v-if="!usersStore.loading" class="card">
            <div class="card-body">
              <div class="row justify-content-between">
                <div class="col-auto"></div>
                <div class="col-auto">
                  <div class="row">
                    <div class="col-auto">
                      <router-link class="btn btn-primary me-2" :to="{ name: 'user-create' }">
                        <i class="bi bi-plus-circle"></i>&nbspДобавить
                      </router-link>
                    </div>
                  </div>
                </div>
              </div>

              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Название</th>
                      <th scope="col">Email</th>
                      <th scope="col">Имя</th>
                      <th scope="col">Фамилия</th>
                      <th scope="col">Операция</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in usersStore.data.results" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.username }}</td>
                      <td>{{ item.email }}</td>
                      <td>{{ item.first_name }}</td>
                      <td>{{ item.last_name }}</td>
                      <td>
                        <router-link class="btn btn-primary me-2" title="Редактировать пользователя"
                            :to="{ name: 'user-edit', params: { id: item.id } }">
                            <i class="bi bi-pencil-square"></i>
                          </router-link>

                          <button type="button" class="btn btn-primary" title="Удалить"><i class="bi bi-x-square"
                              @click="onClickUserDelete(item.id)"></i></button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <pagination
              v-if="usersStore.data.count > perPage"
              :currentPage="currentPage"
              :perPage="perPage"
              :total="usersStore.data.count"
              @pageChanged="onPageChanged"></pagination>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { useUsersStore } from '@/stores/users'
import Pagination from '@/components/Pagination.vue'

export default {
  name: 'Users',
  components: {
    Pagination
  },
  setup() {
    const usersStore = useUsersStore()
    return { usersStore }
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
      this.$router.push({
        path: this.$route.fullPath,
        query: { page: 1, ordering: this.ordering, search: this.search }
      })
      this.usersStore.getUsers(1, this.ordering, this.search)
    },

    resetSearch() {
      this.search = ''
      this.$router.push({
        path: this.$route.fullPath,
        query: { page: 1, ordering: this.ordering, search: this.search }
      })
      this.usersStore.getUsers(1, this.ordering, this.search)
    },

    onOrderingChanged(field) {
      this.ordering = this.ordering === field ? '-' + field : field
      this.$router.push({
        path: this.$route.fullPath,
        query: { page: this.currentPage, ordering: this.ordering, search: this.search }
      })
      this.usersStore.getUsers(this.currentPage, this.ordering, this.search)
    },

    onPageChanged(page) {
      this.currentPage = page
      this.$router.push({
        path: this.$route.fullPath,
        query: { page: page, ordering: this.ordering, search: this.search }
      })
      this.usersStore.getUsers(page, this.ordering, this.search)
    },

    onClickUserDelete(id) {
      this.usersStore.deleteUser(id).then(() => {
        this.usersStore.getUsers()
      })
    }
  },
  created() {
    this.usersStore.getUsers()
  }
}
</script>
