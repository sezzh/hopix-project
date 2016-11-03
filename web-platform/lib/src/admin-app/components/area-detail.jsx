import React from 'react'
import classNames from 'classnames'

export default class ClassName extends React.Component {
  constructor () {
    super()
  }

  render () {
    let sectionClasses = classNames({
      'area-detail': true,
      'area-detail--hide': !this.props.areaDetailState
    })
    let figureClasses = classNames('area-detail__figure')
    let nameClasses = classNames('area-detail__name', 'input-border-bottom')
    let imgClasses = classNames('area-detail__figure__img')
    return (
      <section className={sectionClasses}>
        <figure className={figureClasses}>
          <img className={imgClasses} />
        </figure>
        <input value='Programación' className={nameClasses} />
      </section>
    )
  }
}
