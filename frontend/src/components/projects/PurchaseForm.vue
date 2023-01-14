<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Общее</h5>
          <div class="col-12">
            <label class="form-label" name="company_from">От кого продаем</label>
            <input type="text" class="form-control" v-model="purchase.company_from" />
          </div>

          <div class="col-12">
            <label class="form-label">Уникальный номер проекта</label>
            <input type="text" class="form-control" v-model="project.id" disabled />
          </div>

          <div class="col-12">
            <label class="form-label" name="status">Статус проекта</label>
            <select class="form-select" v-model="project.status">
              <option v-for="attribute in statusSelect" :value="attribute">
                {{ attribute }}
              </option>
            </select>
          </div>

          <div class="col-12">
            <label class="form-label" name="project_inner_no">Внутренний номер проекта</label>
            <input type="text" class="form-control" v-model="purchase.project_inner_no" />
          </div>

          <div class="col-12">
            <label class="form-label" name="project_registration_no">Номер регистрации проекта</label>
            <input type="text" class="form-control" v-model="project.reg_no" disabled />
          </div>

          <div class="col-12">
            <label class="form-label" name="bill">Номер счета от нашей комании</label>
            <input type="text" class="form-control" v-model="purchase.bill" />
          </div>

          <div class="col-12">
            <label class="col-form-label">НДС</label>
            <div class="form-check">
              <input type="checkbox" class="form-check-input" v-model="project.nds" disabled />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="col-lg-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">О партнере</h5>
          <div class="col-12">
            <label class="form-label">Партнер</label>
            <select class="form-select" v-model="project.partner_id" disabled>
              <option v-if="!guidePartnersStore.loading" v-for="partner in guidePartnersStore.data.results"
                :key="partner.id" :value="partner.id">
                {{ partner.name }}
              </option>
            </select>
          </div>

          <div class="col-12">
            <label class="form-label">Скидка</label>
            <input type="text" class="form-control" :value="getDiscount" disabled />
          </div>
        </div>
      </div>
    </div>

  </div>

  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title" name="commentary">Комментарий</h5>
          <textarea class="form-control" style="resize:none" rows="5" v-model="project.commentary"></textarea>
        </div>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Форма закупок</h5>
          <button type="button" class="btn btn-primary me-2" @click="onClickExportPurchases()">
            <i class="bi bi-download"></i>&nbspЭкспорт
          </button>
          <div class="table-responsive mb-3">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Статус товара</th>
                  <th scope="col">ISBN поставщика</th>
                  <th scope="col">Наименование по спецификации</th>
                  <th scope="col">Страна происхождения по спецификации</th>
                  <th scope="col">Страна происхождения по базе</th>
                  <th scope="col">Количество</th>
                  <th scope="col">Артикул</th>
                  <th scope="col">Наименование в базе</th>
                  <th scope="col">Количество в 1 комплекте</th>
                  <th scope="col">Поставщик</th>
                  <th scope="col">Цена закупки</th>
                  <th scope="col">Сумма закупки</th>
                  <th scope="col">Цена продажи</th>
                  <th scope="col">Сумма продажи</th>
                  <th scope="col">НДС(база)</th>
                  <th scope="col">НДС(продажи)</th>
                  <th scope="col">Рентабельность %</th>
                  <th scope="col">Рентабельность РУБ</th>
                  <th scope="col">Срок поставки</th>
                  <th scope="col">Предоплата</th>
                  <th scope="col">Входящие счета</th>
                  <th scope="col">Оплата входяшего счета</th>
                  <th scope="col">Ориентировочный срок прихода на склад</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in purchase.purchases" :key="item.id">
                  <td>{{ index }}</td>
                  <td>
                    <select class="form-select purchase-status" v-model="item.status" required>
                      <option v-for="attribute in statusPurchase" :value="attribute">
                        {{ attribute }}
                      </option>
                    </select>
                  </td>
                  <td><input type="text" v-model="item.isbn"></td>
                  <td>{{ item.offer.name }}</td>
                  <td><input type="text" v-model="item.country"></td>
                  <td>{{ item.offer.product ? item.offer.product.country : "" }}</td>
                  <td>{{ item.offer.request.amount }}</td>
                  <td>{{ item.offer.article }}</td>
                  <td>{{ item.offer.product ? item.offer.product.name : "" }}</td>
                  <td>{{ item.offer.count }}</td>
                  <td>{{ item.offer.product ? item.offer.product.provider.name : "" }}</td>
                  <td><input type="number" min="0" step="any" v-model="item.price_buy"></td>
                  <td>{{ item.offer.request.amount * item.offer.count * item.price_buy }}</td>
                  <td>{{ item.offer.price }}</td>
                  <td>{{ item.offer.request.amount * item.offer.count * item.offer.price }}</td>
                  <td><input type="number" min="0" v-model="item.nds_base"></td>
                  <td><input type="number" min="0" v-model="item.nds_sell"></td>
                  <td>{{ 1 - item.price_buy / item.offer.price }}</td>
                  <td>{{ item.offer.request.amount * item.offer.count * (item.offer.price - item.price_buy) }}</td>
                  <td><input type="text" v-model="item.delivery_period"></td>
                  <td><input type="text" v-model="item.prepayment"></td>
                  <td><input type="text" v-model="item.bill_income"></td>
                  <td><input type="text" v-model="item.bill_income_complete"></td>
                  <td><input type="text" v-model="item.warehouse_delivery_date"></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useGuidePartnersStore } from '@/stores/guidePartners'
import { usePurchasesStore } from '@/stores/purchase'

export default {
  name: 'PurchaseForm',
  props: {
    purchase: {
      type: Object,
      required: true
    },
    project: {
      type: Object,
      required: true
    }
  },
  setup() {
    const guidePartnersStore = useGuidePartnersStore()
    const purchasesStore = usePurchasesStore()
    return { guidePartnersStore, purchasesStore }
  },
  data() {
    return {
      statusSelect: ['В работе', 'На согласовании', 'Согласована спека', 'Выдали ТЗ', 'Разместили аукцион', 'Закуп', 'Доставка', 'Оплатили', 'Закрыт', 'Не состоялся'],
      statusPurchase: ['Заказан', 'От поставщика', 'На складе', 'К заказчику', 'Отгружен']
    }
  },
  computed: {
    getDiscount() {
      if (typeof this.project.partner_id === 'number' && this.guidePartnersStore.data) {
        for (const object of this.guidePartnersStore.data.results) {
          if (object.id === this.project.partner_id) return object.discount
        }
      }
    },
  },
  methods:{
    onClickExportPurchases(){
      this.purchasesStore.exportPurchases(this.purchase.id)
    },

    ndsHandle(){
      if(this.project.nds){
        this.purchase.purchases.forEach(item => {
          item.nds_sell = item.nds_base
        })
      }
    }
  },
  created() {
    this.guidePartnersStore.getPartners()
    this.ndsHandle()
  },
}
</script>