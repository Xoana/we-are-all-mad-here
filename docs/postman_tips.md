# Postman

## Sharing bearer token across multiple requests
Source: [Environments and globals](https://learning.postman.com/docs/sending-requests/variables/)
1.	Click the settings icon (top-right corner) to create an environment.
2.	Click the environment name.
3.	In the Variable column, enter “Bearer” and click Update.
4.	Select your new environment from the drop-down list.
5.	Open your authorization request, and enter the following code on the Tests tab.

    ```
    let jsonData = pm.response.json();
    let token = jsonData.access_token;
    pm.environment.set('Bearer', token);
    ```

6.	Do the following for the remaining requests:

    a.	Click the **Authorization** tab.
    b.	Select **Bearer Token** from the Type drop-down list.
    c.	Enter the following text in the Token field: `{{variable_name}}``

    Where *variable_name* is the name of the environment variable.

Once you send the Authorization request, the bearer token should be available to the other requests.
