import axios from '@/api/axios'

const getSpecifications = () => {
  return axios.get('guide/specifications/')
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
  getSpecification,
  addSpecification,
  editSpecification,
  deleteSpecification
}
