#!/usr/bin/env bash

# Install portaudio development libraries required for PyAudio
apt-get update && apt-get install -y portaudio19-dev

# Install Python dependencies
pip install -r requirements.txt
