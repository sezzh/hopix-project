const express = require('express')
const request = require('request')
const CORE_URI = 'http://core:3000/api/v1/areas'
const STATUS_CODE_ERROR_NOT_FOND = 404
const STATUS_CODE_ERROR_GONE = 410
const STATUS_CODE_CREATED = 201
const STATUS_CODE_OK = 200
const STATUS_CODE_NO_CONTENT = 204
const STATUS_CODE_INTERNAL_ERROR = 500

const areas = express.Router()

areas.get('/areas', (req, res) => {
  let errorMessage = 'Parece ser que hay algo mal con los datos :('
  let opts = {
    uri: CORE_URI,
    method: 'GET'
  }
  request(opts, (error, response, body) => {
    if (error) {
      res.status(STATUS_CODE_ERROR_NOT_FOND).json({ error: errorMessage })
    } else {
      (response.statusCode === STATUS_CODE_OK)
        ? res.send(body)
        : res.status(STATUS_CODE_ERROR_NOT_FOND).json({ error: errorMessage })
    }
  })
})

areas.get('/areas/:areaId', (req, res) => {
  let errorMessage = 'Esta area parece que ya no esta disponible'
  let opts = {
    uri: `${CORE_URI}/${req.params.areaId}`,
    method: 'GET'
  }
  request(opts, (error, response, body) => {
    if (error) {
      res.status(STATUS_CODE_ERROR_GONE).json({ error: errorMessage })
    }
    (response.statusCode === STATUS_CODE_OK)
      ? res.send(body)
      : res.status(STATUS_CODE_ERROR_GONE).json({ error: errorMessage })
  })
})

areas.post('/areas', (req, res) => {
  let errorMessage = 'algo salio mal, intenta de nuevo más tarde D:'
  let body = {
    name: req.body.name
  }
  let opts = {
    uri: CORE_URI,
    method: 'POST',
    json: true,
    body: body
  }
  request(opts, (error, response, body) => {
    if (error) {
      res.status(STATUS_CODE_ERROR_NOT_FOND).json({ error: errorMessage })
    } else {
      if (response.statusCode === STATUS_CODE_CREATED) {
        res.status(STATUS_CODE_CREATED).json({ id: body.id, name: body.name })
      } else {
        res.status(STATUS_CODE_ERROR_NOT_FOND).json({ error: errorMessage })
      }
    }
  })
})

areas.put('/areas/:areaId', (req, res) => {
  let errorMessage = 'algo salio mal... Intenta de nuevo'
  let body = {
    name: req.body.name
  }
  let opts = {
    uri: `${CORE_URI}/${req.params.areaId}`,
    method: 'PUT',
    json: true,
    body: body
  }
  request(opts, (error, response, body) => {
    if (error) {
      res.status(STATUS_CODE_INTERNAL_ERROR).json({ error: errorMessage })
    }
    (response.statusCode === STATUS_CODE_OK)
      ? res.json(body)
      : res.status(STATUS_CODE_ERROR_GONE).json({ error: errorMessage })
  })
})

areas.delete('/areas/:areaId', (req, res) => {
  let errorMessage = 'algo salio mal... Intenta de nuevo'
  let opts = {
    uri: `${CORE_URI}/${req.params.areaId}`,
    method: 'DELETE',
    json: true
  }
  request(opts, (error, response, body) => {
    if (error) {
      res.status(STATUS_CODE_INTERNAL_ERROR).json({ error: errorMessage })
    }
    (response.statusCode === STATUS_CODE_NO_CONTENT)
      ? res.sendStatus(STATUS_CODE_NO_CONTENT)
      : res.status(STATUS_CODE_ERROR_GONE).json({ error: body.error.resource })
  })
})

module.exports = areas
