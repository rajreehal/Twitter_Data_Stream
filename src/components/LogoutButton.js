import { useAuth0 } from "@auth0/auth0-react";
import React from 'react'

const LogoutButton = () => {
  const { logout, isAuthenticated } = useAuth0();

  return (
    isAuthenticated && (
    <button className="authentication-button" onClick={() => 
      window.location.href = 'http://localhost:3000/api/logout'}>
        Sign out
    </button>
    )
  )
}

export default LogoutButton