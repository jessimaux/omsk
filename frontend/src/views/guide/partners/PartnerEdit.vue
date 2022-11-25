<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Партнер</h1>
    </div>

    <section class="section">
      <form v-if="!guidePartnersStore.loading" @submit.prevent="onSubmit">
        <partner-form :partner="partner"></partner-form>
        <div class="text-end mb-3">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>
    </section>
  </main>
</template>

<script>
import { useGuidePartnersStore } from '@/stores/guidePartners'
import PartnerForm from '@/components/guide/PartnerForm.vue'

export default {
  name: 'PartnerEdit',
  components: {
    PartnerForm,
  },
  setup() {
    const guidePartnersStore = useGuidePartnersStore()
    return { guidePartnersStore }
  },
  computed: {
    partner() {
      return this.guidePartnersStore.data
    }
  },

  methods: {
    onSubmit() {
      const id = this.$route.params.id
      this.guidePartnersStore.editPartner(id, this.partner)
        .then(() => {
          this.$router.push({ name: 'guide-partners' })
        })
    }
  },

  created() {
    const id = this.$route.params.id
    this.guidePartnersStore.getPartner(id)
  },

}
</script>