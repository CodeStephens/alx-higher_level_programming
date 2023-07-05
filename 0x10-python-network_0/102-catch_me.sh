#!/bin/bash
# HTTP request PUT method "You got me!"
curl -sLo /dev/null -w "You find me!" 0.0.0.0:5000/catch_me
