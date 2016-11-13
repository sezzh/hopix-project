import React from 'react'
import classNames from 'classnames'
import Hammer from 'react-hammerjs'
import Header from './header.jsx'
import MenuNav from './menu-nav.jsx'
import AreaList from './area-list.jsx'
import AreaDetail from './area-detail.jsx'
import Area from '../models/area.js'
import AreaApi from '../io/area-api.js'

export default class App extends React.Component {
  constructor () {
    super()
    this.handleMenuState = this.handleMenuState.bind(this)
    this.handleAreaDetailState = this.handleAreaDetailState.bind(this)
    this.handleNavOptionsState = this.handleNavOptionsState.bind(this)
    this.handleCreateState = this.handleCreateState.bind(this)
    this.handleSaveArea = this.handleSaveArea.bind(this)
    this.refreshList = this.refreshList.bind(this)
    this.handleCreateArea = this.handleCreateArea.bind(this)
    this.areaApi = new AreaApi()
    this.area = new Area()
    this.state = {
      areaDetailState: false,
      navOptionsState: false,
      menuState: false,
      areas: []
    }
  }

  componentWillMount () {

  }

  componentDidMount () {
    this.refreshList()
  }

  handleSaveArea (event) {
    this.areaApi.post(this.area).then((area) => {
      if (area) { return this.areaApi.get() }
    }).then((areas) => {
      this.setState({ areas: areas })
      this.handleAreaDetailState()
      this.handleNavOptionsState()
    })
  }

  handleCreateArea (area) {
    this.area = area
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

  refreshList () {
    this.areaApi.get().then((areas) => {
      this.setState({ areas: areas })
    })
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
          handleNavOptionsState={this.handleNavOptionsState}
          handleSaveArea={this.handleSaveArea} />
        <Hammer onSwipe={this.handleMenuState} direction='DIRECTION_LEFT'>
          <MenuNav menuState={this.state.menuState} />
        </Hammer>
        <AreaList areas={this.state.areas} />
        <button
          className={btnPlusClasses}
          onClick={this.handleCreateState}>
          <span className={spanClasses} />
        </button>
        <AreaDetail
          handleCreateArea={this.handleCreateArea}
          areaDetailState={this.state.areaDetailState} />
      </section>
    )
  }
}
