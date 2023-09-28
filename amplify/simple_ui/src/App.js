import './App.css';
import { Amplify } from 'aws-amplify';
import { Footer } from './components/Footer';
import { Authenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';

import awsExports from './aws-exports';
Amplify.configure(awsExports);

export default function App() {
  return (
    <Authenticator>
      {({ signOut, user }) => (
        <main>
          <h1>Hello {user.username}</h1>
          <button onClick={signOut}>Sign out</button>
          <Footer />
        </main>
      )}
    </Authenticator>
  );
}