import React from 'react';
import { Heading } from '@aws-amplify/ui-react';
import { Text } from '@aws-amplify/ui-react';
import { AlertSamples } from './AlertSamples';
export const TextSamples = () => {
  return (
    <div className="body-container">
      <Heading level={1}>Text Samples</Heading>
      <Heading level={2}>Truncated Text</Heading>
        <Text isTruncated={true}>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea cupidatat
            non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </Text>
        <Heading level={2}>Text Types</Heading>
        <Text variation="primary">Primary</Text>
        <Text variation="secondary">Secondary</Text>
        <Text variation="tertiary">Tertiary</Text>
        <Text variation="error">Error</Text>
        <Text variation="warning">Warning</Text>
        <Text variation="info">Info</Text>
        <Text variation="success">Success</Text>
        <Text>Default</Text>    
        <AlertSamples />    
      </div>
  );
}
