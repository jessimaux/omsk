import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import { useAuthStore } from '@/stores/auth.js'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

import './assets/vendor/bootstrap-icons/bootstrap-icons.css'
import './assets/vendor/boxicons/css/boxicons.min.css'
import './assets/vendor/quill/quill.snow.css'
import './assets/vendor/quill/quill.bubble.css'
import './assets/vendor/remixicon/remixicon.css'
import './assets/vendor/simple-datatables/style.css'

import './assets/css/style.css'

startApp()

async function startApp() {
  const app = createApp(App)

  app.use(createPinia())
  app.use(router)

  // attempt to auto refresh token before startup
  try {
    const authStore = useAuthStore()
    await authStore.refreshToken()
    await authStore.getCurrentUser()
  } catch {
    // catch error to start app on success or failure
  }

  router.isReady().then(() => {
    app.mount('#app')
  })
}