<template>
  <header id="header" class="header fixed-top d-flex align-items-center">

    <div class="d-flex align-items-center justify-content-between">
      <router-link class="logo d-flex align-items-center" :to="{ name: 'home' }">
        <span class="d-none d-lg-block">Project</span>
      </router-link>
    </div><!-- End Logo -->

    <nav class="header-nav ms-auto">
      <ul class="d-flex align-items-center">

        <li class="nav-item dropdown pe-3">

          <a class="nav-link nav-profile d-flex align-items-center pe-0" href="#" data-bs-toggle="dropdown">
            <span class="d-none d-md-block dropdown-toggle ps-2">{{ user.username }}</span>
          </a><!-- End Profile Iamge Icon -->

          <ul class="dropdown-menu dropdown-menu-end dropdown-menu-arrow profile">
            <li class="dropdown-header">
              <h6>{{ user.username }}</h6>
            </li>
            <li>
              <hr class="dropdown-divider">
            </li>

            <li>
              <a class="dropdown-item d-flex align-items-center" href="#" @click="onClickLogout">
                <i class="bi bi-box-arrow-right"></i>
                <span>Выйти</span>
              </a>
            </li>

          </ul><!-- End Profile Dropdown Items -->
        </li><!-- End Profile Nav -->

      </ul>
    </nav><!-- End Icons Navigation -->

  </header><!-- End Header -->

</template>

<script>
import { useAuthStore } from '@/stores/auth.js'

export default {
  name: 'Navbar',
  setup() {
    const authStore = useAuthStore()
    return { authStore }
  },
  computed: {
    user() {
      return this.authStore.currentUser
    }
  },
  methods: {
    onClickLogout() {
      this.authStore
        .logout()
        .then(() => {
          this.$router.push({ name: 'login' })
        })
    }
  }
}
</script>