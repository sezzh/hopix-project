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
  })
})

areas.get('/areas/:areaId', (req, res) => {
  db.Area.find({ where: { id: req.params.areaId } }).then((area) => {
    res.status(200).json(area)
  })
})

areas.post('/areas', (req, res) => {
  db.Area.create({
    name: req.body.name,
    static_img: req.body.static_img
  }).then(() => {
    db.Area.findOrCreate({
      where: { name: req.body.name }
    }).spread((area, created) => {
      res.status(201).json(area.get({ plain: true }))
    })
  })
})

areas.put('/areas/:areaId', (req, res) => {
  db.Area.update(
    { name: req.body.name },
    { where: { id: req.params.areaId }, returning: true }
  ).then((result) => {
    if (result[0] === 0) {
      res.sendStatus(204)
    } else if (result[0] >= 1) {
      res.status(200).json(result[1])
    }
  })
})

areas.delete('/areas/:areaId', (req, res) => {
  db.Area.destroy({ where: { id: req.params.areaId } }).then((rows) => {
    if (rows === 0) {
      res.sendStatus(404)
    } else if (rows === 1) {
      res.sendStatus(200)
    }
  })
})

module.exports = areas
