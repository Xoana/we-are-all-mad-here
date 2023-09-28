import React from 'react';
import { Heading } from '@aws-amplify/ui-react';
// import { TextSamples } from './TextSamples';
// import { AlertSamples } from './AlertSamples';
import { Text } from '@aws-amplify/ui-react';
import { HomeData, PlaceholderText } from './shared/config';

export const Home = () => {
  const title = HomeData.title;
  const description = PlaceholderText.paragraph;

  return (
      <div className="body-container">
        <Heading level={1}>{ title }</Heading>
        <Text>{ description }</Text>
      </div>
  );
}
