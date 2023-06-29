<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Общее</h5>
          <div class="col-12">
            <label class="form-label required">Имя пользователя</label>
            <div class="input-group mb-3">
              <input type="text" class="form-control" v-model="user.username" :disabled="action==='Update'" required />
              <button v-if="action === 'Update'"
                class="btn btn-outline-secondary"
                type="button"
                id="button-addon2"
                @click="onClickAddPasswordForm">
                Изменить пароль
              </button>
            </div>
          </div>

          <div class="col-12">
            <label class="form-label">Имя</label>
            <input type="text" class="form-control" v-model="user.first_name" />
          </div>

          <div class="col-12">
            <label class="form-label">Фамилия</label>
            <input type="last_name" class="form-control" v-model="user.last_name" />
          </div>

          <div class="col-12">
            <label class="form-label required">Email</label>
            <input type="email" class="form-control" v-model="user.email" required />
          </div>

          <div v-if="action === 'Create' || (action === 'Update' && changePassword)" class="col-12">
            <label class="form-label required" name="password">Пароль</label>
            <input type="password" class="form-control" v-model="user.password" required />
          </div>

          <div v-if="action === 'Create' || (action === 'Update' && changePassword)" class="col-12">
            <label class="form-label required" name="password">Повторите пароль</label>
            <input type="password" class="form-control" v-model="repeat_password" required />
            <div v-if="!comparePassword" class="text-danger">Пароли не совпадают</div>
          </div>

          <div v-if="action === 'Update'" class="col-12">
            <label class="form-label" name="is_active">Активен</label>
            <div class="form-check">
              <input type="checkbox" class="form-check-input" v-model="user.is_active" />
            </div>
          </div>
        </div>
      </div>

      <div class="text-end mb-3">
        <button type="submit" class="btn btn-primary" :disabled="!comparePassword">Сохранить</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserForm',
  props: {
    user: {
      type: Object,
      required: true
    },
    action: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      changePassword: false,
      repeat_password: ''
    }
  },
  computed: {
    comparePassword() {
      if (this.action === 'Create' || (this.action === 'Update' && this.changePassword)) {
        return this.user.password === this.repeat_password ? true : false
      } else {
        return true
      }
    }
  },
  methods: {
    onClickAddPasswordForm() {
      this.changePassword = !this.changePassword
    }
  }
}
</script>
