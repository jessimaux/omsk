<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Пользователь</h1>
    </div>

    <section class="section">
      <form @submit.prevent="onSubmit">
        <validation-errors v-if="usersStore.errors" :validationErrors="usersStore.errors"></validation-errors>
        <user-form :user="user" :action="'Create'"></user-form>
      </form>
    </section>
  </main>
</template>

<script>
import { useUsersStore } from '@/stores/users'
import UserForm from '@/components/users/UserForm.vue'
import ValidationErrors from '@/components/ValidationErrors.vue'


export default {
  name: 'UserCreate',
  components:{
    ValidationErrors,
    UserForm,
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