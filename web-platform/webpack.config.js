const webpack = require('webpack')
const path = require('path')

var watcherOpts = {
  aggregateTimeout: 300,
  poll: true
}

var webpackOpts = {
  context: path.join(__dirname, 'lib', 'src'),
  // These are the apps from the template system.
  entry: {
    login: './login-app/index'
  },
  output: {
    path: path.join(__dirname, 'static', 'bin'),
    filename: '[name].bundle.js'
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false
      },
      output: {
        comments: false
      }
    })
  ]
}

var compiler = webpack(webpackOpts)

compiler.watch(watcherOpts, (err, stats) => {
  if (err) {
    console.error(err.message)
  } else {
    console.log('build done.')
  }
})
