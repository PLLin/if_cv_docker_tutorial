FROM ubuntu:18.04

WORKDIR /app
COPY . /app

RUN apt update && apt install -y python3 python3-pip
RUN pip3 install cython
RUN pip3 install numpy

ENTRYPOINT ["bash"]
