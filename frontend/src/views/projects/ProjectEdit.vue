<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Проект</h1>
    </div>

    <section class="section">
      <form v-if="!projectsStore.loading" @submit.prevent="onSubmit">
        <project-form :project="project"></project-form>
        <specification :requestOffer="requestOffer" :deleteRequests="deleteRequests" :deleteOffers="deleteOffers">
        </specification>
        <div class="text-end mb-3">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>
    </section>
  </main>
</template>

<script>
import { useProjectsStore } from '@/stores/projects'
import ProjectForm from '@/components/projects/ProjectForm.vue'
import Specification from '@/components/specifications/Specification.vue'

export default {
  name: 'ProjectEdit',
  components: {
    ProjectForm,
    Specification,
  },
  setup() {
    const projectsStore = useProjectsStore()
    return { projectsStore }
  },
  data() {
    return {
      deleteRequests: [],
      deleteOffers: []
    }
  },
  computed: {
    project() {
      return {
        name: this.projectsStore.data.name,
        status: this.projectsStore.data.status,
        partner: this.projectsStore.data.partner,
        reg_no: this.projectsStore.data.reg_no,
        nds: this.projectsStore.data.nds,
        company_name: this.projectsStore.data.company_name,
        company_inn: this.projectsStore.data.company_inn,
        company_city: this.projectsStore.data.company_city,
        company_region: this.projectsStore.data.company_region,
        company_children: this.projectsStore.data.company_children,
        commentary: this.projectsStore.data.commentary
      }
    },
    requestOffer() {
      return this.projectsStore.data.specification.requestOffer
    }
  },
  methods: {
    onSubmit() {
      this.projectsStore.editProject(this.project, this.requestOffer, this.deleteRequests, this.deleteOffers)
      .then(()=>{
        this.$router.push({ name: 'projects' })
      })
    }
  },
  created() {
    const id = this.$route.params.id
    this.projectsStore.getProject(id)
  }
}
</script>
