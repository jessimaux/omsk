<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Поставщики</h1>
    </div>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <div class="support-bar d-flex flex-row justify-content-end py-2">
                <router-link class="btn btn-primary me-2" :to="{ name: 'guide-providers-create' }">
                  <i class="bi bi-plus-square"></i>&nbspДобавить
                </router-link>
              </div>

              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col" rowspan="2">#</th>
                      <th scope="col" rowspan="2">Направление</th>
                      <th scope="col" rowspan="2">Наименование</th>
                      <th scope="col" rowspan="2">ИНН</th>
                      <th scope="col" rowspan="2">Регион</th>
                      <th scope="col" rowspan="2">Базовая скидка</th>
                      <th class="text-center" scope="col" colspan="4">Контактное лицо</th>
                      <th scope="col" rowspan="2">Операция</th>
                    </tr>
                    <tr>
                      <th scope="col">ФИО</th>
                      <th scope="col">Роль</th>
                      <th scope="col">Телефон</th>
                      <th scope="col">Почта</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in guideProvidersStore.data" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.sphere }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.inn }}</td>
                      <td>{{ item.region }}</td>
                      <td>{{ item.discount }}</td>
                      <td>{{ item.contact_fio }}</td>
                      <td>{{ item.contact_role }}</td>
                      <td>{{ item.contact_phone }}</td>
                      <td>{{ item.contact_email }}</td>
                      <td>
                        <div class="d-flex flex-row">
                          <button type="button" class="btn btn-primary me-2"><i class="bi bi-x-square"
                              @click="onClickProviderDelete(item.id)"></i></button>

                          <router-link class="btn btn-primary"
                            :to="{ name: 'guide-providers-edit', params: { id: item.id } }"><i
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
import { useGuideProvidersStore } from '@/stores/guideProviders.js'

export default {
  name: 'Providers',
  setup() {
    const guideProvidersStore = useGuideProvidersStore()
    return { guideProvidersStore }
  },
  methods: {
    onClickProviderDelete(id) {
      this.guideProvidersStore.deleteProvider(id)
        .then(() => {
          this.guideProvidersStore.getProviders()
        })
    },
  },
  created() {
    this.guideProvidersStore.getProviders()
  }
}
</script>