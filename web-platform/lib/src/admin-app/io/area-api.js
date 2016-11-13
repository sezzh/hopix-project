import axios from 'axios'
import Area from '../models/area.js'

export default class AreaApi {
  constructor () {
    this.csrfUri = `${window.location.origin}/admin/csrf`
    this.resName = 'areas'
    this.resUri = `${window.location.origin}/admin/api/${this.resName}`
  }

  getCsrfToken () {
    return axios.get(this.csrfUri).then((response) => {
      return Promise.resolve(response.data.csrfToken)
    })
  }

  get (id = null) {
    if (id) {

    } else {
      return axios.get(this.resUri).then((response) => {
        let areas = response.data.map((obj) => {
          let area = new Area()
          area.name = obj.name
          area.id = obj.id
          area.createdAt = obj.createdAt
          area.updatedAt = obj.updatedAt
          return area
        })
        return Promise.resolve(areas)
      })
    }
  }

  post (area) {
    return this.getCsrfToken().then((token) => {
      let body = { name: area.name, _csrf: token }
      return axios.post(this.resUri, body).then((response) => {
        if (response.status === 201) {
          return Promise.resolve(response.data)
        }
      })
    })
  }

}
