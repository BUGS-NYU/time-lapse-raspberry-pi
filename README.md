# time-lapse-raspberry-pi
Using a Raspberry Pi and camera module, I created a sunset timelapse. Detailed documentation on how to make your own
Configure the software. Go to preferences, Raspberry Pi Configuration and Interfaces. Enable the camera. 
Go to programming and select Python 3 (IDLE).
Open a new file and save it as camera.py (The file is in the repository).
Run the script using run or F5
The preview will only work when the pi is using a monitor and there is no remote access. 
If you want to take a timelapse using still images, use sleep to indicate the time frame. Input for sleep is the number of
seconds you would like the module to wait.
You can also take a video using this code:

camera.start_preview()
camera.start_recording('/home/pi/Desktop/pivideo.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
To play the video go to the terminal and type: omxplayer video.h264
