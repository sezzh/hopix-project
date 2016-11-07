const express = require('express')
const request = require('request')
const AUTHSERVICE_URI = 'http://authservice:5000/api/v1/users'
const STATUS_CODE_ERROR = 400
const STATUS_CODE_CREATED = 201
const STATUS_CODE_UNPROCESSABLE = 422
const STATUS_CODE_CONFLICT = 409

const users = express.Router()

users.post('/users', (req, res) => {
  var errorUserMessage = 'Ya parece haber una cuenta asociada a este mail :)'
  var errorGeneralMessage = 'Algo salio mal, prueba de nuevo más tarde D:'
  var statusCode = 0
  let opts = {
    method: 'POST',
    uri: AUTHSERVICE_URI,
    json: true,
    body: {
      sub: req.body.username,
      password: req.body.password
    }
  }

  new Promise((resolve, reject) => {
    request(opts, (err, response, body) => {
      if (!err) { statusCode = response.statusCode }
      if (err) { reject(err) }
      if (response.statusCode >= STATUS_CODE_ERROR) {
        reject(body.error)
      } else if (response.statusCode === STATUS_CODE_CREATED) {
        resolve(response.statusCode)
      }
    })
  }).then((response) => {
    res.status(STATUS_CODE_CREATED).json({ csrfToken: req.csrfToken() })
  }).catch((err) => {
    if (err) {
      if (statusCode === STATUS_CODE_CONFLICT) {
        res.status(statusCode).json({ error: errorUserMessage })
      } else if (statusCode >= STATUS_CODE_ERROR) {
        res.status(statusCode).json({ error: errorGeneralMessage })
      } else {
        res.status(STATUS_CODE_UNPROCESSABLE).json({
          error: errorGeneralMessage
        })
      }
    }
  })
})

module.exports = users
