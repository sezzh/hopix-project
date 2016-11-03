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
    return (
      <section className={sectionClasses}>
        <ul className={listClasses}>
          <AreaItem />
          <AreaItem />
          <AreaItem />
          <AreaItem />
          <AreaItem />
          <AreaItem />
          <AreaItem />
          <AreaItem />
          <AreaItem />
          <AreaItem />
          <AreaItem />
        </ul>
      </section>
    )
  }
}
