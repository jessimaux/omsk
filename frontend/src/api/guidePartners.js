import axios from '@/api/axios'

const getPartners = (page, field, search) => {
  return axios.get('guide/partners/', {params: {page: page, ordering: field, search: search}})
}

const getFullPartners = () => {
  return axios.get('guide/partners/select/')
}

const exportPartners = () => {
  return axios.get('guide/partners/export/', { responseType: 'arraybuffer' })
}

const importPartners = (file) => {
  return axios.post('guide/partners/import/', file)
}

const getPartner = (id) => {
  return axios.get(`guide/partners/${id}/`)
}

const addPartner = (partner) => {
  return axios.post('guide/partners/', partner)
}

const editPartner = (id, partner) => {
  return axios.put(`guide/partners/${id}/`, partner)
}

const deletePartner = (id) => {
  return axios.delete(`guide/partners/${id}/`)
}

export default {
  getPartners,
  getFullPartners,
  exportPartners,
  importPartners,
  getPartner,
  addPartner,
  editPartner,
  deletePartner
}
