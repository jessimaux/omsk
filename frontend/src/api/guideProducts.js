import axios from '@/api/axios'

const searchProducts = (query) => {
  return axios.get('guide/products-search/', {params: {search: query}})
}

const getProducts = (query) => {
  return axios.get('guide/products/', {params: {search: query}})
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


export default {
  searchProducts,
  getProducts,
  exportProducts,
  importProducts,
  getProduct,
  addProduct,
  editProduct,
  deleteProduct,
}
