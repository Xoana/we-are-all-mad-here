# Angular Tips

## Force a Clean Install

1. Delete *node_modules* folder.
1. Delete *package-lock.json*.
1. Run ```npm install –force```.

## Update Angular Version

1. If it is not already installed, install the application. (*node_modules* must exist.)
1. Delete _package-lock.json_ file, and run the following command:

    ```$ ng update @angular/cli@<version> @angular/core@<version>```

    Where *<version>* is the target Angular version; for example, 
    ```$ ng update @angular/cli@12 @angular/core@12```

    **Note**: You must upgrade one version at a time.

## Create a Mock API

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

References:
* [Fake Your Angular Backend Until You Make It](https://blog.angulartraining.com/fake-your-angular-backend-until-you-make-it-8d145f713e14)

