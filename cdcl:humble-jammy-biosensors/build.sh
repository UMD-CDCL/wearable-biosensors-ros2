#!/bin/bash

docker build \
  --no-cache \
  --ssh default \
  -t cdcl:humble-jammy-biosensors \
  .
