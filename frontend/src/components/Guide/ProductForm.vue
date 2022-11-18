<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Общее</h5>
          <div class="col-12">
            <label class="form-label">№ по приказу</label>
            <input type="text" class="form-control" v-model="product.str_by_order">
          </div>

          <div class="col-12">
            <label class="form-label">Артикул</label>
            <input type="text" class="form-control" v-model="product.article">
          </div>

          <div class="col-12">
            <label class="form-label">Наименование</label>
            <input type="text" class="form-control" v-model="product.name">
          </div>

          <div class="col-12">
            <label class="form-label">РРЦ</label>
            <input type="text" class="form-control" v-model="product.price_rrc">
          </div>

          <div class="col-12">
            <label class="form-label">Закупочная стоимость</label>
            <input type="text" class="form-control" v-model="product.price_buy">
          </div>

          <div class="col-12">
            <label class="form-label">Поставщик</label>
            <input type="text" class="form-control" v-model="product.provider">
          </div>

          <div class="col-12">
            <label class="form-label">НДС</label>
            <input type="text" class="form-control" v-model="product.nds">
          </div>

          <div class="col-12">
            <label class="form-label">Наличие</label>
            <input type="text" class="form-control" v-model="product.available">
          </div>
        </div>
      </div>
    </div>

    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Описание</h5>
          <div class="col-12">
            <label class="form-label">Ссылка</label>
            <input type="text" class="form-control" v-model="product.link">
          </div>

          <div class="col-12">
            <label class="form-label">Страна происхождения</label>
            <input type="text" class="form-control" v-model="product.country">
          </div>

          <div class="col-12">
            <label class="form-label">Описание</label>
            <input type="text" class="form-control" v-model="product.description">
          </div>

          <div class="col-12">
            <label class="form-label">ТЗ</label>
            <input type="text" class="form-control" v-model="product.description_tech">
          </div>

          <div class="col-12">
            <label class="form-label">Заявка</label>
            <input type="text" class="form-control" v-model="product.description_add">
          </div>

          <div class="col-12">
            <label class="form-label">Рекомендации</label>
            <input type="text" class="form-control" v-model="product.recommendation">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductForm',
  props: {
    product: {
      type: Object,
      required: true
    }
  },
}
</script>