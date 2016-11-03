import React from 'react'
import classNames from 'classnames'

export default class MenuNav extends React.Component {
  constructor () {
    super()
  }

  render () {
    let navClasses = classNames({
      'nav-menu': true,
      'nav-menu--hide': !this.props.menuState
    })
    let figureClasses = classNames('nav-menu__figure')
    let spanClasses = classNames('nav-menu__figure__icon', 'icon-face')
    let userDataClasses = classNames('nav-menu__user-data')
    let userNameClasses = classNames('nav-menu__user-data__username')
    let userTypeClasses = classNames('nav-menu__user-data__usertype')
    return (
      <nav className={navClasses}>
        <figure className={figureClasses}>
          <span className={spanClasses} />
        </figure>
        <div className={userDataClasses}>
          <h1 className={userNameClasses}>sezzh</h1>
          <h2 className={userTypeClasses}>superuser</h2>
        </div>
      </nav>
    )
  }
}
