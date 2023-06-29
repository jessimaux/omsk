import axios from '@/api/axios'

const getLogs = (page, field, search) => {
  return axios.get('logs/', {params: {page: page, ordering: field, search: search}})
}

export default {
  getLogs
}
