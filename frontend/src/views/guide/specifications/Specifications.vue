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
              <h5 class="card-title">Спецификации</h5>

              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Наименование</th>
                      <th scope="col">Количество позиций</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in guideSpecificationsStore.data" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.name }}</td>
                      <td> ? </td>
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
  created() {
    this.guideSpecificationsStore.getSpecifications()
  }
}
</script>