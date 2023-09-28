import React from 'react';
import CustomSeparatorIconExample from './Breadcrumbs';
import BasicTabs from './Tabs'
export const Header = () => {
  return (
      <div className="header-container">
        <nav className="nav" role="navigation">
          <div className="container nav-elements">
            {/* <CustomSeparatorIconExample /> */}
            <BasicTabs />

          </div>
        </nav>
      </div>
  );
}
