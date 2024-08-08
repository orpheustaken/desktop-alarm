from domain.audio import Audio
from domain.equation import Equation
from domain.input import Input
from domain.message import Message
from domain.schedule import Schedule


class Main:
    def __init__(self):
        self.time_input = None
        self.audio = Audio()
        self.equation = Equation()
        self.input = Input()
        self.message = Message()
        self.schedule = Schedule()

    def run(self):
        self.message.print_title()

        self.time_input = self.input.handle_user_input()

        self.message.print_execution_time(self.time_input)

        # wait until time defined by user to proceed
        self.schedule.check_system_time_loop(self.time_input)

        self.audio.play_audio()

        self.message.print_random_quote()

        # TODO: equations to solve for then be able to stop the sound and exit
        self.equation.enter_equation_loop()

        self.audio.stop_audio()

        exit(0)


if __name__ == "__main__":
    app = Main()
    app.run()
