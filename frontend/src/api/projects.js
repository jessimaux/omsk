import axios from '@/api/axios'

// PROJECTS

const getProjects = (page, field, search) => {
  return axios.get('projects/', {params: {page: page, ordering: field, search: search}})
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

const patchProject = (id, project) => {
  return axios.patch(`projects/${id}/`, project)
}

const deleteProject = (id) => {
  return axios.delete(`projects/${id}/`)
}

const fileUploadProject = (files) => {
  return axios.post('projects/files/', files)
}

// SPECIFICATIONS

const exportSpecification = (id, params) => {
  return axios.get(`specifications/${id}/report_xlsx/`, {params: params, responseType: 'arraybuffer' })
}

// REGISTRATION FORM

const exportRegistrationForm = (id) => {
  return axios.get(`projects/${id}/report_registration/`, {responseType: 'arraybuffer' })
}

export default {
  getProjects,
  getProject,
  editProject,
  patchProject,
  addProject,
  deleteProject,
  fileUploadProject,
  exportSpecification,
  exportRegistrationForm,
}