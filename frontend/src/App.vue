<template>
  <Navbar v-if="globalStore.getShowNavbar && !authStore.isLoading" />
  <Sidebar v-if="globalStore.getShowSidebar && !authStore.isLoading" />
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
  }
}
</script>