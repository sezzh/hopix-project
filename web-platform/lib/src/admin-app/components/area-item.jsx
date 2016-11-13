import React from 'react'
import classNames from 'classnames'

export default class AreaItem extends React.Component {
  constructor () {
    super()
  }

  render () {
    let itemClasses = classNames('area-item')
    let figureClasses = classNames('area-item__figure')
    let imgClasses = classNames('area-item__figure__img')
    let nameClasses = classNames('area-item__name')
    return (
      <li data-id={this.props.id} className={itemClasses}>
        <figure className={figureClasses}>
          <img className={imgClasses} />
        </figure>
        <h3 className={nameClasses}>
          {this.props.name}
        </h3>
      </li>
    )
  }
}
