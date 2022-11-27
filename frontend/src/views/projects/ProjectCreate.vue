<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Проект</h1>
    </div>

    <section class="section">
      <form @submit.prevent="onSubmit">
        <project-form :project="project" @projectFormSubmit="onStageSubmit"></project-form>
        <specification :requestOffer="requestOffer" @submit.prevent="onSubmit"></specification>

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
  name: 'ProjectCreate',
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
      project: {
        name: '',
        status: '',
        company_name: '',
        company_inn: '',
        company_city: '',
        company_region: '',
        company_children: '',
        reg_no: '',
        nds: true,
        partner: '',
        commentary: '',
      },
      requestOffer: [
        {
          str_by_order: '',
          name: '',
          tx: '',
          amount: '',
          price: '',
          offer: [{
            product: '',
            article: '',
            name: '',
            count: '',
            price: '0',
            available: '0',
          }],
        },
      ],
    }
  },

  methods: {
    onSubmit() {
      this.projectsStore.addProject(this.project)
        .then(() => {
          this.projectsStore.addSpecification()
            .then(() => {
              this.projectsStore.addRequestOffer(this.requestOffer)
                .then(() => {
                  this.$router.push({ name: 'projects' })
                })
            })
        })
    },
  },
}
</script>
