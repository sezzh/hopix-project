import React from 'react'
import classNames from 'classnames'
import Area from '../models/area.js'

export default class ClassName extends React.Component {
  constructor () {
    super()
    this.handleNameChange = this.handleNameChange.bind(this)
    this.state = {
      name: ''
    }
    this.area = new Area()
  }

  handleNameChange (event) {
    this.setState({ name: event.target.value })
    this.area.name = event.target.value
    this.props.handleCreateArea(this.area)
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
        <input
          type='text'
          placeholder='Nombre del area'
          value={this.state.name}
          onChange={this.handleNameChange}
          className={nameClasses} />
      </section>
    )
  }
}
