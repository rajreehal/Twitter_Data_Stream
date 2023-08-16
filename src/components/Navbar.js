import React, {useState, useEffect} from 'react';
import * as FaIcons from "react-icons/fa";
import { Link } from 'react-router-dom'
import { NavbarData } from './NavbarData'
import LoginButton from './LoginButton';
import LogoutButton from './LogoutButton';
import './Navbar.css';
import { IconContext } from 'react-icons/lib';

function Navbar(props) {
    const [sidebar, setSidebar] = useState(false)
    const showSidebar = () => setSidebar(!sidebar)

    const collapse = props.onCollapse

    useEffect(() => {
        collapse(sidebar)
    }, [sidebar, collapse])

    return (
        <>
        <IconContext.Provider value={{color: '#fff'}}>
        <div className='navbar'>
            <Link to="#" className='menu-bars-closed'>
                <FaIcons.FaBars onClick={showSidebar} color='#4c4c4c'/>
            </Link>
            <div className="navbar-right">
                <LogoutButton />
            </div>
        </div>
        <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
            <ul className='nav-menu-items'>
                <li className='navbar-toggle'>
                    <Link to='#' className='menu-bars'>
                        <FaIcons.FaBars onClick={showSidebar} />
                    </Link>
                </li>
                {NavbarData.map((item, index) => {
                    return (
                        <li key={index} className={item.cName}>
                            <Link to={item.path}>
                                {item.icon}
                                <span>{item.title}</span>
                            </Link>
                        </li>
                    )
                })}
            </ul>
        </nav>
        </IconContext.Provider>
        </>
    )
}

export default Navbar