import { withAuthenticationRequired } from "@auth0/auth0-react";
import React from "react";
import Loader from "./components/Loader";

export const ProtectedRoute = ({ component }) => {
  const Component = withAuthenticationRequired(component, {
    onRedirecting: () => <Loader class="lds-ring"/>,
  });

  return <Component />
}