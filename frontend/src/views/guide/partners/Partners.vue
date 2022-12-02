<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Партнеры</h1>
    </div>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <div class="support-bar d-flex flex-row justify-content-end py-2">
                <router-link class="btn btn-primary me-2" :to="{ name: 'guide-partners-create' }">
                  <i class="bi bi-plus-square"></i>&nbspДобавить
                </router-link>

                <button class="btn btn-primary me-2" @click="exportPartners">
                  <i class="bi bi-download"></i>&nbspЭкспорт
                </button>

                <div class="btn-import">
                  <label for="btn-import" class="btn btn-primary"><i class="bi bi-upload"></i>&nbspИмпорт</label>
                  <input type="file" id="btn-import" @change="importPartners" ref="file" hidden>
                </div>
              </div>

              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Наименование</th>
                      <th scope="col">ИНН</th>
                      <th scope="col">Регион</th>
                      <th scope="col">Базовая скидка</th>
                      <th scope="col">Операция</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in guidePartnersStore.data" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.inn }}</td>
                      <td>{{ item.region }}</td>
                      <td>{{ item.discount }}</td>
                      <td>
                        <div class="d-flex flex-row">
                          <button type="button" class="btn btn-primary me-2" @click="onClickPartnerDelete(item.id)">
                            <i class="bi bi-x-square"></i>
                          </button>

                          <router-link class="btn btn-primary"
                            :to="{ name: 'guide-partners-edit', params: { id: item.id } }">
                            <i class="bi bi-pencil-square"></i>
                          </router-link>
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
import { useGuidePartnersStore } from '@/stores/guidePartners.js'

export default {
  name: 'Partners',
  setup() {
    const guidePartnersStore = useGuidePartnersStore()
    return { guidePartnersStore }
  },
  methods: {
    onClickPartnerDelete(id) {
      this.guidePartnersStore.deletePartner(id)
        .then(() => {
          this.guidePartnersStore.getPartners()
        })
    },

    exportPartners() {
      this.guidePartnersStore.exportPartners()
    },

    importPartners() {
      this.file = this.$refs.file.files[0]
      const formData = new FormData()
      formData.append('file', this.file)
      this.guidePartnersStore.importPartners(formData)
        .then(() => {
          this.guidePartnersStore.getPartners()
        })
      this.$refs.file.value = null;
    }
  },
  created() {
    this.guidePartnersStore.getPartners()
  }
}
</script>