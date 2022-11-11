import axios from '@/api/axios'

const getPartners = () => {
  return axios.get('guide/partners/')
}

const getProducts = () => {
  return axios.get('guide/products/')
}

const exportProducts = () => {
  return axios.get('guide/products/export/', { responseType: 'arraybuffer' })
}

const importProducts = (file) => {
  return axios.post('guide/products/import/', file)
}

const getProduct = (id) => {
  return axios.get(`guide/products/${id}/`)
}

const addProduct = (product) => {
  return axios.post('guide/products/', product)
}

const editProduct = (id, product) => {
  return axios.put(`guide/products/${id}/`, product)
}

const deleteProduct = (id) => {
  return axios.delete(`guide/products/${id}/`)
}

const getProviders = () => {
  return axios.get('guide/providers/')
}

const getSpecifications = () => {
  return axios.get('guide/specifications/')
}

export default {
  getPartners,
  getProducts,
  exportProducts,
  importProducts,
  getProduct,
  addProduct,
  editProduct,
  deleteProduct,
  getProviders,
  getSpecifications,
}
