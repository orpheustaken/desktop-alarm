def enter_equation_loop():
    count_exit_prompt = 0

    while 1:
        if count_exit_prompt == 0:
            prompt = input("Want to turn it off? [Y/n] ").lower()
        else:
            prompt = input("What about now? [Y/n] ").lower()

        if prompt == "y" or prompt == "":
            break
        else:
            count_exit_prompt += 1
