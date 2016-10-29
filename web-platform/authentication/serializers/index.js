const jwt = require('jsonwebtoken')
const secret = process.env.WEBPLATFORM_JWT_SECRET

module.exports.serializeUser = (user, done) => done(null, user)

module.exports.deserializeUser = (user, done) => {
  jwt.verify(user.jwt, secret, (err, decoded) => {
    if (err) {
      done(err)
    }
    done(null, decoded)
  })
}
