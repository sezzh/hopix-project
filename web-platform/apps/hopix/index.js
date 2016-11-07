const express = require('express')
const passport = require('passport')
const api = require('apps/hopix/api')
const ensureAuthUser = require('authentication/middlewares').ensureAuthUser

const hopix = express.Router()

hopix.get('/', ensureAuthUser, (req, res) => {
  res.send('estas logueado')
})

hopix.get('/login', (req, res) => {
  let welcomeMessage = 'Conocimiento, entrenamiento y experiencia, ' +
  'todo en un solo lugar.'
  if (req.flash().error) {
    res.status(401).json(req.flash())
  } else {
    res.render(
      'hopix/register',
      { welcomeMessage: welcomeMessage, csrfToken: req.csrfToken() }
    )
  }
})

hopix.post('/login',
passport.authenticate('local',
  { failureRedirect: '/login', failureFlash: true }),
(req, res) => {
  if (req.xhr) {
    res.sendStatus(200)
  } else {
    res.redirect('/')
  }
})

hopix.use('/web/api', api)

module.exports = hopix
