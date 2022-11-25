<template>
  <Navbar v-if="globalStore.getShowNavbar && !authStore.getIsLoading" />
  <Sidebar v-if="globalStore.getShowSidebar && !authStore.getIsLoading" />
  <router-view></router-view>
</template>

<script>
import Navbar from './components/navbar/Navbar.vue'
import Sidebar from './components/sidebar/Sidebar.vue'
import { useGlobalStore } from '@/stores/global'
import { useAuthStore } from '@/stores/auth'

export default {
  name: "App",
  setup() {
    const globalStore = useGlobalStore()
    const authStore = useAuthStore()
    return { globalStore, authStore }
  },
  components: {
    Sidebar,
    Navbar,
  },
  mounted() {
    this.authStore.getCurrentUser()
  }
}
</script>

<style>

</style>
