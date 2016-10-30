const http = require('http')
const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')
const port = process.env.CORE_PORT || 3000
const Sequelize = require('sequelize')

// Web server initialize.
const app = express()
const server = http.createServer(app)

// Parsers.
app.use(bodyParser.json())

const sequelizeOpts = {
  host: process.env.CORE_DB_HOST_SECRET,
  dialect: process.env.CORE_DB_TECNOLOGY,
  pool: {
    max: 5,
    min: 0,
    idle: 10000
  }
}

const sequelize = new Sequelize(
  process.env.CORE_DB_NAME_SECRET,
  process.env.CORE_DB_USERNAME_SECRET,
  process.env.CORE_DB_PASSWORD_SECRET,
  sequelizeOpts
)

var User = sequelize.define('user', {
  firstName: {
    type: Sequelize.STRING
  },
  lastName: {
    type: Sequelize.STRING
  }
})

User.sync({ force: true }).then(() => {
  return User.create({
    firstName: 'Jesus',
    lastName: 'Cruz'
  })
})

app.get('/', (req, res) => {
  User.findAll().then((users) => {
    res.send(users)
  })
})

server.listen(port, () => {
  console.log(`Express working on ${port}`)
})
