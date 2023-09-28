import React from 'react';
import { Heading } from '@aws-amplify/ui-react';
import { TextSamples } from './TextSamples';
import { Text } from '@aws-amplify/ui-react';
import { ContactData, PlaceholderText } from './shared/config';

export const Contact = () => {
    const title = ContactData.title;
    const description = PlaceholderText.paragraph;

    return (
      <div className="body-container">
        <Heading level={1}>{ title }</Heading>
        <Text>{ description }</Text>
      </div>
  );
}
