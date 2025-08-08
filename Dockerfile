FROM python:slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN ["pip", "install", "--no-cache-dir", "setuptools", "cookiecutter"]

RUN mkdir /cookiecutter
WORKDIR /cookiecutter
ENTRYPOINT ["cookiecutter"]
