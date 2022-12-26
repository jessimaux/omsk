<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Общее</h5>
          <div class="col-12">
            <label class="form-label" name="name">Наименование</label>
            <input type="text" class="form-control" v-model="partner.name">
          </div>

          <div class="col-12">
            <label class="form-label" name="inn">ИНН</label>
            <input type="text" class="form-control" v-model="partner.inn" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="region">Город / Регион</label>
            <input type="text" class="form-control" v-model="partner.region" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="discount">Базовая скидка</label>
            <input type="number" class="form-control" v-model="partner.discount" required>
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
            <i v-show="(partner.contacts.length > 1)" class="bi bi-dash-square"
              @click="deleteContact(partner.contacts, index)"></i>
          </h5>
          <div class="col-12">
            <label class="form-label" name="fio">ФИО</label>
            <input type="text" class="form-control" v-model="contact.fio" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="role">Роль</label>
            <input type="text" class="form-control" v-model="contact.role" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="phone">Контактный телефон</label>
            <input type="text" class="form-control" v-model="contact.phone" required>
          </div>

          <div class="col-12">
            <label class="form-label" name="email">E-mail</label>
            <input type="text" class="form-control" v-model="contact.email" required>
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