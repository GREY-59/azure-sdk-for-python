# syntax=docker/dockerfile:1

FROM python:3.12.0b4-slim

WORKDIR /app

COPY ./scripts /app/stress/scripts

WORKDIR /app/stress/scripts
RUN pip3 install -r dev_requirement.txt
