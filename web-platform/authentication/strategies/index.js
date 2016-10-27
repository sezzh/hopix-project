const LocalStrategy = require('passport-local').Strategy

const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQiLCJuYW1lIjoiSmVzdXMgQ3J1eiIsInVzZXJuYW1lIjoic2V6emgifQ.AZhSmvmV_zgdRNwfL-xUdBYm9OYeMwD6Cn2Nql736kc'

var localOpts = {}

var localStrategy =
new LocalStrategy(localOpts, (username, password, done) => {
  var error = 'Algo salio absurdamente mal... trate de nuevo...'
  if (username !== 'sezzh') {
    return done(null, false, { message: error })
  }
  if (password !== 'tifis') {
    return done(null, false, { message: error })
  }

  return done(null, { jwt: token })
})

module.exports.localStrategy = localStrategy
