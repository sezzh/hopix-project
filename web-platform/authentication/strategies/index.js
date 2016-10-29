const LocalStrategy = require('passport-local').Strategy
const request = require('request')

var localStrategy =
new LocalStrategy((username, password, done) => {
  let authURI = 'http://authservice:5000/auth/tokens'
  let error = 'Algo salio absurdamente mal... trate de nuevo...'
  let loginOpts = {
    type: 'superuser',
    sub: username,
    password: password
  }
  let requestOpts = {
    uri: authURI,
    method: 'POST',
    body: loginOpts,
    json: true
  }
  // JWT request to auth service.
  request(requestOpts, (err, response) => {
    if (err || response.statusCode === 404 || response.statusCode === 403) {
      return done(null, false, { message: error })
    } else {
      return done(null, { jwt: response.body.token })
    }
  })
})

module.exports.localStrategy = localStrategy
