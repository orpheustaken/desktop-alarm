import subprocess


class Message:
    title = "Alarm Manager"

    @staticmethod
    def print_title():
        subprocess.run("figlet " + Message.title, shell=True)

    @staticmethod
    def print_execution_time(time_input):
        print("\nAlarm set to run at " + time_input + "...")

    @staticmethod
    def print_random_quote():
        subprocess.run("fortune | cowsay", shell=True)
