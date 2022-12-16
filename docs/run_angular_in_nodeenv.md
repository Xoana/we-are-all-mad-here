# Run an Angular Application in nodeenv

## Create Environment

1. ```$ python -m venv <venv_name>```
1. ```$ cd <venv_name>```
1. ```$ source ./Scripts/activate```
1. ```$ python -m pip install --upgrade pip```
1. Install dependencies for nodeenv: https://pypi.org/project/nodeenv/#local-installation
1. ```$ pip install nodeenv```
1. ```$ nodeenv -p``` 
    **Note**: To install a specific version: ```nodeenv -p --node=16.13.2```
    **Note**: Might receive error; see [Error: Failed to create nodejs.exe link](#error-failed-to-create-nodejsexe-link).
1. ```$ node -v```
1. ```$ npm i @angular/core```
1. ```$ ng version```
1. ```$ npm i @angular/cli```
1. ```$ npm i @angular/core```
1. ```cd <angular_project>```
    **Note**: If the project has already been installed, do a clean install as described in [Force a Clean Install](./angular_tips.md#force-a-clean-install).
1. ```npm install``` (or ```npm install --force``` if forcing a clean instal).

## Troubleshooting

### Error: Failed to create nodejs.exe link

Seems to work anyway...

https://issueantenna.com/repo/ekalinin/nodeenv/issues