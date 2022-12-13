<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Закупки</h1>
    </div>
    <section class="section">
      <form v-if="(!purchasesStore.loading && !projectsStore.loading)" @submit.prevent="onSubmit">
        <purchase-form :purchase="purchase" :project="project"></purchase-form>
        <div class="text-end mb-3">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>
    </section>
  </main>
</template>

<script>
import { usePurchasesStore } from '@/stores/purchase'
import { useProjectsStore } from '@/stores/projects'
import PurchaseForm from '@/components/projects/PurchaseForm.vue'

export default {
  name: 'Purchase',
  components: {
    PurchaseForm,
  },
  setup() {
    const purchasesStore = usePurchasesStore()
    const projectsStore = useProjectsStore()
    return { purchasesStore, projectsStore }
  },
  computed: {
    purchase() {
      return this.purchasesStore.data
    },
    project() {
      const { specification, ...newProject } = this.projectsStore.data
      return newProject
    }
  },
  methods:{
    onSubmit(){
      this.projectsStore.patchProject(this.project.id, this.project)
      this.purchasesStore.editPurchase(this.purchase.id, this.purchase)
    }
  },
  created() {
    const id = this.$route.params.id
    this.projectsStore.getProject(id)
      .then(() => {
        this.purchasesStore.getPurchase(this.projectsStore.data.purchase_id)
      })
  }
}
</script>