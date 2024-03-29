import axios from '@/api/axios'

const searchProducts = (query) => {
  return axios.get('guide/products/search/', {params: {search: query}})
}

const getProducts = (page, field, search) => {
  return axios.get('guide/products/', {params: {page: page, ordering: field, search: search}})
}

const exportProducts = () => {
  return axios.get('guide/products/export_xlsx/', { responseType: 'arraybuffer' })
}

const importProducts = (file) => {
  return axios.post('guide/products/import_xlsx/', file)
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
