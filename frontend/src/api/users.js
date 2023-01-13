import axios from '@/api/axios'

const getUsers = () => {
  return axios.get('auth/users/')
}

const createUser = (user) => {
  return axios.post('auth/users/', user)
}

export default {
  getUsers,
  createUser,
}