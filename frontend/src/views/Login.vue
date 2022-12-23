<template>
  <div class="container">
    <section class="section register min-vh-100 d-flex flex-column align-items-center justify-content-center py-4">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-4 col-md-6 d-flex flex-column align-items-center justify-content-center">
            <div class="card mb-3">
              <div class="card-body">

                <div class="pb-2">
                  <h5 class="card-title text-center pb-0 fs-4">Авторизация</h5>
                </div>

                <validation-errors :validationErrors="authStore.errors"></validation-errors>

                <form class="row g-3 needs-validation" @submit.prevent="onSubmit">

                  <div class="col-12">
                    <label for="yourUsername" class="form-label">Имя пользователя</label>
                    <div class="input-group has-validation">
                      <input type="text" name="username" class="form-control" id="yourUsername" v-model="user.username"
                        required>
                    </div>
                  </div>

                  <div class="col-12">
                    <label for="yourPassword" class="form-label">Пароль</label>
                    <input type="password" name="password" class="form-control" id="yourPassword"
                      v-model="user.password" required>
                  </div>

                  <div class="col-12">
                    <button class="btn btn-primary w-100" type="submit">Войти</button>
                  </div>

                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { defineComponent } from "vue"
import { useAuthStore } from '@/stores/auth'
import { useGlobalStore } from "@/stores/global"
import ValidationErrors from "@/components/ValidationErrors.vue"

export default defineComponent({
  name: "AppLogin",
  components: {
    ValidationErrors
  },
  setup() {
    const authStore = useAuthStore()
    const globalStore = useGlobalStore()
    return { authStore, globalStore }
  },
  data() {
    return {
      user: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    onSubmit() {
      this.authStore.login(this.user)
        .then(() => {
          this.$router.push({ name: 'projects' })
        })
    }
  },
  created() {
    this.globalStore.showSidebar = false
    this.globalStore.showNavbar = false
  },
  beforeUnmount() {
    this.globalStore.showSidebar = true
    this.globalStore.showNavbar = true
  }
})
</script>