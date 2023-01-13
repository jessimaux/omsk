import axios from 'axios'
import { getItem } from '@/tools/persistanceStorage'

axios.defaults.baseURL = import.meta.env.VITE_BASEURL

// middleware: add auth header
axios.interceptors.request.use((config) => {
  const token = getItem('accessToken')
  const authorizationToken = token ? `Token ${token}` : ''
  config.headers.Authorization = authorizationToken
  return config
})

// middleware: remove token when 401
axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      localStorage.removeItem('accessToken')
    }
  }
  return Promise.reject(error)
})


export default axios