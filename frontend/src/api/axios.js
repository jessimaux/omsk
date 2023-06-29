import axios from 'axios'
import {getCookie} from '@/tools/persistanceStorage'

axios.defaults.baseURL = 'http://127.0.0.1:8000/api'

axios.interceptors.request.use((config) => {
  const token = getCookie('access')
  const authorizationToken = token ? `Bearer ${token}` : ''
  config.headers.Authorization = authorizationToken
  return config
})

export default axios