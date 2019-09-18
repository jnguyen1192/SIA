FROM ubuntu:18.04

WORKDIR /code

# TODO Install libraries

# install all python libraries
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files on the container
COPY . .


# TODO Launch unit tests


CMD echo hello world !