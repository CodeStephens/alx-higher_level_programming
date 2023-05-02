#!/bin/bash
# HTTP request PUT method "You got me!"
curl -so /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
