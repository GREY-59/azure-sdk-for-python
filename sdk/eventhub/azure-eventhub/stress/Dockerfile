# syntax=docker/dockerfile:1

FROM python:slim-bookworm

WORKDIR /app

COPY ./scripts /app/stress/scripts

WORKDIR /app/stress/scripts
RUN pip3 install -r dev_requirement.txt
