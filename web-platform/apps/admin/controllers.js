const express = require('express')
const passport = require('passport')

var router = express.Router()

var passportOpt = {
  successRedirect: '/',
  failureRedirect: '/login',
  failureFlash: true
}

router.get('/', (req, res) => {
  res.render(
    'admin/hello',
    {
      title: 'titulo',
      contenido: 'holii',
      img: {
        bebish: 'enla ventana'
      }
    }
  )
})

router.get('/login', (req, res) => {
  res.render(
    'admin/login',
    {
      csrfToken: req.csrfToken()
    }
  )
})

router.post('/login',
passport.authenticate('local', passportOpt),
(req, res) => {
  console.dir(req.body)
  res.send('okis')
})

module.exports = router
