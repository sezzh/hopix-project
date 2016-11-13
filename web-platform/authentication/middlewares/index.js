/*
 * Middleware encargado de saber si el usuario esta logueado en "/admin"
 * y además es superuser.
 */
module.exports.ensureAuthAdmin = function (req, res, next) {
  if (req.isAuthenticated() && req.user.type === 'superuser') {
    return next()
  } else {
    res.redirect('/admin/login')
  }
}

/*
 * Middleware que permite proteger los recursos que se piden vía restful.
 */
module.exports.ensureIsSuperUser = function (req, res, next) {
  if (req.isAuthenticated() && req.user.type === 'superuser') {
    return next()
  } else {
    res.sendStatus(403)
  }
}

/*
 * Middleware que permite saber si un user esta autenticado.
 */
module.exports.ensureAuthUser = function (req, res, next) {
  if (req.isAuthenticated()) {
    return next()
  } else {
    res.redirect('/login')
  }
}
