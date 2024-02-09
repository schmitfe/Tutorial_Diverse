# syntax=docker/dockerfile:1

# Use an official Python runtime as a parent image
FROM ubuntu:22.04

# Set the working directory in the container to /app
WORKDIR /app


# Update the package lists for upgrades for security purposes
# Install gcc and python
RUN apt-get update && apt-get install -y gcc python3 python3-pip

# Install Cython
RUN pip3 install cython

# Add the current directory contents into the container at /app
ADD ./app /app

# Compile the Cython script
RUN python3 setup.py build_ext --inplace

# Run the compiled script when the container launches
#ENTRYPOINT ["python3", "main.py", "--arg"]
#CMD ["3"]
CMD ["python3", "main.py","--arg", "3"]
