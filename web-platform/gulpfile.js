const gulp = require('gulp')
const webpack = require('webpack-stream')

gulp.task('default', () => {
  return gulp.src('lib/src')
  .pipe(webpack(require('webpack.config.js')))
  .pipe(gulp.dest('static/bin/'))
})
