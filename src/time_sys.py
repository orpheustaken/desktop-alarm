import datetime


def check_system_time_loop(time):
    while 1:
        system_time = datetime.datetime.now()
        system_time_formatted = system_time.strftime("%H:%M")

        if system_time_formatted == time:
            break
