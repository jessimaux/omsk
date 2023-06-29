import axios from '@/api/axios'

const login = (user) => {
  return axios.post('token/', user)
}

const getCurrentUser = () => {
  return axios.get('users/me/')
}

const refresh = (refresh_token) => {
  return axios.post('token/refresh/', { refresh: refresh_token })
}

export default {
  login,
  refresh,
  getCurrentUser
}
