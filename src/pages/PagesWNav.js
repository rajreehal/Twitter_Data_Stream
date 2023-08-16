import React from "react";
import { useState } from 'react';
import Navbar from "../components/Navbar";
import { Outlet } from 'react-router'

export default () => {
    const [status, setStatus] = useState(true)
    return (
      <>
        <Navbar onCollapse={(status) => {
                setStatus(status)
              }}/>
        <div className={!status ? 'container-screenshift-navbar-closed':'container-screenshift-navbar'}>
            <Outlet />
        </div>
      </>
    );
  };