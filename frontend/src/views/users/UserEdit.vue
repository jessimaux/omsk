<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Пользователь</h1>
    </div>

    <section class="section">
      <form v-if="!usersStore.loading" @submit.prevent="onSubmit">
        <validation-errors v-if="usersStore.errors" :validationErrors="usersStore.errors"></validation-errors>
        <user-form :user="user" :action="'Update'"></user-form>
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
  components: {
    ValidationErrors,
    UserForm
  },
  setup() {
    const usersStore = useUsersStore()
    return { usersStore }
  },
  computed: {
    user() {
      return this.usersStore.data
    }
  },
  methods: {
    onSubmit() {
      this.usersStore.editUser(this.user.id, this.user).then(() => {
        this.$router.push({ name: 'users' })
      })
    }
  },
  created() {
    const id = this.$route.params.id
    this.usersStore.getUser(id).then(() => {
      if (this.usersStore.status === 404) this.$router.push({ name: '404' })
    })
  }
}
</script>
