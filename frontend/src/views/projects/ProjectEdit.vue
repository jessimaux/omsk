<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Проект</h1>
    </div>

    <section class="section">
      <form v-if="!projectsStore.loading" @submit.prevent="onSubmit">
        <project-form :project="project"></project-form>
        <specification :specification="project.specification">
        </specification>
        <order-buyer-form :specification_id="this.projectsStore.data.specification.id"></order-buyer-form>
        <project-file-upload :files="files" :uploadedFiles="project.files"></project-file-upload>
        <p class="small fst-italic">Создано {{ project.created_by }} в {{ project.created_at }}</p>
        <p class="small fst-italic">Обновлено {{ project.updated_by }} в {{ project.updated_at }}</p>
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
import OrderBuyerForm from '@/components/projects/OrderBuyerForm.vue'
import ProjectFileUpload from '@/components/projects/ProjectFileUpload.vue'

export default {
  name: 'ProjectEdit',
  components: {
    ProjectForm,
    Specification,
    OrderBuyerForm,
    ProjectFileUpload,
  },
  setup() {
    const projectsStore = useProjectsStore()
    return { projectsStore }
  },
  data() {
    return {
      files: [],
    }
  },
  computed: {
    project() {
      return this.projectsStore.data
    }
  },
  methods: {
    onSubmit() {
      this.projectsStore.editProject(this.project.id, this.project)
        .then(() => {
          const files_id = this.files.map((obj) => obj.id)
          this.projectsStore.data.files.forEach((object)=>{
            if(object.id in files_id === false){
              this.projectsStore.fileDeleteProject(object.id)
            } 
          })

          if (this.files.length > 0) {
            const formData = new FormData()
            for (let file of this.files) {
              formData.append('files', file)
            }
            formData.append('project', this.project.id)
            this.projectsStore.fileUploadProject(formData)
          }
          this.$router.push({ name: 'projects' })
        })
    }
  },
  created() {
    const id = this.$route.params.id
    this.projectsStore.getProject(id)
      .then(() => {
        if (this.projectsStore.status === 404) this.$router.push({ name: '404' })
      })
  }
}
</script>
