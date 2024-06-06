#!/usr/bin/env bash

# Set environment variables
HBNB_MYSQL_USER=hbnb_dev
HBNB_MYSQL_PWD=hbnb_dev_pwd
HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db
HBNB_TYPE_STORAGE=db
HBNB_API_HOST=0.0.0.0
HBNB_API_PORT=5000

cd ../../../


# Prompt the user for a specific microapi to check
echo "Enter a specific microapi to check: "
read -r microapi
sleep 2

# Perform actions using curl
echo "This is the first test: printing all subjects first"
curl -X GET http://0.0.0.0:5000/api/v1/"$microapi/"
sleep 2

echo "This is the second test: posting"
curl -X POST http://0.0.0.0:5000/api/v1/"$microapi"/ -H "Content-Type: application/json" -d '{"name": "California"}'
sleep 2
