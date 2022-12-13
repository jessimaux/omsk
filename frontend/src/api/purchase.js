import axios from '@/api/axios'

const getPurchase = (id) => {
  return axios.get(`purchases/${id}/`)
}

const editPurchase = (id, purchase) => {
  return axios.put(`purchases/${id}/`, purchase)
}

export default {
  getPurchase,
  editPurchase
}