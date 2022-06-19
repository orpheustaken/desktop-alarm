import audio
import equation
import message
import time_sys
import user_input

message.print_title()

time_input = user_input.handle_user_input()

# Wait until time defined by user to proceed
time_sys.check_system_time_loop(time_input)

audio.play_audio()

message.print_random_quote()

# Equations to solve for then be able to stop the sound and exit
equation.enter_equation_loop()

audio.stop_audio()

exit(0)
