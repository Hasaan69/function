def shutdown():
    choice = input("Do you want to shutdown? Press 'x' for yes, 'y' for no: ")
    if choice.lower() == 'x':
        print('Shutting down...')
        quit()
    else:
        print("It's not gonna shutdown.")
shutdown()