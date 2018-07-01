#!/bin/bash

set -xeuo pipefail
mv ~/Downloads/export.xml ./$1.xml
./convert.sh $1.xml
