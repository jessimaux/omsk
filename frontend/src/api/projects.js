import axios from '@/api/axios'

// PROJECTS

const getProjects = () => {
  return axios.get('projects/')
}

const getProject = (id) => {
  return axios.get(`projects/${id}/`)
}

const addProject = (project) => {
  return axios.post('projects/', project)
}

const editProject = (id, project) => {
  return axios.put(`projects/${id}/`, project)
}

const deleteProject = (id) => {
  return axios.delete(`projects/${id}/`)
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
  return axios.get(`specifications/requests/${id}/`)
}

const addRequest = (request) => {
  return axios.post('specifications/requests/', request)
}

const editRequest = (id, request) => {
  return axios.put(`specifications/requests/${id}/`, request)
}

const deleteRequest = (id) => {
  return axios.delete(`specifications/requests/${id}/`)
}

// OFFER

const getOffers = () => {
  return axios.get('specifications/offers/')
}

const getOffer = (id) => {
  return axios.get(`specifications/offers/${id}/`)
}

const addOffer = (offer) => {
  return axios.post('specifications/offers/', offer)
}

const editOffer = (id, offer) => {
  return axios.put(`specifications/offers/${id}/`, offer)
}

const deleteOffer = (id) => {
  return axios.delete(`specifications/offers/${id}/`)
}

export default {
  getProjects,
  getProject,
  editProject,
  addProject,
  deleteProject,
  addSpecification,
  getOffers,
  getOffer,
  addOffer,
  editOffer,
  deleteOffer,
  getRequests,
  getRequest,
  addRequest,
  editRequest,
  deleteRequest,
}