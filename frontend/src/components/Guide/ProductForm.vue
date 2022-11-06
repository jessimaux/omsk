<template>
  <div class="card">
    <div class="card-header">
      <h5 class="card-title">Продукт</h5>
    </div>
    <div class="card-body">
      <form class="row g-3" @submit.prevent="onSubmit">
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

        <div class="text-center">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>

    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductForm',
  props: {
    initialValues: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      product: {
        str_by_order: this.initialValues.str_by_order,
        article: this.initialValues.article,
        name: this.initialValues.name,
        price_rrc: this.initialValues.price_rrc,
        price_buy: this.initialValues.price_buy,
        link: this.initialValues.link,
        country: this.initialValues.country,
        description: this.initialValues.description,
        description_tech: this.initialValues.description_tech,
        description_add: this.initialValues.description_add,
        recommendation: this.initialValues.recommendation,
        provider: this.initialValues.provider,
        nds: this.initialValues.nds,
        available: this.initialValues.available
      }
    }
  },
  methods: {
    onSubmit() {
      this.$emit('productSubmit', this.product)
    }
  }
}
</script>