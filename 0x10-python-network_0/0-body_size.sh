#!/bin/bash
size_of_download=$(curl -s -w '%{size_download}' -o /dev/null $1)
echo ${size_of_download}
