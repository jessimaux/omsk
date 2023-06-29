import axios from '@/api/axios'

const getUsers = (page, field, search) => {
  return axios.get('users/', {params: {page: page, ordering: field, search: search}})
}

const getUser = (id) => {
  return axios.get(`users/${id}/`)
}

const editUser = (id, user_data) => {
  return axios.put(`users/${id}/`, user_data)
}

const createUser = (user) => {
  return axios.post('users/', user)
}

const deleteUser = (id) => {
  return axios.delete(`users/${id}`)
}

export default {
  getUsers,
  getUser,
  createUser,
  editUser,
  deleteUser
}