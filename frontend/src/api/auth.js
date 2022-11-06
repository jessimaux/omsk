import axios from '@/api/axios'


const login = (user) => {
  return axios.post('auth/token/login/', user)
}

const logout = () => {
  return axios.post('auth/token/logout/')
}

const getCurrentUser = () => {
  return axios.get('auth/users/me/')
}

export default {
  login,
  logout,
  getCurrentUser,
}