import React from 'react';
import CustomSeparatorIconExample from './Breadcrumbs';
import { Authenticator } from '@aws-amplify/ui-react';

export const Header = () => {
  return (
      <div className="header-container">
        <nav className="nav" role="navigation">
          <div className="container nav-elements">
            <CustomSeparatorIconExample />
            {/* <div class='signout'>
                <Authenticator>
                    {({ signOut, user }) => (
                        <button onClick={signOut}>Sign out</button>
                    )}
                </Authenticator>     
            </div>        */}
          </div>
        </nav>
      </div>
  );
}
