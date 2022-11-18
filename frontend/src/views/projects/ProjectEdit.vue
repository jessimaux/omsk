<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Проект</h1>
    </div>

    <section class="section">
      <form v-if="!projectsStore.loading">
        <project-form :project="project"></project-form>
        <!-- <specification :requestOffer="requestOffer"></specification> -->

        <div class="text-end mb-3">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>
    </section>
  </main>
</template>

<script>
import { useProjectsStore } from '@/stores/projects'
import ProjectForm from '@/components/Projects/ProjectForm.vue'
import Specification from '@/components/Specifications/Specification.vue'

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
  computed: {
    project() {
      return this.projectsStore.data
    }
  },
  created() {
    const id = this.$route.params.id
    this.projectsStore.getProject(id)
  }
}
</script>
