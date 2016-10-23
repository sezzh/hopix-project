const express = require('express')
const http = require('http')
const port = 3000
const routerAdmin = require('./apps/admin/controllers')
var app = express()

// Static folders.
app.use('/static', express.static(`${__dirname}/static`))
app.use('/public', express.static(`${__dirname}/public`))

// View engine.
app.set('view engine', 'pug')
app.set('views', './views')

// Routers.
app.use('/admin', routerAdmin)

const server = http.createServer(app)
server.listen(port, () => {
  console.log(`Express working on ${port}`)
})
