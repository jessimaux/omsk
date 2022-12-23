<template>
<main>
    <div class="container">

      <section class="section error-404 min-vh-100 d-flex flex-column align-items-center justify-content-center">
        <h1>404</h1>
        <h2>Страница не найдена.</h2>
        <router-link class="btn" :to="{ name: 'projects' }">Вернуться на главную</router-link>
      </section>

    </div>
  </main>
</template>

<script>
import { useGlobalStore } from "@/stores/global"

export default{
  name: 'NotFound',
  setup() {
    const globalStore = useGlobalStore()
    return { globalStore }
  },
  created() {
    this.globalStore.showSidebar = false
    this.globalStore.showNavbar = false
  },
  beforeUnmount() {
    this.globalStore.showSidebar = true
    this.globalStore.showNavbar = true
  }
}
</script>