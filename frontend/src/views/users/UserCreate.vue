<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Пользователь</h1>
    </div>

    <section class="section">
      <form @submit.prevent="onSubmit">
        <validation-errors v-if="usersStore.errors" :validationErrors="usersStore.errors"></validation-errors>
        <div class="row">
          <div class="col-lg-6">
            <div class="card">
              <div class="card-body">

                <h5 class="card-title">Общее</h5>
                <div class="col-12">
                  <label class="form-label" name="username">Наименование</label>
                  <input type="text" class="form-control" v-model="user.username" autocomplete="off" required>
                </div>

                <div class="col-12">
                  <label class="form-label" name="email">Email</label>
                  <input type="email" class="form-control" v-model="user.email" autocomplete="new-email" required>
                </div>

                <div class="col-12">
                  <label class="form-label" name="password">Пароль</label>
                  <input type="password" class="form-control" v-model="user.password" autocomplete="new-password" required>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="text-end mb-3">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      
      </form>
    </section>
  </main>
</template>

<script>
import { useUsersStore } from '@/stores/users'
import ValidationErrors from '@/components/ValidationErrors.vue'


export default {
  name: 'UserCreate',
  components:{
    ValidationErrors,
  },
  setup() {
    const usersStore = useUsersStore()
    return { usersStore }
  },
  data() {
    return {
      user: {
        email: '',
        username: '',
        password: ''
      }
    }
  },
  methods:{
    onSubmit(){
      this.usersStore.createUser(this.user)
      .then(()=>{
        this.$router.push({name: 'users'})
      })
    }
  }
}
</script>