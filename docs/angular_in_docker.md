# Run Angular Application in Docker

## Set Up Local Environment

1. Create and activate python venv.
1. pip install nodeenv
    ```
    (venv) $ pip install nodeenv
    (venv) $ nodeenv --version
    1.7.0
    ```

1. pip install dependencies for nodeenv; see [Local Installation](https://pypi.org/project/nodeenv/#local-installation).
1. cd into python venv folder and add node virtual environment to the python venv:
    ```$ nodeenv -p```
    Reference: [Setting up a virtualenv with Node.js](https://nbdime.readthedocs.io/en/latest/nodevenv.html)
1. Check node versions in venv and outside of venv:
    ```$ node -v```
    **Local**: 
    ```
    $ node -v
    v19.2.0
    ```
    **Global**: 
    ```
    $ node -v
    v14.16.1
    ```
1. Install Angular Core and CLI:
    ```$ npm i @angular/cli```
    ```$ npm i @angular/core```

## Create an Angular Application

1. Create new sample application:
    ```ng new hello-world```
1. Build application:
    ```ng serve```
1. Confirm that it works by accessing localhost:4200.

## Build and Run Dockerfile
1. Create Dockerfile; see [Dockerfile](../angular_docker/Dockerfile)
1. Build Dockerfile: 
   ```$ docker build -t angular_in_docker .```
1. Run container:
    ```$ docker run --name angular_in_docker_container -d -p 8080:80 angular_in_docker```
1. Access app on localhost:8080.