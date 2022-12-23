<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Проект</h1>
    </div>

    <section class="section">
      <form @submit.prevent="onSubmit">
        <project-form :project="project"></project-form>

        <div class="row">
          <div class="col-lg-6">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Импорт спецификации</h5>
                <div class="col-12">
                  <label class="form-label">Шаблон типовой спецификации</label>
                  <select class="form-select" @change="applySpecification($event)">
                    <option value="">Не выбрано</option>
                    <option v-for="(specification, index) in guideSpecificationsStore.data" :key="specification.id"
                      :value="index">
                      {{ specification.name }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>

        <specification :specification="project.specification"></specification>
        <project-file-upload :files="files"></project-file-upload>
        <div class="text-end mb-3">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>
    </section>
  </main>
</template>

<script>
import { useProjectsStore } from '@/stores/projects'
import { useGuideSpecificationsStore } from '@/stores/guideSpecifications'
import ProjectForm from '@/components/projects/ProjectForm.vue'
import Specification from '@/components/specifications/Specification.vue'
import ProjectFileUpload from '@/components/projects/ProjectFileUpload.vue'

export default {
  name: 'ProjectCreate',
  components: {
    ProjectForm,
    Specification,
    ProjectFileUpload
  },
  setup() {
    const projectsStore = useProjectsStore()
    const guideSpecificationsStore = useGuideSpecificationsStore()
    return { projectsStore, guideSpecificationsStore }
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
        partner_id: '',
        commentary: '',
        specification: {
          guide: false,
          requests: [
            {
              str_by_order: '',
              name: '',
              tx: '',
              amount: '',
              price: '',
              offers: [{
                product: '',
                product_id: '',
                article: '',
                name: '',
                count: ''
              }],
            },
          ],
        }
      },
      files: [],
    }
  },

  methods: {
    applySpecification(event) {
      this.project.specification.requests = this.guideSpecificationsStore.data[event.target.value].requests
    },

    onSubmit() {
      this.projectsStore.addProject(this.project)
        .then(() => {
          if (this.files.length > 0) {
            const formData = new FormData()
            for (let file of this.files) {
              formData.append('files', file)
            }
            formData.append('project', this.projectsStore.project)

            this.projectsStore.fileUploadProject(formData)
          }
          
          this.$router.push({ name: 'projects' })
        })
    },
  },

  created() {
    this.guideSpecificationsStore.getFullSpecifications()
  }
}
</script>
