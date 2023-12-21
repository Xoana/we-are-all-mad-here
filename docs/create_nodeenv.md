# How to create a node virtual environment

1. Create a python virtual environment:

    `python -m venv <venv_name>`

1. Activate the python virtual environment:
    * Windows: `source <path_to_venv>/Scripts/activate`
    * Mac: `source <path_to_venv>/bin/activate`

1. Run `pip install nodeenv` to install the nodeenv package:

    ```
    (venv) $ pip install nodeenv
    (venv) $ nodeenv --version
    1.7.0
    ```

1. Install Node.js into the venv:

    ```$ nodeenv -p --node=<node_version>```

    Where `node_version` is the version of node.js that you want to install.

    Reference: [Setting up a virtualenv with Node.js](https://nbdime.readthedocs.io/en/latest/nodevenv.html)

    **Note**: To confirm the node version within your venv, run this command: 
    
    ```$ node -v```