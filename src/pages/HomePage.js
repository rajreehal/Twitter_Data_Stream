import React from 'react'
import { Link } from 'react-scroll';
import LoginButton from '../components/LoginButton';
import './HomePage.css';

const HomePage = () => {

  return (
    <div>
        <header className="nav-homepage">
          <nav className="nav__container__actions">
            <ul className="ul-homepage">
              <li className="">
                <Link activeClass="active" smooth spy to="gossip">
                  Gossip
                </Link>
              </li>
              <li>
                <Link activeClass="active" smooth spy to="features">
                  Features
                </Link>
              </li>
              <li>
                <Link activeClass="active" smooth spy to="about">
                  About
                </Link>
              </li>
            </ul>
          </nav>
          <div className="nav-homepage-login-button">
            <LoginButton />
          </div>
          <button className="contact-sales">
              Contact sales
          </button>
        </header>
        <section id="gossip">
          <div className="hp-gossip-left">
            <h1>Real-time targeted social media opportunities for you to engage.</h1>
          </div>
          <div className="hp-gossip-right">
            
          </div>
        </section>
        <section id="features">
          <div className="hp-features">
            <h1>Real-time tweet streams</h1>
          </div>
        </section>
          
        <section id="about">About</section>
    </div>
  )
}

export default HomePage;