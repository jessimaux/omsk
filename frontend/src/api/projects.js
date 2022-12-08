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

const exportSpecification = (id, params) => {
  return axios.get(`specifications/${id}/export/`, {params: params, responseType: 'arraybuffer' })
}

export default {
  getProjects,
  getProject,
  editProject,
  addProject,
  deleteProject,
  exportSpecification,
}