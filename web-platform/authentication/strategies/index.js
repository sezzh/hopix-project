const LocalStrategy = require('passport-local').Strategy
const request = require('request')
const AUTH_URI = 'http://authservice:5000/auth/tokens'
const STATUS_CODE_ERROR = 400
const STATUS_CODE_GONE = 410
const STATUS_CODE_CONFLICT = 409

var opts = {
  passReqToCallback: true
}

var ls = new LocalStrategy(opts, (req, username, password, done) => {
  let error = 'Algo salio absurdamente mal... trate de nuevo...'
  let userError = 'Parece que no hay una cuenta asociada...'
  let passError = 'Puede que tu contraseña este mal!'
  let loginOpts = {
    sub: username,
    password: password
  }

  if (req.originalUrl === '/admin/login') {
    loginOpts.type = 'superuser'
  }

  let requestOpts = {
    uri: AUTH_URI,
    method: 'POST',
    body: loginOpts,
    json: true
  }

  // JWT request to auth service.
  request(requestOpts, (err, response) => {
    if (err) {
      return done(err)
    } else if (response.statusCode === STATUS_CODE_CONFLICT) {
      return done(null, false, { message: passError })
    } else if (response.statusCode === STATUS_CODE_GONE) {
      return done(null, false, { message: userError })
    } else if (response.statusCode >= STATUS_CODE_ERROR) {
      return done(null, false, { message: error })
    } else if (response.body.token) {
      return done(null, { jwt: response.body.token })
    }
  })
})

module.exports.localStrategy = ls
