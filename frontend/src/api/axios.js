import axios from 'axios'
import {getCookie} from '@/tools/persistanceStorage'

axios.defaults.baseURL = import.meta.env.VITE_BASEURL

axios.interceptors.request.use((config) => {
  const token = getCookie('access')
  const authorizationToken = token ? `Bearer ${token}` : ''
  config.headers.Authorization = authorizationToken
  return config
})

export default axios