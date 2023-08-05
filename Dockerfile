FROM ubuntu:18.04

RUN apt update
RUN apt install -y curl
RUN apt install -y wget
RUN apt install -y git
RUN apt install -y python3.7 python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow

RUN mkdir /home/Dev