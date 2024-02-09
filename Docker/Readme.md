Docker is a platform that allows you to automate the deployment, scaling, and management of applications using containerization. A Docker container is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.

To create a Docker image with Cython and compiled code, you would typically follow these steps:

1. Write a `Dockerfile` that describes the environment in which your application will run. This includes the base image, any dependencies, environment variables, and the application itself.

2. Build the Docker image using the `docker build` command.

3. Run the Docker image using the `docker run` command.

Here's an example of how you can create a Docker image that includes Cython and some compiled code:

1. Create a `Dockerfile`:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD app /app

# Install Cython
RUN pip install cython

# Compile the Cython script
RUN python setup.py build_ext --inplace

# Run the compiled script when the container launches
CMD ["python", "main.py"]
```

In this `Dockerfile`, we start from a base image with Python 3.8 installed. We set the working directory to `/app` and add the contents of the current directory (which should include your Cython script and a `setup.py` file for building the Cython script) to the `/app` directory in the container. We then install Cython, compile the Cython script, and specify that the `main.py` script should be run when the container is launched.

2. Build the Docker image:

```bash
docker build -t my-cython-app .
```

This command builds the Docker image, with the tag `my-cython-app`, from the `Dockerfile` in the current directory.

3. Run the Docker image:

```bash
docker run -it --rm --name my-running-app my-cython-app
```

This command runs the Docker image as a container. The `-it` option tells Docker to allocate a pseudo-TTY connected to the container’s stdin, creating an interactive bash shell in the container. The `--rm` option tells Docker to automatically clean up the container and remove the file system when the container exits. The `--name` option assigns a name to the container.

Please replace `main.py` with the name of your Python script that uses the compiled Cython code. Also, ensure you have a `setup.py` file for building your Cython script.


Name the image and afterwards you can use it like this:

```bash
 docker run docker_test 16
```
or if you want to access the bash shell, the entry point is set to /bin/bash
```bash
docker docker run -it --entrypoint /bin/bash docker_test
```

Furthermore we can use this image to be used as our python environment in e.g. Pycharm.