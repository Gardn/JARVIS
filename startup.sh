#!/bin/bash
## I created a startup.sh file to ensure that the python 
## file runs before the festival program. This gives us 
## the most up to date time and weather every time we boot, 
## though weather requires internet connection.

#### Running the weather python file
python weather.py
#### Running the Festival program to speak the text, 
#### put out from the above command.
festival --tts "Login.txt"


