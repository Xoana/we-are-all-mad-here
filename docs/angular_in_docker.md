# Angular in Docker

## Host Angular Application in Docker

1. If you do not already have an Angular application, create one using this command:

    ```ng new hello-world```

1. Create a Dockerfile:

    To build a previously installed application:

    ```
    FROM node:12.7-alpine AS build
    RUN npm run build
    FROM nginx:1.17.1-alpine
    COPY ./dist/test-ui /usr/share/nginx/html
    ```

    For example, refer to this [Dockerfile](../angular_docker/host_in_docker/hello-world/Dockerfile).
    
    To install and build an application:

    ```
    FROM node:12.7-alpine AS build
    WORKDIR /usr/src/app
    COPY package.json ./
    RUN npm install
    COPY . .
    RUN npm run build
    FROM nginx:1.17.1-alpine
    COPY --from=build /usr/src/app/dist/hello-world /usr/share/nginx/html
    ```

    For example, refer to this [Dockerfile](../angular_docker/install_build_in_docker/hello-world/Dockerfile).

1. Build the Dockerfile: 

    ```$ docker build -t <image_name> .```

1. Run container:

    ```$ docker run --name <container_name> -d -p 8080:80 <image_name>```

1. Access app on localhost:8080.
