#!/bin/bash

# Get the directory path of the script
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

# Set the relative path to the socket file
SOCKET_FILE="${SCRIPT_DIR}/run/gunicorn.sock"

# Wait for 4 seconds
sleep 4

# Set the permissions for the socket file
chmod 777 "${SOCKET_FILE}"
