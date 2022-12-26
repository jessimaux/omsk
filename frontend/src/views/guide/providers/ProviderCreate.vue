<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Поставщик</h1>
    </div>

    <section class="section">
      <form @submit.prevent="onSubmit">
        <validation-errors v-if="guideProvidersStore.errors" :validationErrors="guideProvidersStore.errors"></validation-errors>
        <provider-form :provider="provider"></provider-form>
        <div class="text-end mb-3">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>
    </section>
  </main>
</template>

<script>
import { useGuideProvidersStore } from '@/stores/guideProviders'
import ProviderForm from '@/components/guide/ProviderForm.vue'
import ValidationErrors from '@/components/ValidationErrors.vue'

export default {
  name: 'ProviderCreate',
  components: {
    ProviderForm,
  },
  setup() {
    const guideProvidersStore = useGuideProvidersStore()
    return { guideProvidersStore }
  },
  data() {
    return {
      provider: {
        name: '',
        sphere: '',
        inn: '',
        region: '',
        discount: '',
        contacts: [{
          fio: '',
          role: '',
          phone: '',
          email: ''
        }]
      }
    }
  },

  methods: {
    onSubmit() {
      this.guideProvidersStore.addProvider(this.provider)
        .then(() => {
          this.$router.push({ name: 'guide-providers' })
        })
    }
  }

}
</script>