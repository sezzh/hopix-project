const LocalStrategy = require('passport-local').Strategy
const request = require('request')

const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQiLCJuYW1lIjoiSmVzdXMgQ3J1eiIsInVzZXJuYW1lIjoic2V6emgifQ.AZhSmvmV_zgdRNwfL-xUdBYm9OYeMwD6Cn2Nql736kc'

var localStrategy =
new LocalStrategy((username, password, done) => {
  let error = 'Algo salio absurdamente mal... trate de nuevo...'
  let loginOpts = {
    type: 'superuser',
    sub: username,
    password: password
  }
  request.post('http://authservice/auth/tokens', loginOpts, (err, response) => {
    if (err) {
      console.dir(err)
    } else {
      console.dir(response)
    }
  })
  if (username !== 'sezzh') {
    return done(null, false, { message: error })
  }
  if (password !== 'tifis') {
    return done(null, false, { message: error })
  }

  return done(null, { jwt: token })
})

module.exports.localStrategy = localStrategy
