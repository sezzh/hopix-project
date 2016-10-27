const http = require('http')
const path = require('path')
const express = require('express')
const expressSession = require('express-session')
const cookieParser = require('cookie-parser')
const bodyParser = require('body-parser')
const csrf = require('csurf')
const flash = require('req-flash')
const passport = require('passport')
const localStrategy = require('authentication/strategies').localStrategy
const routerAdmin = require('apps/admin/controllers')
const serializers = require('authentication/serializers')
const port = process.env.WEBPLATFORM_PORT || 3000

// Web server initialize.
const app = express()
const server = http.createServer(app)

// Express Sessions configuration.
var esOpts = {
  secret: process.env.WEBPLATFORM_SESSION_SECRET,
  resave: false,
  saveUninitialized: false
}

// Static folders.
app.use('/static', express.static(path.join(__dirname, 'static')))
app.use('/public', express.static(path.join(__dirname, 'public')))

// View engine.
app.set('view engine', 'pug')
app.set('views', './views')

// Parsers.
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(cookieParser())

// crsf protection.
app.use(csrf({ cookie: true }))

// Passport config
app.use(expressSession(esOpts))
app.use(flash())
app.use(passport.initialize())
app.use(passport.session())
passport.use(localStrategy)
passport.serializeUser(serializers.serializeUser)
passport.deserializeUser(serializers.deserializeUser)

// Internal Routers.
app.use('/admin', routerAdmin)

server.listen(port, () => {
  console.log(`Express working on ${port}`)
})
