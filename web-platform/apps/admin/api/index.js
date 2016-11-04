const express = require('express')
const areas = require('apps/admin/api/areas')

const api = express.Router()

api.use(areas)

module.exports = api
