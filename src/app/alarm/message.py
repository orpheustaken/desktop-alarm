import subprocess

title = "Alarm Manager"


def print_title():
    subprocess.run("figlet " + title, shell=True)


def print_execution_time(time_input):
    print("\nAlarm set to run at " + time_input + "...")


def print_random_quote():
    subprocess.run("fortune | cowsay", shell=True)
