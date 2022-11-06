<template>
  <main id="main" class="main">
    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Продукты</h5>
              <router-link :to="{ name: 'guide-products-create' }">
                <button class="btn btn-primary"><i class="bi bi-plus-square"></i>Добавить</button>
              </router-link>

              <button class="btn btn-primary" @click="exportProducts"><i class="bi bi-download"></i>Экспорт</button>

              <input type="file" @change="importProducts" ref="file">
            </div>
            <div class="card-body">
              <!-- Default Table -->
              <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">№</th>
                      <th scope="col">Артикул</th>
                      <th scope="col">Наименование</th>
                      <th scope="col">РРЦ</th>
                      <th scope="col">Закупочная стоимость</th>
                      <th scope="col">Ссылка</th>
                      <th scope="col">Страна происхождения</th>
                      <th scope="col">Описание</th>
                      <th scope="col">ТЗ</th>
                      <th scope="col">Заявка</th>
                      <th scope="col">Рекомендации</th>
                      <th scope="col">Поставщик</th>
                      <th scope="col">НДС</th>
                      <th scope="col">Наличие</th>
                      <th scope="col">Операция</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in   guideStore.getData" :key="item.id">
                      <td>{{ item.id }}</td>
                      <td>{{ item.str_by_order }}</td>
                      <td>{{ item.article }}</td>
                      <td>{{ item.name }}</td>
                      <td>{{ item.price_rrc }}</td>
                      <td>{{ item.price_buy }}</td>
                      <td>{{ item.link }}</td>
                      <td>{{ item.country }}</td>
                      <td>{{ item.description }}</td>
                      <td>{{ item.description_tech }}</td>
                      <td>{{ item.description_add }}</td>
                      <td>{{ item.recommendation }}</td>
                      <td>{{ item.provider }}</td>
                      <td>{{ item.nds }}</td>
                      <td>{{ item.available }}</td>
                      <td>
                        <i class="bi bi-x-square" @click="onClickProductDelete(item.id)"></i>
                        <router-link :to="{ name: 'guide-products-edit', params: { id: item.id } }"><i
                            class="bi bi-pencil-square"></i></router-link>
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
import { useGuideStore } from '@/stores/guide.js'

export default {
  name: 'Products',
  setup() {
    const guideStore = useGuideStore()
    return { guideStore }
  },
  data() {
    return {
      file: null,
    }
  },
  methods: {
    onClickProductDelete(id) {
      this.guideStore.deleteProduct(id)
        .then(() => {
          this.guideStore.getProducts()
        })
    },

    exportProducts() {
      this.guideStore.exportProducts()
    },

    importProducts() {
      this.file = this.$refs.file.files[0]
      const formData = new FormData()
      formData.append('file', this.file)
      this.guideStore.importProducts(formData)
        .then(() => {
          this.guideStore.getProducts()
        })
      this.$refs.file.value = null;
    }
  },
  created() {
    this.guideStore.getProducts()
  }
}
</script>