import React from 'react'
import ReactDOM from 'react-dom'
import Hello from './components/hello.jsx'

(function () {
  ReactDOM.render(<Hello />, document.querySelector('[data-react="dom"]'))
})()
