<template>
  <div class="card">
    <div class="card-header">
      <h5 class="card-title">Проект</h5>
    </div>
    <div class="card-body">
      <form class="row g-3" @submit.prevent="onSubmit">
        <div class="col-12">
          <label class="form-label">Название проекта</label>
          <input
            type="text"
            class="form-control"
            v-model="initialValues.name"
          />
        </div>

        <div class="col-12">
          <label class="form-label">Статус проекта</label>
          <select class="form-select" v-model="project.status">
            <option v-for="attribute in statusSelect" :value="attribute">
              {{ attribute }}
            </option>
          </select>
        </div>

        <div class="col-12">
          <label class="form-label">Наименование учреждения</label>
          <input
            type="text"
            class="form-control"
            v-model="project.company_name"
          />
        </div>

        <div class="col-12">
          <label class="form-label">ИНН</label>
          <input
            type="text"
            class="form-control"
            v-model="project.company_inn"
          />
        </div>

        <div class="col-12">
          <label class="form-label">Город</label>
          <input
            type="text"
            class="form-control"
            v-model="project.company_city"
          />
        </div>

        <div class="col-12">
          <label class="form-label">Область</label>
          <input
            type="text"
            class="form-control"
            v-model="project.company_region"
          />
        </div>

        <div class="col-12">
          <label class="form-label">Партнер</label>
          <select class="form-select" v-model="project.partner">
            <option
              v-for="partner in partners"
              :key="partner.id"
              :value="partner.id"
            >
              {{ partner.name }}
            </option>
          </select>
        </div>

        <div class="col-12">
          <label class="form-label">Номер регистрации проекта</label>
          <input type="text" class="form-control" v-model="project.reg_no" />
        </div>

        <div class="col-12">
          <label class="form-label">Количество детей в классе</label>
          <input
            type="text"
            class="form-control"
            v-model="project.company_children"
          />
        </div>

        <div class="col-12">
          <label class="form-label">Скидка</label>
          <input
            type="text"
            class="form-control"
            :value="getDiscount"
            disabled
          />
        </div>

        <div class="col-12">
          <label class="form-label">НДС</label>
          <input type="text" class="form-control" v-model="project.nds" />
        </div>

        <!-- <div class="col-12">
          <label class="form-label">Типовая спецификация</label>
          <input type="text" class="form-control">
        </div> -->

        <div class="col-12">
          <label class="form-label">Срок поставки</label>
          <input
            type="text"
            class="form-control"
            v-model="project.delivery_period"
          />
        </div>

        <div class="col-12">
          <legend class="col-form-label">Наличие договора</legend>
          <div class="form-check">
            <input
              type="checkbox"
              class="form-check-input"
              v-model="project.contract"
            />
          </div>
        </div>

        <div class="col-12">
          <label class="form-label">Комментарий</label>
          <textarea
            class="form-control"
            v-model="project.commentary"
          ></textarea>
        </div>

        <div class="col-12">
          <legend class="col-form-label">
            Опции формирования файла клиента
          </legend>
          <div class="col-sm-10">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" />
              <label class="form-check-label">
                Добавить "Строка по приказу"
              </label>
            </div>

            <div class="form-check">
              <input class="form-check-input" type="checkbox" />
              <label class="form-check-label"> Добавить "Ссылка" </label>
            </div>

            <div class="form-check">
              <input class="form-check-input" type="checkbox" />
              <label class="form-check-label">
                Добавить "Страна производства"
              </label>
            </div>

            <div class="form-check">
              <input class="form-check-input" type="checkbox" />
              <label class="form-check-label"> Добавить "Описание" </label>
            </div>

            <div class="form-check">
              <input class="form-check-input" type="checkbox" />
              <label class="form-check-label">
                Добавить "Техническое описание"
              </label>
            </div>

            <div class="form-check">
              <input class="form-check-input" type="checkbox" />
              <label class="form-check-label"> Добавить "Заявка" </label>
            </div>
          </div>
        </div>

        <!-- dynamic table -->
        <div class="table-responsive">
          <table class="table">
            <thead>
              <tr>
                <th scope="col" colspan="7" class="text-center">Запрос</th>
                <th scope="col" colspan="6" class="text-center">Предложение</th>
              </tr>
              <tr>
                <th scope="col"></th>
                <th scope="col">#</th>
                <th scope="col">Приказ</th>
                <th scope="col">Наименование</th>
                <th scope="col">ТХ</th>
                <th scope="col">Количество</th>
                <th scope="col">Цена</th>
                <th scope="col">Сумма</th>
                <th scope="col">Артикул</th>
                <th scope="col">Наименование</th>
                <th scope="col">Количество</th>
                <th scope="col">Цена</th>
                <th scope="col">Сумма</th>
                <th scope="col">Наличие</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody v-for="(row, index) in requestOffer" :key="`row-${index}`">
              <tr>
                <td :rowspan="requestOffer[index].offer.length">
                  <i
                    @click="addRow(requestOffer)"
                    class="bi bi-plus-square"
                  ></i>
                  <i
                    v-show="requestOffer.length > 1"
                    @click="removeRow(index, requestOffer)"
                    class="bi bi-dash-square"
                  ></i>
                </td>
                <td :rowspan="requestOffer[index].offer.length">{{ index }}</td>
                <td :rowspan="requestOffer[index].offer.length">
                  <input
                    type="text"
                    v-model="requestOffer[index].str_by_order"
                  />
                </td>
                <td :rowspan="requestOffer[index].offer.length">
                  <input type="text" v-model="requestOffer[index].name" />
                </td>
                <td :rowspan="requestOffer[index].offer.length">
                  <input type="text" v-model="requestOffer[index].tx" />
                </td>
                <td :rowspan="requestOffer[index].offer.length">
                  <input type="text" v-model="requestOffer[index].amount" />
                </td>
                <td :rowspan="requestOffer[index].offer.length">
                  <input type="text" v-model="requestOffer[index].price" />
                </td>
                <td :rowspan="requestOffer[index].offer.length">
                  {{ requestOffer[index].price * requestOffer[index].amount }}
                </td>
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[0].article"
                  />
                </td>
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[0].name"
                  />
                </td>
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[0].count"
                  />
                </td>
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[0].price"
                  />
                </td>
                <td>
                  {{
                    requestOffer[index].offer[0].count *
                    requestOffer[index].offer[0].price
                  }}
                </td>
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[0].available"
                  />
                </td>
                <td>
                  <i
                    @click="addSubRow(requestOffer[index].offer)"
                    class="bi bi-plus-square"
                  ></i>
                  <i
                    v-show="requestOffer[index].offer.length > 1"
                    @click="removeSubRow(0, requestOffer[index].offer)"
                    class="bi bi-dash-square"
                  ></i>
                </td>
              </tr>
              <tr
                v-if="requestOffer[index].offer.length > 1"
                v-for="(subrow, subindex) in row.offer.slice(
                  1,
                  row.offer.length
                )"
                :key="`subrow-${subindex}`"
              >
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[subindex + 1].article"
                  />
                </td>
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[subindex + 1].name"
                  />
                </td>
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[subindex + 1].count"
                  />
                </td>
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[subindex + 1].price"
                  />
                </td>
                <td>
                  {{
                    requestOffer[index].offer[subindex + 1].count *
                    requestOffer[index].offer[subindex + 1].price
                  }}
                </td>
                <td>
                  <input
                    type="text"
                    v-model="requestOffer[index].offer[subindex + 1].available"
                  />
                </td>
                <td>
                  <i
                    @click="addSubRow(requestOffer[index].offer)"
                    class="bi bi-plus-square"
                  ></i>
                  <i
                    v-show="requestOffer[index].offer.length > 1"
                    @click="
                      removeSubRow(subindex + 1, requestOffer[index].offer)
                    "
                    class="bi bi-dash-square"
                  ></i>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="text-center">
          <button type="submit" class="btn btn-primary">Сохранить</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { useGuideStore } from '@/stores/guide.js'

export default {
  name: 'projectForm',
  props: {
    initialValues: {
      type: Object,
      required: true,
    },
  },
  setup() {
    const guideStore = useGuideStore()
    return { guideStore }
  },
  data() {
    return {
      project: {
        name: this.initialValues.name,
        status: this.initialValues.status,
        company_name: this.initialValues.company_name,
        company_inn: this.initialValues.company_inn,
        company_city: this.initialValues.company_city,
        company_region: this.initialValues.company_region,
        company_children: this.initialValues.company_children,
        reg_no: this.initialValues.reg_no,
        nds: this.initialValues.nds,
        partner: this.initialValues.partner,
        delivery_period: this.initialValues.delivery_period,
        contract: this.initialValues.contract,
        commentary: this.initialValues.commentary,
      },
      partners: [],
      statusSelect: [
        'В работе',
        'На согласовании',
        'Согласована спека',
        'Выдали ТЗ',
        'Разместили аукцион',
        'Закуп',
        'Доставка',
        'Оплатили',
        'Закрыт',
        'Не состоялся',
      ],
      requestOffer: [
        {
          str_by_order: '',
          name: '',
          tx: '',
          amount: '',
          price: '',
          offer: [
            {
              article: '',
              name: '',
              count: '',
              price: '',
              available: '',
            },
          ],
        },
      ],
    }
  },
  computed: {
    getDiscount() {
      if (typeof this.project.partner === 'number') {
        return this.partners[this.project.partner - 1].discount
      }
    },
  },
  methods: {
    onSubmit() {
      const form = { project: this.project, requestOffer: this.requestOffer }
      this.$emit('projectSubmit', form)
    },

    addRow(fieldType) {
      fieldType.push({
        str_by_order: '',
        name: '',
        tx: '',
        amount: '',
        price: '',
        total: '',
        specification: '',
        offer: [
          {
            article: '',
            name: '',
            count: '',
            price: '',
            total: '',
            available: '',
          },
        ],
      })
    },

    removeRow(index, fieldType) {
      fieldType.splice(index, 1)
    },

    addSubRow(fieldType) {
      fieldType.push({
        article: '',
        name: '',
        count: '',
        price: '',
        total: '',
        available: '',
      })
    },

    removeSubRow(index, fieldType) {
      fieldType.splice(index, 1)
    },
  },
  created() {
    this.guideStore.getPartners().then(() => {
      this.partners = this.guideStore.data
    })
  },
}
</script>
