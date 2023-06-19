import axios from '@/api/axios'

const getSpecifications = (page, field, search) => {
  return axios.get('specifications/', {params: {page: page, ordering: field, search: search}})
}

const getFullSpecifications = () => {
  return axios.get('specifications/select/')
}

const getSpecification = (id) => {
  return axios.get(`specifications/${id}/`)
}

const addSpecification = (specification) => {
  return axios.post('specifications/', specification)
}

const editSpecification = (id, specification) => {
  return axios.put(`specifications/${id}/`, specification)
}

const deleteSpecification = (id) => {
  return axios.delete(`specifications/${id}/`)
}

export default {
  getSpecifications,
  getFullSpecifications,
  getSpecification,
  addSpecification,
  editSpecification,
  deleteSpecification
}
