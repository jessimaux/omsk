<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Общее</h5>
          <div class="col-12">
            <label class="form-label">Наименование</label>
            <input type="text" class="form-control" v-model="provider.name" required>
          </div>

          <div class="col-12">
            <label class="form-label">Сфера</label>
            <input type="text" class="form-control" v-model="provider.sphere" required>
          </div>

          <div class="col-12">
            <label class="form-label">ИНН</label>
            <input type="text" class="form-control" v-model="provider.inn" required>
          </div>

          <div class="col-12">
            <label class="form-label">Город / Регион</label>
            <input type="text" class="form-control" v-model="provider.region" required>
          </div>

          <div class="col-12">
            <label class="form-label">Базовая скидка</label>
            <input type="number" class="form-control" v-model="provider.discount" required>
          </div>

        </div>
      </div>
    </div>
  </div>

  <div class="row">
    <div v-for="(contact, index) in provider.contacts" :key="provider.id" class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Контактное лицо
            <i class="bi bi-plus-square" @click="addContact(provider.contacts)"></i>
            <i v-show="(provider.contacts.length > 1)" class="bi bi-dash-square"
              @click="deleteContact(provider.contacts, index)"></i>
          </h5>
          <div class="col-12">
            <label class="form-label">ФИО</label>
            <input type="text" class="form-control" v-model="contact.fio" required>
          </div>

          <div class="col-12">
            <label class="form-label">Роль</label>
            <input type="text" class="form-control" v-model="contact.role" required>
          </div>

          <div class="col-12">
            <label class="form-label">Контактный телефон</label>
            <input type="text" class="form-control" v-model="contact.phone" required>
          </div>

          <div class="col-12">
            <label class="form-label">E-mail</label>
            <input type="text" class="form-control" v-model="contact.email" required>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProviderForm',
  props: {
    provider: {
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