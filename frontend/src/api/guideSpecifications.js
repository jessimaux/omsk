import axios from '@/api/axios'

const getSpecifications = (page, field, search) => {
  return axios.get('guide/specifications/', {params: {page: page, ordering: field, search: search}})
}

const getFullSpecifications = () => {
  return axios.get('guide/specifications/select')
}

const getSpecification = (id) => {
  return axios.get(`guide/specifications/${id}/`)
}

const addSpecification = (specification) => {
  return axios.post('guide/specifications/', specification)
}

const editSpecification = (id, specification) => {
  return axios.put(`guide/specifications/${id}/`, specification)
}

const deleteSpecification = (id) => {
  return axios.delete(`guide/specifications/${id}/`)
}

export default {
  getSpecifications,
  getFullSpecifications,
  getSpecification,
  addSpecification,
  editSpecification,
  deleteSpecification
}
