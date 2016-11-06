const express = require('express')
const request = require('request')
const AUTHSERVICE_URI = 'http://authservice:5000/api/v1/users'

const users = express.Router()

users.post('/users', (req, res) => {
  let statusCode = 0
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
      if (err || response.statusCode >= 400) {
        statusCode = response.statusCode
        reject(err || body)
      }
      if (response.statusCode === 201) {
        resolve(response.statusCode)
      }
    })
  }).then((data) => {
    res.status(201).json({ csrfToken: req.csrfToken() })
  }).catch((err) => {
    if (err) {
      if (statusCode === 409) {
        res.sendStatus(statusCode)
      } else {
        res.status(statusCode).json(err)
      }
    }
  })
})

module.exports = users
