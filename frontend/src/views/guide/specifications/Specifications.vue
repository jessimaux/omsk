<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Спецификации</h1>
    </div>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <div class="support-bar d-flex flex-row justify-content-end py-2">
                <router-link class="btn btn-primary me-2" :to="{ name: 'guide-specifications-create' }">
                  <i class="bi bi-plus-square"></i>&nbspДобавить
                </router-link>
              </div>

              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Наименование</th>
                      <th scope="col">Описание</th>
                      <th scope="col">Операция</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in guideSpecificationsStore.data" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.description }}</td>
                      <td>
                        <div class="d-flex flex-row">
                          <button type="button" class="btn btn-primary me-2"><i class="bi bi-x-square"
                              @click="onClickSpecificationDelete(item.id)"></i></button>

                          <router-link class="btn btn-primary"
                            :to="{ name: 'guide-specifications-edit', params: { id: item.id } }"><i
                              class="bi bi-pencil-square"></i></router-link>
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
import { useGuideSpecificationsStore } from '@/stores/guideSpecifications.js'

export default {
  name: 'Specifications',
  setup() {
    const guideSpecificationsStore = useGuideSpecificationsStore()
    return { guideSpecificationsStore }
  },
  methods: {
    onClickSpecificationDelete(id) {
      this.guideSpecificationsStore.deleteSpecification(id)
        .then(() => {
          this.guideSpecificationsStore.getSpecifications()
        })
    },
  },
  created() {
    this.guideSpecificationsStore.getSpecifications()
  }
}
</script>