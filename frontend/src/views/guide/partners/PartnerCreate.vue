<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Партнер</h1>
    </div>

    <section class="section">
      <form @submit.prevent="onSubmit">
        <validation-errors v-if="guidePartnersStore.errors" :validationErrors="guidePartnersStore.errors"></validation-errors>
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
import ValidationErrors from '@/components/ValidationErrors.vue'

export default {
  name: 'PartnerCreate',
  components: {
    PartnerForm,
    ValidationErrors,
  },
  setup() {
    const guidePartnersStore = useGuidePartnersStore()
    return { guidePartnersStore }
  },
  data() {
    return {
      partner: {
        name: '',
        inn: '',
        region: '',
        discount: '',
        contacts: [{
          fio: '',
          role: '',
          phone: '',
          email: ''
        }],
      }
    }
  },

  methods: {
    onSubmit() {
      this.guidePartnersStore.addPartner(this.partner)
        .then(() => {
          this.$router.push({ name: 'guide-partners' })
        })
    }
  }

}
</script>