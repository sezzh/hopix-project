const express = require('express')
const http = require('http')
const cookieParser = require('cookie-parser')
const csrf = require('csurf')
const bodyParser = require('body-parser')
const routerAdmin = require('./apps/admin/controllers')
const port = 3000
const passport = require('passport')
const LocalStrategy = require('passport-local').Strategy

var user = { username: 'sezzh', password: 'tifis', id: 4 }

var app = express()

app.get('/', (req, res) => {
  res.send('holi')
})

// Static folders.
app.use('/static', express.static(`${__dirname}/static`))
app.use('/public', express.static(`${__dirname}/public`))

// View engine.
app.set('view engine', 'pug')
app.set('views', './views')

// crsf protection.
app.use(cookieParser())
app.use(bodyParser.json())
app.use(csrf({ cookie: true }))
app.use(passport.initialize())

// Passport test
passport.use(new LocalStrategy((username, password, done) => {
  if (!username === 'sezzh') {
    return done(null, false, { message: 'incorrect username.' })
  }
  if (!password === 'tifis') {
    return done(null, false, { message: 'Incorrect password' })
  }

  return done(null, user)
}))

// Internal Routers.
app.use('/admin', routerAdmin)

const server = http.createServer(app)
server.listen(port, () => {
  console.log(`Express working on ${port}`)
})
