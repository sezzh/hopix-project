const express = require('express')
const users = require('apps/hopix/api/users')

const api = express.Router()

api.use(users)

module.exports = api
