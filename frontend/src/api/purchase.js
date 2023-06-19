import axios from '@/api/axios'

const getPurchase = (id) => {
  return axios.get(`purchases/${id}/`)
}

const editPurchase = (id, purchase) => {
  return axios.put(`purchases/${id}/`, purchase)
}

const exportPurchases = (id) => {
  return axios.get(`purchases/${id}/export_xlsx/`, {responseType: 'arraybuffer' })
}

export default {
  getPurchase,
  editPurchase,
  exportPurchases,
}