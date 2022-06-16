from multiprocessing import Process

import os
import time
import datetime

title = "Alarm"
audio  = 'assets/marc.m4a'
# audio = 'assets/sound.opus'

def play_audio():
    os.system("2>/dev/null 1>/dev/null " + "mpv --no-video --loop " + audio)

play_audio_process = Process(target=play_audio)

os.system("figlet " + title)

hour = input("Enter hour: ")
minute = input("Enter minute: ")

time_input = hour + ":" + minute

print("\nExecute at " + time_input + "...")

while(1):
    system_time = datetime.datetime.now()
    system_time_formatted = system_time.strftime("%H:%M")

    if (system_time_formatted == time_input):
        break

play_audio_process.start()
time.sleep(1)

while(1):
    prompt = input("\nWant to turn it off? [Y/n] ").lower()

    if (prompt == "y" or prompt == ""):
        break

play_audio_process.terminate()
os.system("kill $(pidof mpv)")

exit(0)

