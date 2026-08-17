# taser karaoke
This is all the software and hardware used to put together the taser karaoke system.

# Dependencies
I am using Python 3.13.13
The code should work with any OS, however it does require some screen capture software. I am using OBS for this project, but you can always use a different one.
- Make sure that it can publish the captured video to a virtual camera. This is how the python script capture the game footage.

# How to launch
1. Install dependencies
```bash
# Use this in powershell to get into virtual environment "taser"
# Make sure to create a virtual environment first
pip install -r requirements.txt
```
2. Install YARG (Yet Another Rhythm Game)
Go to the following github repo to install it.
https://github.com/YARC-Official/YARC-Launcher/releases/tag/v1.3.0 

3. Install OBS
This is how the video is captured from the game and analyzed by the python script.
- Make sure that the entire game is captured in the OBS frame.
- "Start Virtual Camera" when you want to start sending the game footage to the python script.

4. Run game-viewing python script
```bash
Python game_viewer.py
```