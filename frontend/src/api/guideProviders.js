import axios from '@/api/axios'

const getProviders = (page, field, search) => {
  return axios.get('guide/providers/', {params: {page: page, ordering: field, search: search}})
}

const getFullProviders = () => {
  return axios.get('guide/providers/select/')
}

const exportProviders = () => {
  return axios.get('guide/providers/export/', { responseType: 'arraybuffer' })
}

const importProviders = (file) => {
  return axios.post('guide/providers/import/', file)
}

const getProvider = (id) => {
  return axios.get(`guide/providers/${id}/`)
}

const addProvider = (provider) => {
  return axios.post('guide/providers/', provider)
}

const editProvider = (id, provider) => {
  return axios.put(`guide/providers/${id}/`, provider)
}

const deleteProvider = (id) => {
  return axios.delete(`guide/providers/${id}/`)
}



export default {
  getProviders,
  getFullProviders,
  getProvider,
  exportProviders,
  importProviders,
  addProvider,
  editProvider,
  deleteProvider
}
