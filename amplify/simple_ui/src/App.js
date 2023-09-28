import './App.css';
import * as React from 'react';
// import '@aws-amplify/ui-react/styles.css';
import { Amplify } from 'aws-amplify';
import { Authenticator, Tabs } from '@aws-amplify/ui-react';
import { Header } from './components/Header';
import { Home } from './components/Home'
import { Footer } from './components/Footer';
import awsExports from './aws-exports';
import { Contact } from './components/Contact'
import { TextSamples } from './components/TextSamples';
Amplify.configure(awsExports);

export default function App() {
  return ( 
    <Authenticator>
      {({ signOut, user }) => (
        <main>
          <Header />
          <Home />
          {/* <Contact /> */}
          {/* <TextSamples /> */}
          <button class='signout' onClick={signOut}>Sign out</button>
          <Footer />
        </main>
      )}
    </Authenticator>
  );
}