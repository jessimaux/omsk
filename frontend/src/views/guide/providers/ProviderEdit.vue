<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Поставщик</h1>
    </div>

    <section class="section">
      <form v-if="!guideProvidersStore.loading" @submit.prevent="onSubmit">
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
  name: 'ProviderEdit',
  components: {
    ProviderForm,
  },
  setup() {
    const guideProvidersStore = useGuideProvidersStore()
    return { guideProvidersStore }
  },
  computed: {
    provider() {
      return this.guideProvidersStore.data
    }
  },

  methods: {
    onSubmit() {
      const id = this.$route.params.id
      this.guideProvidersStore.editProvider(id, this.provider)
        .then(() => {
          this.$router.push({ name: 'guide-providers' })
        })
    }
  },

  created() {
    const id = this.$route.params.id
    this.guideProvidersStore.getProvider(id)
    .then(() => {
        if (this.guideProvidersStore.status === 404) this.$router.push({ name: '404' })
      })
  },

}
</script>