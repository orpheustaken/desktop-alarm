import datetime
import time


def check_system_time_loop(time_input):
    while 1:
        system_time = datetime.datetime.now()
        system_time_formatted = system_time.strftime("%H:%M")

        if system_time_formatted == time_input:
            break

        # To address performance issues
        time.sleep(40)
