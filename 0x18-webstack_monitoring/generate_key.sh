#!/bin/bash

# Generate a random 32-character string
application_key=$(openssl rand -hex 16)

echo "Generated Application Key: $application_key"
