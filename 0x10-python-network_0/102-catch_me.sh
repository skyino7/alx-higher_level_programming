#!/bin/bash
# Makes a request to server and that causes the server to respond with a message containing You got me!, in the body of the response.
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me
