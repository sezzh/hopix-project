import React from 'react'
import classNames from 'classnames'

export default class Header extends React.Component {
  constructor () {
    super()
    this.handleAreaDetailState = this.handleAreaDetailState.bind(this)
    this.handleMenuState = this.handleMenuState.bind(this)
    this.saveArea = this.saveArea.bind(this)
  }

  handleAreaDetailState () {
    this.props.handleAreaDetailState()
    this.props.handleNavOptionsState()
  }

  handleMenuState () {
    this.props.handleMenuState()
  }

  saveArea (event) {
    this.props.handleSaveArea(event)
  }

  render () {
    let headerClasses = classNames(
      'header-admin', 'header-admin--justify-left', 'header-admin--fixed'
    )
    let menuBtnClasses = classNames('btn', 'btn--nav-menu')
    let figureClasses = classNames('header-admin__user-figure', 'u--hide')
    let imgClasses = classNames('header-admin__user-figure__img', 'icon-face')
    let h1Classes = classNames('header-admin__username')
    let h2Classes = classNames('header-admin__usertype')
    let userDataClasses = classNames('header-admin__user-data', 'u--hide')
    let optionsClasses = classNames({
      'header-admin__options': true,
      'u--hide': !this.props.navOptionsState
    })
    let btnHeaderClasses = classNames(
      'btn', 'btn--no-radius', 'btn--nav-option'
    )
    return (
      <header
        className={headerClasses}>
        <button className={menuBtnClasses} onClick={this.handleMenuState}>
          <span className='icon-menu' />
        </button>
        <figure className={figureClasses}>
          <span className={imgClasses} />
        </figure>
        <div className={userDataClasses}>
          <h1 className={h1Classes}>Administrador</h1>
          <h2 className={h2Classes}>superuser</h2>
        </div>
        <div className={optionsClasses}>
          <button
            className={btnHeaderClasses}
            onClick={this.handleAreaDetailState}>
            <span className='icon-arrow_back' />
          </button>
          <button className={btnHeaderClasses}>
            <span className='icon-undo' />
          </button>
          <button
            onClick={this.saveArea}
            className={btnHeaderClasses}>
            <span className='icon-done' />
          </button>
        </div>
      </header>
    )
  }
}
