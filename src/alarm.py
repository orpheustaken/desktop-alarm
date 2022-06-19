import audio

import subprocess
import datetime

title = "Alarm Manager"
count_exit_prompt = 0

subprocess.run("figlet " + title, shell=True)

hour = input("Enter hour: ")
minute = input("Enter minute: ")

time_input = hour + ":" + minute

print("\nExecute at " + time_input + "...")

# Wait until time defined by user to proceed
while 1:
    system_time = datetime.datetime.now()
    system_time_formatted = system_time.strftime("%H:%M")

    if system_time_formatted == time_input:
        break

audio.play_audio()

subprocess.run("fortune | cowsay", shell=True)

while 1:
    if count_exit_prompt == 0:
        prompt = input("Want to turn it off? [Y/n] ").lower()
    else:
        prompt = input("What about now? [Y/n] ").lower()

    if prompt == "y" or prompt == "":
        break
    else:
        count_exit_prompt += 1

audio.stop_audio()

exit(0)
