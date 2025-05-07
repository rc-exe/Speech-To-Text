#!/usr/bin/env bash

# Install portaudio for PyAudio
apt-get update && apt-get install -y portaudio19-dev

# Continue with the normal build
pip install -r requirements.txt
