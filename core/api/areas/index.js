const express = require('express')
const db = require('models')

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
      res.status(500).end()
    }
  })
})

areas.get('/areas/:areaId', (req, res) => {
  db.Area.findOne({ where: { id: req.params.areaId } }).then((area) => {
    (area !== null) ? res.status(200).json(area) : res.status(404).end()
  }).catch((err) => {
    if (err) {
      res.status(500).end()
    }
  })
})

areas.post('/areas', (req, res) => {
  db.sequelize.authenticate().then(() => {
    db.Area.findOrCreate({
      where: { name: req.body.name }
    }).spread((area, created) => {
      if (created) {
        res.status(201).json(area.get({ plain: true }))
      } else {
        res.status(409).end()
      }
    }).catch((errors) => {
      if (errors) {
        res.status(422).end()
      }
    })
  }).catch((err) => {
    if (err) {
      res.status(500).end()
    }
  })
})

areas.put('/areas/:areaId', (req, res) => {
  db.sequelize.authenticate().then(() => {
    db.Area.update(
      { name: req.body.name },
      { where: { id: req.params.areaId }, returning: true }
    ).then((result) => {
      (result[0] === 0) ? res.status(404).end() : res.status(200).json(result[1])
    }).catch((errors) => {
      if (errors) {
        res.status(422).end()
      }
    })
  }).catch((err) => {
    if (err) {
      res.status(500).end()
    }
  })
})

areas.delete('/areas/:areaId', (req, res) => {
  db.sequelize.authenticate().then(() => {
    db.Area.destroy({ where: { id: req.params.areaId } }).then((rows) => {
      (rows === 0) ? res.status(404).end() : res.status(204).end()
    })
  }).catch((err) => {
    if (err) {
      res.status(500).end()
    }
  })
})

module.exports = areas
