# Angular Tips

## Force a Clean Install

1. Delete *node_modules* folder.
1. Delete *package-lock.json*.
1. Run ```npm install --force```.

## Update Angular Version

1. If it is not already installed, install the application. (*node_modules* must exist.)
1. Delete _package-lock.json_ file, and run the following command:

    ```$ ng update @angular/cli@<version> @angular/core@<version>```

    Where `<version>` is the Angular version; for example:

    ```$ ng update @angular/cli@12 @angular/core@12```

    **Note**: You must upgrade one version at a time. Refer to the [Angular Upgrade Guide](https://update.angular.io/) for details on how to upgrade to each version.

## Discover Vulnerabilities & Locate Package Dependencies

To discover vulnerabilities within your project, run this command:

`$ npm audit`
    
**Note**: To save the output to a file, add `> filename.txt`; for example, `npm audit > audit_results.txt`.

To list dependencies for a specific package, run this command:

`npm ls <package_name> dependencies`

**Note**: You can also search the *package.json* files within the *node_modules* folder for specific package names using this command:

`find ./node_modules -name package.json | xargs grep <package_name>`

## Create a Mock API

Source: [Fake Your Angular Backend Until You Make It](https://blog.angulartraining.com/fake-your-angular-backend-until-you-make-it-8d145f713e14)

1. ```npm install json-server```
1. Create an ```api``` folder under ```src```; i.e., ```src/api```
1. In the api folder create a ```db.json``` file; e.g., 
    ```
    {
        "periodicElements": [
            { "number": "1", "symbol": "H", "name": "Hydrogen", "weight": "1.00797"},
            { "number": "2", "symbol": "He", "name": "Helium", "weight": "4.0026"},
            { "number": "3", "symbol": "Li", "name": "Lithium", "weight": "6.941"},
            { "number": "4", "symbol": "Be", "name": "Beryllium", "weight": "9.01218"},
            { "number": "5", "symbol": "B", "name": "Boron", "weight": "10.81"},
            { "number": "6", "symbol": "C", "name": "Carbon", "weight": "12.011"},
            { "number": "7", "symbol": "N", "name": "Nitrogen", "weight": "14.0067"},
            { "number": "8", "symbol": "O", "name": "Oxygen", "weight": "15.9994"},
            { "number": "9", "symbol": "F", "name": "Fluorine", "weight": "18.998403"},
            { "number": "10", "symbol": "Ne", "name": "Neon", "weight": "20.179"}
        ]
    }
    ```
1. In the api folder, create a ```route.json``` file with the following content:
    ```
    {
        "/api/*": "/$1"
    }
    ```
1. Add the following key/value pair to the scripts section of your package.json file:
    ```
    "api": "json-server api/db.json --routes api/routes.json --no-cors=true"
    ```
1. Start the API: 
    ```
    npm run api
    ```

1. Access the API at `http://localhost:3000/api/periodicElements` to confirm the service is running.

1. Add ```HttpClientModule``` to ```app.module.ts```.
    ```
    import { BrowserModule } from '@angular/platform-browser';
    import { NgModule } from '@angular/core';
    ​
    import { AppComponent } from './app.component';
    import { HttpClientModule } from '@angular/common/http';
    ​
    @NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule,
        HttpClientModule,
    ],
    bootstrap: [AppComponent]
    })
    export class AppModule {}
    ```    