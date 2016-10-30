const http = require('http')
const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')
const port = process.env.CORE_PORT || 3000

// Web server initialize.
const app = express()
const server = http.createServer(app)

// Parsers.
app.use(bodyParser.json())

app.get('/', (req, res) => {
  res.send('hello world! :D')
})

server.listen(port, () => {
  console.log(`Express working on ${port}`)
})
