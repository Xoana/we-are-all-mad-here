# React on AWS Amplify

## Installation and Configuration

1. Create venv; see [Run an Angular Application in nodeenv](../docs/run_angular_in_nodeenv.md) in this repo.
1. Install Node.js.
1. Install and configure Amplify CLI globally; refer to  [Installation](https://docs.amplify.aws/cli/start/install/).
1. Create React app: `npx create-react-app simple_ui`
1. Initialize amplify: `amplify init`
1. Install `ui-react`: `npm install aws-amplify @aws-amplify/ui-react`
1. Add the following to your index.js file:
    ```
    import {Amplify} from 'aws-amplify';
    import awsconfig from './aws-exports';

    Amplify.configure(awsconfig);
    ```
1. Add Amplify [Authenticator](https://ui.docs.amplify.aws/react/connected-components/authenticator).

    **Note**: *aws-exports.js* contains config details, which should match the user pool on AWS Cognito Management Console.

1. Run app and create a new user in log in box. 

    **Note** User will be added to AWS Cognito Management Console. If user is created in AWS Management Console, ensure forced password reset is used.

## Hosting



## AWS CLI - Additional Commands

* `amplify status`: Display what you've added already and if it's locally configured or deployed.
* `amplify add <category>`: Add features like user login or a backend API.
* `amplify push`: Build all your local backend resources and provision in the cloud.
* `amplify console`: Open the Amplify Console and view your project status.
* `amplify publish`: Build all your local backend and frontend resources (if you have hosting category added) and provision in the cloud.
* `amplify add api`: Create a backend API. 
    
    **Note**: Use `amplify push` to deploy the API.

## Further Reading
* [Amplify Dev Center](https://ui.docs.amplify.aws/)
* [React.dev](https://react.dev/)