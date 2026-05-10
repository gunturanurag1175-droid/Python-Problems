
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started: 
            print("Car had been already started")
        else:
            started = True
            print("Car has started..")
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else: 
            started = False
            print("Car has Stopped.")
    elif command == "help":
        print("""Start - to start the car
Stop - to stop the car
quit - to quit""")
    elif command == "quit":
        break
    else: print("Sorry, I don't understand that!")