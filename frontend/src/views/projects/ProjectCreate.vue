<template>
  <main id="main" class="main">
    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <project-form :initialValues="initialValues" @projectSubmit="onSubmit">
          </project-form>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { useProjectsStore } from '@/stores/projects'

import ProjectForm from '@/components/Projects/ProjectForm.vue'

export default {
  name: 'ProjectCreate',
  components: {
    ProjectForm,
  },
  setup() {
    const projectsStore = useProjectsStore()
    return { projectsStore }
  },
  data() {
    return {
      initialValues: {
        name: '1',
        status: '1',
        company_name: '1',
        company_inn: '1',
        company_city: '1',
        company_region: '1',
        company_children: '1',
        reg_no: '1',
        nds: false,
        partner: '1',
        delivery_period: '2000-01-01',
        contract: false,
        commentary: '',
      }
    }
  },

  methods: {
    onSubmit(projectFormInput) {
      this.projectsStore.addFullProject(projectFormInput)
    }
  }

}
</script>