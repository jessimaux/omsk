<template>
  <main id="main" class="main">
    <div class="pagetitle">
      <h1>Продукты</h1>
    </div>

    <section class="section">
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <div class="support-bar d-flex flex-row justify-content-end py-2">
                <router-link class="btn btn-primary me-2" :to="{ name: 'guide-products-create' }">
                  <i class="bi bi-plus-square"></i>&nbspДобавить
                </router-link>

                <button class="btn btn-primary me-2" @click="exportProducts">
                  <i class="bi bi-download"></i>&nbspЭкспорт
                </button>

                <div class="btn-import">
                  <label for="btn-import" class="btn btn-primary"><i class="bi bi-upload"></i>&nbspИмпорт</label>
                  <input type="file" id="btn-import" @change="importProducts" ref="file" hidden>
                </div>
              </div>

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
                    <tr v-for="item in guideProductsStore.getData" :key="item.id">
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
                        <div class="d-flex flex-row">
                          <button type="button" class="btn btn-primary me-2"><i class="bi bi-x-square"
                              @click="onClickProductDelete(item.id)"></i></button>
                          <router-link class="btn btn-primary"
                            :to="{ name: 'guide-products-edit', params: { id: item.id } }"><i
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
import { useGuideProductsStore } from '@/stores/guideProducts.js'

export default {
  name: 'Products',
  setup() {
    const guideProductsStore = useGuideProductsStore()
    return { guideProductsStore }
  },
  data() {
    return {
      file: null,
    }
  },
  methods: {
    onClickProductDelete(id) {
      this.guideProductsStore.deleteProduct(id)
        .then(() => {
          this.guideProductsStore.getProducts()
        })
    },

    exportProducts() {
      this.guideProductsStore.exportProducts()
    },

    importProducts() {
      this.file = this.$refs.file.files[0]
      const formData = new FormData()
      formData.append('file', this.file)
      this.guideProductsStore.importProducts(formData)
        .then(() => {
          this.guideProductsStore.getProducts()
        })
      this.$refs.file.value = null;
    }
  },
  created() {
    this.guideProductsStore.getProducts()
  }
}
</script>