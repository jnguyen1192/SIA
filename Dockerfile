FROM ubuntu:18.04

WORKDIR /code

# Copy all the files on the container
COPY . .

# TODO Install libraries
# @source : https://hub.docker.com/r/fnndsc/ubuntu-python3/dockerfile/
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

#RUN xhost +

RUN touch ~/.Xauthority

RUN pip3 install --no-cache-dir -r requirements.txt


# TODO Launch unit tests
CMD python3 infinite_loop.py