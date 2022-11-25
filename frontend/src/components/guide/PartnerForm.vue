<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Общее</h5>
          <div class="col-12">
            <label class="form-label">Наименование</label>
            <input type="text" class="form-control" v-model="partner.name" required>
          </div>

          <div class="col-12">
            <label class="form-label">ИНН</label>
            <input type="text" class="form-control" v-model="partner.inn" required>
          </div>

          <div class="col-12">
            <label class="form-label">Город / Регион</label>
            <input type="text" class="form-control" v-model="partner.region" required>
          </div>

          <div class="col-12">
            <label class="form-label">Базовая скидка</label>
            <input type="text" class="form-control" v-model="partner.discount" required>
          </div>

        </div>
      </div>
    </div>

    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Контактное лицо</h5>
          <div class="col-12">
            <label class="form-label">ФИО</label>
            <input type="text" class="form-control" v-model="partner.contact_fio">
          </div>

          <div class="col-12">
            <label class="form-label">Роль</label>
            <input type="text" class="form-control" v-model="partner.contact_role">
          </div>

          <div class="col-12">
            <label class="form-label">Контактный телефон</label>
            <input type="text" class="form-control" v-model="partner.contact_phone">
          </div>

          <div class="col-12">
            <label class="form-label">E-mail</label>
            <input type="text" class="form-control" v-model="partner.contact_email">
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PartnerForm',
  props: {
    partner: {
      type: Object,
      required: true
    }
  }
}
</script>