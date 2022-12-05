<template>
  <main id="main" class="main">
    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Проекты</h5>
              <router-link :to="{ name: 'project-create' }"><button class="btn btn-primary"><i
                    class="bi bi-plus-square"></i>Добавить</button></router-link>
              <!-- Default Table -->
              <div v-if="!projectsStore.loading" class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">№ счета</th>
                      <th scope="col">Статус проекта</th>
                      <th scope="col">Контрагент</th>
                      <th scope="col">Компания</th>
                      <th scope="col">Общая сумма счета</th>
                      <th scope="col">Отгружено на сумму</th>
                      <th scope="col">Товары</th>
                      <th scope="col">Срок поставки</th>
                      <th scope="col">Комментарии</th>
                      <th scope="col">Наличие товара</th>
                      <th scope="col">Операция</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in projectsStore.data.results" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>?</td>
                      <td>{{ item.status }}</td>
                      <td>{{ item.partner }}</td>
                      <td>{{ item.company }}</td>
                      <td>?</td>
                      <td>?</td>
                      <td>?</td>
                      <td>{{ item.delivery_period }}</td>
                      <td>{{ item.commentary }}</td>
                      <td>?</td>
                      <td>
                        <div class="d-flex flex-row">
                          <button type="button" class="btn btn-primary me-2"><i class="bi bi-x-square"
                              @click="onClickProjectDelete(item.id)"></i></button>

                          <router-link class="btn btn-primary" :to="{ name: 'project-edit', params: { id: item.id } }">
                            <i class="bi bi-pencil-square"></i></router-link>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { useProjectsStore } from '@/stores/projects.js'
export default {
  name: 'Projects',
  setup() {
    const projectsStore = useProjectsStore()
    return { projectsStore }
  },
  methods: {
    onClickProjectDelete(id) {
      this.projectsStore.deleteProject(id)
        .then(() => {
          this.projectsStore.getProjects()
        })
    },
  },
  created() {
    this.projectsStore.getProjects()
  }
}
</script>