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
  </div>

  <div class="row">
    <div v-for="(contact, index) in partner.contacts" :key="contact.id" class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Контактное лицо
              <i class="bi bi-plus-square" @click="addContact(partner.contacts)"></i>
              <i v-show="(partner.contacts.length > 1)" class="bi bi-dash-square" @click="deleteContact(partner.contacts, index)"></i>
          </h5>
          <div class="col-12">
            <label class="form-label">ФИО</label>
            <input type="text" class="form-control" v-model="contact.fio">
          </div>

          <div class="col-12">
            <label class="form-label">Роль</label>
            <input type="text" class="form-control" v-model="contact.role">
          </div>

          <div class="col-12">
            <label class="form-label">Контактный телефон</label>
            <input type="text" class="form-control" v-model="contact.phone">
          </div>

          <div class="col-12">
            <label class="form-label">E-mail</label>
            <input type="text" class="form-control" v-model="contact.email">
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
  },
  methods: {
    addContact(fieldType) {
      fieldType.push({
        fio: '',
        role: '',
        phone: '',
        email: ''
      })
    },
    deleteContact(fieldType, index) {
      fieldType.splice(index, 1)
    }
  }
}
</script>