# Angular in Docker

## Host Angular Application in Docker

1. Create Dockerfile; see [Dockerfile](../angular_docker/host_in_docker/hello-world/Dockerfile)
1. Build Dockerfile: 
   ```$ docker build -t <image_name> .```
1. Run container:
    ```$ docker run --name <container_name> -d -p 8080:80 <image_name>```
1. Access app on localhost:8080.

## Install and Build Angular Application in Docker

1. Create new sample application:
    ```ng new hello-world```
1. Create Dockerfile; see [Dockerfile](../angular_docker/install_build_in_docker/hello-world/Dockerfile).
1. Build Docker image:
   ```$ docker build -t <image_name> .```
1. Run container:
    ```$ docker run --name <container_name> -d -p 8080:80 <image_name>```
1. Access app on localhost:8080.
