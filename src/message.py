import subprocess

title = "Alarm Manager"


def print_title():
    subprocess.run("figlet " + title, shell=True)


def print_random_quote():
    subprocess.run("fortune | cowsay", shell=True)
