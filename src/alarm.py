import audio
import message
import user_input

import datetime

count_exit_prompt = 0

message.print_title()

time_input = user_input.handle_user_input()

print("\nExecute at " + time_input + "...")

# Wait until time defined by user to proceed
while 1:
    system_time = datetime.datetime.now()
    system_time_formatted = system_time.strftime("%H:%M")

    if system_time_formatted == time_input:
        break

audio.play_audio()

message.print_random_quote()

# Equations to solve
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
