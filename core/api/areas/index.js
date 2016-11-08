const express = require('express')
const db = require('models')
const error500 = {error: {BD: 'Sin conexión.'}}
const error410 = {error: {recurso: 'El recurso solicitado no existe.'}}
var areas = express.Router()

areas.get('/areas', (req, res) => {
  let data = []
  db.Area.findAll().then((areas) => {
    areas.forEach((area) => {
      data.push(area.dataValues)
    })
    res.status(200).json(data)
  }).catch((err) => {
    if (err) {
      res.status(500).json(error500)
    }
  })
})

areas.get('/areas/:areaId', (req, res) => {
  db.Area.findOne({ where: { id: req.params.areaId } }).then((area) => {
    (area !== null)
    ? res.status(200).json(area)
    : res.status(410).json(error410)
  }).catch((err) => {
    if (err) {
      res.status(500).json(error500)
    }
  })
})

areas.post('/areas', (req, res) => {
  db.sequelize.authenticate().then(() => {
    db.Area.findOrCreate({
      where: { name: req.body.name }
    }).spread((area, created) => {
      (created)
      ? res.status(201).json(area.get({ plain: true }))
      : res.status(409).json({error: {recurso: 'El recurso ya existe'}})
    }).catch((err) => {
      if (err) {
        var error = {}
        for (var i in err.errors) {
          if (err.errors[i].path === 'name') {
            error = {name: err.errors[i].message}
          }
        }
        res.status(422).json({error: error})
      }
    })
  }).catch((err) => {
    if (err) {
      res.status(500).json(error500)
    }
  })
})

areas.put('/areas/:areaId', (req, res) => {
  db.sequelize.authenticate().then(() => {
    db.Area.update(
      { name: req.body.name },
      { where: { id: req.params.areaId }, returning: true }
    ).then((result) => {
      (result[0] === 0)
      ? res.status(410).json(error410)
      : res.status(200).json(result[1][0])
    }).catch((err) => {
      if (err) {
        var error = {}
        for (var i in err.errors) {
          if (err.errors[i].path === 'name') {
            error = {name: err.errors[i].message}
          }
        }
        res.status(422).json({error: error})
      }
    })
  }).catch((err) => {
    if (err) {
      res.status(500).json(error500)
    }
  })
})

areas.delete('/areas/:areaId', (req, res) => {
  db.sequelize.authenticate().then(() => {
    db.Area.destroy({ where: { id: req.params.areaId } }).then((rows) => {
      (rows === 0) ? res.status(410).json(error410) : res.status(204).end()
    })
  }).catch((err) => {
    if (err) {
      res.status(500).json(error500)
    }
  })
})

module.exports = areas
