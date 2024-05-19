from termcolor import colored


def is_valid_hour(hour):
    if len(hour) != 2:
        print(colored("Error: Hour must be a value of two digits", "red"))
        exit(1)

    try:
        if int(hour) < 00 or int(hour) > 23:
            print(colored("Error: Hour must be a value between 00 and 23", "red"))
            exit(1)
    except ValueError:
        print(colored("Error: Hour must be an integer", "red"))
        exit(1)

    if hour.find("-") != -1:
        print(colored("Error: Zero cannot be negative", "red"))
        exit(1)


def is_valid_minute(minute):
    if len(minute) != 2:
        print(colored("Error: Minute must be a value of two digits", "red"))
        exit(1)

    try:
        if int(minute) < 00 or int(minute) > 59:
            print(colored("Error: Minute must be a value between 00 and 59", "red"))
            exit(1)
    except ValueError:
        print(colored("Error: Minute must be an integer", "red"))
        exit(1)

    if minute.find("-") != -1:
        print(colored("Error: Zero cannot be negative", "red"))
        exit(1)


def handle_user_input():
    hour = input("Enter hour: ")

    is_valid_hour(hour)

    minute = input("Enter minute: ")

    is_valid_minute(minute)

    return hour + ":" + minute
