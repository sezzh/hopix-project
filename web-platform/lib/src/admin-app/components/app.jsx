import React from 'react'
import classNames from 'classnames'
import Hammer from 'react-hammerjs'
import Header from './header.jsx'
import MenuNav from './menu-nav.jsx'
import AreaList from './area-list.jsx'
import AreaDetail from './area-detail.jsx'

export default class App extends React.Component {
  constructor () {
    super()
    this.handleMenuState = this.handleMenuState.bind(this)
    this.handleAreaDetailState = this.handleAreaDetailState.bind(this)
    this.handleNavOptionsState = this.handleNavOptionsState.bind(this)
    this.handleCreateState = this.handleCreateState.bind(this)
    this.state = {
      areaDetailState: false,
      navOptionsState: false,
      menuState: false
    }
  }

  handleCreateState () {
    this.handleAreaDetailState()
    this.handleNavOptionsState()
  }

  handleMenuState () {
    if (this.state.menuState) {
      this.setState({ menuState: false })
    } else {
      this.setState({ menuState: true })
    }
  }

  handleNavOptionsState () {
    if (this.state.navOptionsState) {
      this.setState({ navOptionsState: false })
    } else {
      this.setState({ navOptionsState: true })
    }
  }

  handleAreaDetailState () {
    if (this.state.areaDetailState) {
      this.setState({ areaDetailState: false })
    } else {
      this.setState({ areaDetailState: true })
    }
  }

  render () {
    let sectionClasses = classNames('body-app')
    let btnPlusClasses = classNames('btn-round', 'btn-round--fixed')
    let spanClasses = classNames('btn-round__icon', 'icon-add')
    return (
      <section className={sectionClasses}>
        <Header
          handleAreaDetailState={this.handleAreaDetailState}
          navOptionsState={this.state.navOptionsState}
          handleMenuState={this.handleMenuState}
          handleNavOptionsState={this.handleNavOptionsState} />
        <Hammer onSwipe={this.handleMenuState} direction='DIRECTION_LEFT'>
          <MenuNav menuState={this.state.menuState} />
        </Hammer>
        <AreaList />
        <button
          className={btnPlusClasses}
          onClick={this.handleCreateState}>
          <span className={spanClasses} />
        </button>
        <AreaDetail areaDetailState={this.state.areaDetailState} />
      </section>
    )
  }
}
