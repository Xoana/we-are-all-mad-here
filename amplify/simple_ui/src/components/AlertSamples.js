import { Heading, Alert } from '@aws-amplify/ui-react';

export const AlertSamples = () => {
  return (
    <>
    <Heading level={1}>Alert Samples</Heading>
      <Alert variation='info' heading='Info'>Information alert.</Alert>
      <Alert variation='error' heading='Error'>Add error details here.</Alert>
      <Alert variation='warning' heading='Warning'>Add warning details here.</Alert>
      <Alert variation='success' heading='Success'>Add success message here.</Alert>
      <Alert>Default</Alert>
    </>
  );
};