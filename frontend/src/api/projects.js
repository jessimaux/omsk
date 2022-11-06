import axios from '@/api/axios'


const getProjects = () => {
  return axios.get('projects/')
}

const addProject = (project) => {
  return axios.post('projects/', project)
}

const addSpecification = (specification) => {
  return axios.post('specifications/specifications/', specification)
}

const addRequest = (request) => {
  return axios.post('specifications/requests/', request)
}

const addOffer = (offer) => {
  return axios.post('specifications/offers/', offer)
}

export default {
  getProjects,
  addProject,
  addSpecification,
  addOffer,
  addRequest
}