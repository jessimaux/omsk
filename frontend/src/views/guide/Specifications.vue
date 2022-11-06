<template>
  <main id="main" class="main">
    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">Спецификации</h5>

              <!-- Default Table -->
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
                    <tr v-for="item in guideStore.getData" :key="item.id">
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
import { useGuideStore } from '@/stores/guide.js'

export default {
  name: 'Specifications',
  setup() {
    const guideStore = useGuideStore()
    return { guideStore }
  },
  created() {
    this.guideStore.getSpecifications()
  }
}
</script>