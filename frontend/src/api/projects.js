import axios from '@/api/axios'

// PROJECTS

const getProjects = () => {
  return axios.get('projects/')
}

const getProject = (id) => {
  return axios.get(`projects/${id}`)
}

const addProject = (project) => {
  return axios.post('projects/', project)
}

const editProject = (id, project) => {
  return axios.put(`projects/${id}/`, project)
}

// SPECIFICATIONS

const addSpecification = (specification) => {
  return axios.post('specifications/specifications/', specification)
}

// REQUEST

const getRequests = () => {
  return axios.get('specifications/requests/')
}

const getRequest = (id) => {
  return axios.get(`specifications/requests/${id}`)
}

const addRequest = (request) => {
  return axios.post('specifications/requests/', request)
}

const editRequest = (id, request) => {
  return axios.put(`specifications/requests/${id}`, request)
}

// OFFER

const getOffers = () => {
  return axios.get('specifications/offers/')
}

const getOffer = (id) => {
  return axios.get(`specifications/offers/${id}`)
}

const addOffer = (offer) => {
  return axios.post('specifications/offers/', offer)
}

const editOffer = (id, offer) => {
  return axios.post(`specifications/offer/${id}`, offer)
}

export default {
  getProjects,
  getProject,
  editProject,
  addProject,
  addSpecification,
  getOffers,
  getOffer,
  addOffer,
  editOffer,
  getRequests,
  getRequest,
  addRequest,
  editRequest
}