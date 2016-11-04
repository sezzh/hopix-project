const express = require('express')
const request = require('request')

const areas = express.Router()

areas.get('/areas', (req, res) => {
  res.send('holi! :D')
})

module.exports = areas
