import React from 'react'
import classNames from 'classnames'
import AreaItem from './area-item.jsx'

export default class AreaList extends React.Component {
  constructor () {
    super()
  }

  render () {
    let sectionClasses = classNames('body', 'body--header-fixed')
    let listClasses = classNames('list')
    let areasItem = this.props.areas.map((area) => {
      return (
        <AreaItem key={area.id} id={area.id} name={area.name} />
      )
    })
    return (
      <section className={sectionClasses}>
        <ul className={listClasses}>
          {areasItem}
        </ul>
      </section>
    )
  }
}
