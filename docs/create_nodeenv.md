# How to create a node virtual environment

1. Create a python virtual environment: ```$ python -m venv <venv_name>```
1. Navigate into the python virtual environment directory: ```$ cd <venv_name>```
1. Activate the python virutal environment: ```$ source ./Scripts/activate```
1. If necessary, upgrade pip: ```$ python -m pip install --upgrade pip```
1. Install dependencies for nodeenv; see [Node.js virtual environment > Local Installation](https://pypi.org/project/nodeenv/#local-installation). Currently, pip install make, tail, and libssl-dev.
1. Install nodenv: ```$ pip install nodeenv```
1. Associate nodenv with the python venv: ```$ nodeenv -p``` 

    **Notes**:
    * To install a specific version: ```nodeenv -p --node=16.13.2```
    * If `nodeenv -p` returns error stating there is no venv, ensure you are inside the venv, and rerun the `source` command.
    * See [Error: Failed to create nodejs.exe link](#error-failed-to-create-nodejsexe-link).

1. Check node version:  ```$ node -v```