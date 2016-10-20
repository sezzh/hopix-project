const express = require('express')
const http = require('http')
var request = require('request')

var app = express()

app.get('/', (req, res) => {
  res.send('Hello world')
})

app.get('/test', (req, res) => {
  request('http://authservice:5000/test', (error, response, body) => {
    if (!error && response.statusCode === 200) {
      res.send(body)
    }
  })
})

const server = http.createServer(app)
server.listen(3000, () => {
  console.log('Example app')
})
