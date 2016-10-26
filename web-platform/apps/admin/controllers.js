const express = require('express')

var router = express.Router()

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

router.post('/login', (req, res) => {
  console.dir(req.body)
  res.send('okis')
})

module.exports = router
