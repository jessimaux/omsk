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

                <div class="col-auto">
                  <div class="row">
                    <div class="col-auto">
                      <router-link class="btn btn-primary me-2" :to="{ name: 'user-create' }">
                        <i class="bi bi-plus-square"></i>&nbspДобавить
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
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in usersStore.data" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.username }}</td>
                      <td>{{ item.email }}</td>
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
import { useUsersStore } from '@/stores/users'

export default {
  name: 'Users',
  setup() {
    const usersStore = useUsersStore()
    return { usersStore }
  },
  methods:{
    deleteUser(id){
      this.usersStore.deleteUser(id)
      .then(() => {
        this.usersStore.getUsers()
      })
    }
  },
  created() {
    this.usersStore.getUsers()
  },
}
</script>