import React from 'react';
import '@aws-amplify/ui-react/styles.css';

export const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <nav className="nav" role="navigation">
          <div className="container nav-elements">
            {/* <ul className="navbar">
              <li><a href="#home">home</a></li>
              <li><a href="#history">history</a></li>
              <li><a href="#products">products</a></li>
              <li><a href="#guarantee">guarantee</a></li>
              <li><a href="#people">people</a></li>
            </ul> */}
          </div>
        </nav>
        <p className="legal">Copyright 2023</p>
      </div>
    </footer>
  );
}
