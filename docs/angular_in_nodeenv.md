# Angular Application in nodeenv


## Set Up Local Environment

1. Create and activate python venv.

1. pip install dependencies for nodeenv; see [Local Installation](https://pypi.org/project/nodeenv/#local-installation).

    **Note**: To install libssl-dev, ```pip install cryptography``` and ```pip install paramiko```.

1. Install nodeenv:
    ```
    (venv) $ pip install nodeenv
    (venv) $ nodeenv --version
    1.7.0
    ```

1. cd into python venv folder and add node virtual environment to the python venv:
    ```$ nodeenv -p --node=16.13.2```

    Reference: [Setting up a virtualenv with Node.js](https://nbdime.readthedocs.io/en/latest/nodevenv.html)

1. Check node versions in venv and outside of venv:
    ```$ node -v```

1. Install Angular Core and CLI:
    ```$ npm i @angular/cli```
    ```$ npm i @angular/core```

## Create an Angular Application

1. Create new sample application:
    ```ng new hello-world```
1. Build application:
    ```ng serve```
1. Confirm that it works by accessing localhost:4200.