#!/bin/bash

# "--priviledged" required to access usb and bluetooth devices
# "-v /dev/bus/usb:/dev/bus/usb" required to access usb
# "--net=host" required to make docker network equiv to host network
# "--cap-add=NET_ADMIN" allows us to use `tc`
# "-it" makes container interactive
#    -v /home/yashas/biosensors_ws:/home/cdcl/cdcl_ws \
docker run --rm \
    --privileged \
    -v /dev/bus/usb:/dev/bus/usb \
    --device=/dev/hidraw1 \
    --net=host \
    --cap-add=NET_ADMIN \
    -it \
    --name biosensors \
    cdcl:humble-jammy-biosensors
