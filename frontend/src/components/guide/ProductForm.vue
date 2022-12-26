<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Общее</h5>
          <div class="col-12">
            <label class="form-label" name="str_by_order">№ по приказу</label>
            <input type="text" class="form-control" v-model="product.str_by_order" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="article">Артикул</label>
            <input type="text" class="form-control" v-model="product.article" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="name">Наименование</label>
            <input type="text" class="form-control" v-model="product.name" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="price_rrc">РРЦ</label>
            <input type="number" class="form-control" v-model="product.price_rrc" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="price_buy">Закупочная стоимость</label>
            <input type="number" class="form-control" v-model="product.price_buy" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="provider">Поставщик</label>
            <select class="form-select" v-model="product.provider" required>
              <option v-if="!guideProvidersStore.loading" v-for="provider in guideProvidersStore.data" :key="provider.id" :value="provider.id">
                {{ provider.name }}
              </option>
            </select>
          </div>

          <div class="col-12">
            <label class="form-label" name="nds">НДС</label>
            <input type="number" min="0" class="form-control" v-model="product.nds" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="available">Наличие</label>
            <input type="number" min="0" class="form-control" v-model="product.available" required>
          </div>
        </div>
      </div>
    </div>

    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Описание</h5>
          <div class="col-12">
            <label class="form-label" name="link">Ссылка</label>
            <input type="text" class="form-control" v-model="product.link" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="country">Страна происхождения</label>
            <input type="text" class="form-control" v-model="product.country" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="description">Описание</label>
            <textarea class="form-control" style="resize:none" rows="5" v-model="product.description" required></textarea>
          </div>

          <div class="col-12">
            <label class="form-label" name="description_tech">ТЗ</label>
            <textarea class="form-control" style="resize:none" rows="5" v-model="product.description_tech" required></textarea>
          </div>

          <div class="col-12">
            <label class="form-label" name="description_add">Заявка</label>
            <textarea class="form-control" style="resize:none" rows="5" v-model="product.description_add" required></textarea>
          </div>

          <div class="col-12">
            <label class="form-label" name="recommendation">Рекомендации</label>
            <textarea class="form-control" style="resize:none" rows="5" v-model="product.recommendation" required></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useGuideProvidersStore } from '@/stores/guideProviders'

export default {
  name: 'ProductForm',
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  setup() {
    const guideProvidersStore = useGuideProvidersStore()
    return { guideProvidersStore }
  },
  created() {
    this.guideProvidersStore.getFullProviders()
  }
}
</script>