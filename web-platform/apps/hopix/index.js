const express = require('express')
const passport = require('passport')
const ensureAuthUser = require('authentication/middlewares').ensureAuthUser

const hopix = express.Router()

hopix.get('/', ensureAuthUser, (req, res) => {

})

hopix.get('/login', (req, res) => {
  let welcomeMessage = 'Conocimiento, entrenamiento y experiencia, ' +
  'todo en un solo lugar.'

  if (req.flash().error) {

  } else {
    res.render('hopix/register', { welcomeMessage: welcomeMessage })
  }
})

hopix.post('/login',
passport.authenticate('local',
  { failureRedirect: '/login', failureFlash: true }),
(req, res) => {

})

module.exports = hopix
