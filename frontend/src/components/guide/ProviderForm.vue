<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Общее</h5>
          <div class="col-12">
            <label class="form-label required" name="name">Наименование</label>
            <input type="text" class="form-control" v-model="provider.name" required>
          </div>

          <div class="col-12">
            <label class="form-label required" name="sphere">Сфера</label>
            <input type="text" class="form-control" v-model="provider.sphere" required>
          </div>

          <div class="col-12">
            <label class="form-label required" name="inn">ИНН</label>
            <input type="text" class="form-control" v-model="provider.inn" required>
          </div>

          <div class="col-12">
            <label class="form-label required" name="region">Город / Регион</label>
            <input type="text" class="form-control" v-model="provider.region" required>
          </div>

          <div class="col-12">
            <label class="form-label required" name="discount">Базовая скидка</label>
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
          <div class="card-title">
          <h5 class="me-1">Контактное лицо</h5>
            <i class="bi bi-plus-square me-1" @click="addContact(provider.contacts)"></i>
            <i v-show="(provider.contacts.length > 1)" class="bi bi-dash-square me-1"
              @click="deleteContact(provider.contacts, index)"></i>
            </div>
          <div class="col-12">
            <label class="form-label required" name="fio">ФИО</label>
            <input type="text" class="form-control" v-model="contact.fio" required>
          </div>

          <div class="col-12">
            <label class="form-label required" name="role">Роль</label>
            <input type="text" class="form-control" v-model="contact.role" required>
          </div>

          <div class="col-12">
            <label class="form-label required" name="phone">Контактный телефон</label>
            <input type="text" class="form-control" v-model="contact.phone" required>
          </div>

          <div class="col-12">
            <label class="form-label required" name="email">E-mail</label>
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