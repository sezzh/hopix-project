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
    'admin/login'
  )
})

module.exports = router
