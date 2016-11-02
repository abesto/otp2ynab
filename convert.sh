#!/bin/bash

set -euo pipefail

input="$1"
name=$(basename "$input" '.xml')
output="${name}.ofx"

if [ ! -f virtualenv/bin/activate ]; then
    virtualenv --python python3 virtualenv
fi

set +u; . virtualenv/bin/activate; set -u

if ! pip freeze | grep ofxstatement-otp &>/dev/null; then
    pip install ofxstatement ofxstatement-otp
fi

ofxstatement convert -t otp "$input" "$output"

echo "Converted ${input} to ${output}"
