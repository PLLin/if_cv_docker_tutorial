FROM ubuntu:18.04

WORKDIR /app
COPY . /app

RUN apt update && apt install -y python3 python3-pip

RUN pip3 install pip==21.2.1
RUN pip3 install cython
RUN pip3 install -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENTRYPOINT ["uvicorn", "demo:app", "--host", "0.0.0.0", "--port", "8000"]
