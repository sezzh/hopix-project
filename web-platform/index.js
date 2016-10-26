const express = require('express')
const http = require('http')
const cookieParser = require('cookie-parser')
const csrf = require('csurf')
const bodyParser = require('body-parser')
const routerAdmin = require('./apps/admin/controllers')
const port = 3000

var app = express()

// Static folders.
app.use('/static', express.static(`${__dirname}/static`))
app.use('/public', express.static(`${__dirname}/public`))

// View engine.
app.set('view engine', 'pug')
app.set('views', './views')

// crsf protection.
app.use(bodyParser.json())
app.use(cookieParser())
app.use(csrf({ cookie: true }))

// Internal Routers.
app.use('/admin', routerAdmin)

const server = http.createServer(app)
server.listen(port, () => {
  console.log(`Express working on ${port}`)
})
