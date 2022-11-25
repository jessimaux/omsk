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
              <h5 class="card-title">Партнеры</h5>

              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col" rowspan="2">#</th>
                      <th scope="col" rowspan="2">Наименование</th>
                      <th scope="col" rowspan="2">ИНН</th>
                      <th scope="col" rowspan="2">Город / Регион</th>
                      <th scope="col" rowspan="2">Базовая скидка</th>
                      <th class="text-center" scope="col" colspan="4">Контактное лицо</th>
                    </tr>
                    <tr>
                      <th scope="col">ФИО</th>
                      <th scope="col">Роль</th>
                      <th scope="col">Телефон</th>
                      <th scope="col">Почта</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in guidePartnersStore.data" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.inn }}</td>
                      <td>{{ item.region }}</td>
                      <td>{{ item.discount }}</td>
                      <td>{{ item.contact_fio }}</td>
                      <td>{{ item.contact_role }}</td>
                      <td>{{ item.contact_phone }}</td>
                      <td>{{ item.contact_email }}</td>
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
  created() {
    this.guidePartnersStore.getPartners()
  }
}
</script>