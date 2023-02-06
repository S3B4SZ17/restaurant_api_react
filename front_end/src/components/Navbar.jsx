import React, { useState } from 'react';
import {
  MDBNavbar,
  MDBContainer,
  MDBNavbarBrand,
  MDBIcon,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBNavbarLink,
  MDBNavbarToggler,
  MDBCollapse
} from 'mdb-react-ui-kit';
import axios from "axios";
import Image from 'react-bootstrap/Image'

import { MDBDropdown, MDBDropdownMenu, MDBDropdownToggle, MDBDropdownItem } from 'mdb-react-ui-kit';


export default function Navbar() {
  const [showNavText, setShowNavText] = useState(false);
  const [isAuthenticated] = useState(localStorage.getItem("isAuthenticated"));
  const [email, setEmail] = useState(localStorage.getItem("user_email"));
  const [profilePicture, setProfilePicture] = useState(localStorage.getItem("profile_pic"));

  const instance = axios.create({
    baseURL: "http://localhost:8080",
  });

  // Catch the AunAuthorized Request
  
  instance.interceptors.response.use((response) => response, (error) => {
      if (error.response.status === 401) {
        localStorage.clear();
        window.location = '/login';
      }
    });

  return (
    <MDBNavbar expand='lg' dark bgColor='dark'>
      <MDBContainer fluid>
        <MDBNavbarBrand href='/'>My restaurant</MDBNavbarBrand>
        <MDBNavbarToggler
          type='button'
          data-target='#navbarText'
          aria-controls='navbarText'
          aria-expanded='false'
          aria-label='Toggle navigation'
          onClick={() => setShowNavText(!showNavText)}
        >
          <MDBIcon icon='bars' fas />
        </MDBNavbarToggler>
        <MDBCollapse navbar show={showNavText}>
          <MDBNavbarNav className='mr-auto mb-2 mb-lg-0'>
            <MDBNavbarItem>
              <MDBNavbarLink active aria-current='page' href='/'>
                Home
              </MDBNavbarLink>
            </MDBNavbarItem>
          </MDBNavbarNav>
          
        </MDBCollapse>
      </MDBContainer>
    </MDBNavbar>
  );
}
