#!/usr/bin/env python3

### Nicer selection of sound devices, test prog

# requirements: sudo apt install python3-pyaudio

import sounddevice as sd

print( sd.query_devices() )
