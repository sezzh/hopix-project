import axios from 'axios'
import cssclass from 'cssclass'
import validate from 'validate.js'

(function () {
  var btnOpenLogin = document.querySelector('[data-login-form="open-btn"]')
  var registryForm = document.querySelector('[data-registry="form"]')
  var loginForm = document.querySelector('[data-login="form"]')

  btnOpenLogin.addEventListener('click', () => {
    if (loginForm.hasClass('floating-login--hide')) {
      loginForm.removeClass('floating-login--hide')
    } else {
      loginForm.addClass('floating-login--hide')
    }
  })

  registryForm.addEventListener('submit', (event) => {
    let emailError = 'No parece un email valido D:'
    let passwordError = 'las contraseñas no parecen coincidir...'
    let data = {}
    event.preventDefault()

    let passConstraints = {
      confirmPassword: {
        equality: {
          attribute: 'password'
        }
      }
    }

    let emailConstraints = {
      from: {
        email: true
      }
    }

    let email =
      registryForm.querySelector('[data-registry="data-email"]').value
    let password =
      registryForm.querySelector('[data-registry="data-password"]').value
    let passwordR =
      registryForm.querySelector('[data-registry="data-password-r"]').value

    // Validators
    let passValidation = validate({
      password: password, confirmPassword: passwordR
    }, passConstraints)
    let emailValidation = validate({ from: email }, emailConstraints)
    if (emailValidation) {
      displayError(emailError)
    } else if (passValidation) {
      displayError(passwordError)
    } else {
      data.username = email
      data.password = password
      data._csrf =
        registryForm.querySelector('[data-registry="data-token"]').value
      createAccount(data)
    }
  })

  function createAccount (data) {
    axios.post(registryForm.action, data).then((response) => {
      if (response.status === 201) {
        let loginOpts = {
          username: data.username,
          password: data.password,
          _csrf: response.data.csrfToken
        }
        return axios.post('/login', loginOpts)
      }
    }).then((response) => {
      if (response.data === 'done') {
        window.location.assign('/')
      }
    }).catch((error) => {
      displayError(error)
    })
  }

  function login () {

  }

  function displayError (message) {
    let errorSpan = registryForm.querySelector('[data-registry="message"]')
    errorSpan.innerHTML = message
    if (errorSpan.hasClass('section-login__form__message-error--hide')) {
      errorSpan.removeClass('section-login__form__message-error--hide')
    }
  }
})()
