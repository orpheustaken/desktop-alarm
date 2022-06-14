import os
import datetime

title = "Alarm Manager"
# audio = 'assets/sound.opus'
audio  = 'assets/marc.m4a'

os.system("figlet " + title)

wakeup_hour = input("Enter hour: ")
wakeup_minute = input("Enter minute: ")

wakeup = wakeup_hour + ":" + wakeup_minute

print("\nWake up at " + wakeup + "...")

while(1):
    system_time = datetime.datetime.now()
    system_time_formatted = system_time.strftime("%H:%M")

    if (system_time_formatted == wakeup):
        break

while(1):
    os.system("mpv " + audio)
#    prompt = input("Want to turn it down? ")
#
#    if (prompt == "y"):
#        break

