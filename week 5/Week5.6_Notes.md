## Docker Installation
To isolate our project file from our system machine, Docker is one of the options. With Docker we are able to pack all our project is a system that we want and run it in any system machine. For example if we want Ubuntu 18.04 we can have it in any operating system such as a mac or windows. <br>
Here are the instructions to get started with Docker for the churn prediction project:

### MacOS

For MacOS, installation steps are in the [Docker docs](https://docs.docker.com/desktop/install/mac-install/).


## Notes

- We pack our project in a Docker container. Then, we're able to run our project on any machine.
- Firstly, we need to have a Docker image. In the Docker image file there are settings and dependecies of our project. The Docker images are available at [Docker](https://hub.docker.com/search?type=image) website.

Here is our Dockerfile (no comments allowed in Dockerfile, so we should remove the comments)

```docker
# First install the python 3.8, the slim version uses less space
FROM python:3.8.12-slim

# Install pipenv library in Docker 
RUN pip install pipenv

# create a directory in Docker named app and we're using it as work directory 
WORKDIR /app                                                                

# Copy the Pip files into our working derectory 
COPY ["Pipfile", "Pipfile.lock", "./"]

# install the pipenv dependencies for the project and deploy them.
RUN pipenv install --deploy --system

# Copy any python files and the model we had to the working directory of Docker 
COPY ["*.py", "churn-model.bin", "./"]

# We need to expose the 9696 port because we're not able to communicate with Docker outside it
EXPOSE 9696

# If we run the Docker image, we want our churn app to be running
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_serving:app"]
```

The flags `--deploy` and `--system` makes sure that we install the dependencies directly inside the Docker container without creating an additional virtual environment (which `pipenv` does by default). We don't need the dependencies in a venv. Bcz Docker provides complete isolation at system level.

If we don't put the last line `ENTRYPOINT`, we will be in a python shell.
Note that for the entrypoint, we put our commands in double quotes.

After creating the Dockerfile, we need to build it:

```bash
docker build -t churn-prediction .
```

To run it,  execute the command below:

```bash
docker run -it -p 9696:9696 churn-prediction:latest
```

Flag details: 

* `-t`: is used for specifying the tag name "churn-prediction".
* `-it`: in order for Docker to allow us access to the terminal.
* `--rm`: allows us to remove the image from the system after we're done.  
* `-p`: to map the 9696 port of the Docker to 9696 port of our machine. (first 9696 is the port number of our machine and the last one is Docker container port.)
* `--entrypoint=bash`: After running Docker, we will now be able to communicate with the container using bash (as we would normally do with the Terminal). Default is `python`.
