# Angular in nodeenv

This procedure describes how to create a nodeenv python virtual environment for developing Angular applications.

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

1. With your venv still activated, create an Angular application:

    ```ng new hello-world```

1. Change into the application folder, and run the following command to build and serve the application:

    ```ng serve```

1. Access the application at `http://localhost:4200/`.


