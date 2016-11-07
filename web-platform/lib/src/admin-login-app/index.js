import axios from 'axios'

(function () {
  const STATUS_CODE_OK = 200
  var form = document.querySelector('[data-login="form"]')

  form.addEventListener('submit', (event) => {
    event.preventDefault()
    let data = {
      username: '',
      password: '',
      _csrf: ''
    }
    let target = event.target
    let error = 'No puedes dejar nada vacio D:'
    for (let i = 0; i < target.length; i++) {
      for (let j = 0; j < target[i].attributes.length; j++) {
        if (target[i].attributes[j].value === 'data-username') {
          if (target[i].value === '') {
            displayError(error)
          } else {
            data.username = target[i].value
          }
        } else if (target[i].attributes[j].value === 'data-password') {
          if (target[i].value === '') {
            displayError(error)
          } else {
            data.password = target[i].value
          }
        } else if (target[i].attributes[j].value === 'data-token') {
          data._csrf = target[i].value
        }
      }
    }
    if (data.username !== '' && data.password !== '') sendRequest(data)
  })

  function displayError (message) {
    let helperClass = 'u--margin-bottom'
    let helperOn = false
    let messageContainer = form.querySelector('[data-login="message"]')
    messageContainer.classList.forEach((cssClass) => {
      (cssClass === helperClass) ? helperOn = true : helperOn = false
    })
    if (!helperOn) {
      messageContainer.className += '  ' + helperClass
    }
    messageContainer.innerHTML = message
  }

  function sendRequest (data) {
    axios.post('/admin/login', data).then((response) => {
      if (response.status === STATUS_CODE_OK) {
        window.location.assign('/admin')
      }
    }).catch((error) => {
      displayError(error.response.data.error)
    })
  }
})()
