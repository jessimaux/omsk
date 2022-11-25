<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Поставщик</h1>
    </div>

    <section class="section">
      <form v-if="!guideProvidersStore.loading" @submit.prevent="onSubmit">
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
  },

}
</script>