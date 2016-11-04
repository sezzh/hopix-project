const express = require('express')
const admin = require('apps/admin')
const hopix = require('apps/hopix')

const apps = express.Router()

apps.use(hopix)
apps.use('/admin', admin)

module.exports = apps
