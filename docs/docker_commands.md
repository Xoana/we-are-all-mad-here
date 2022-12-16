# Frequently-Used Docker Commands


* Get Docker version:
    * Summary: ```$ docker --version```
    * Details: ```$ docker version```

* List images:

   ```$ docker image ls```

* List active containers:

   ```$ docker container ls```

* Build image from Dockerfile: 
   
   ```$ docker build -t <image_name> .```

* Run container from image:

    ```$ docker run --name <container_name> -d -p 8080:80 <image_name>```

* Stop a container:

    ```$ docker stop install_build_in_docker_container```
