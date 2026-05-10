print("Hello User! Wanna learn how to build a car? if yes, just say 'Start'. ")
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car has started..")
    elif command == "stop":
        print("Car has Stopped.")
    elif command == "help":
        print("""Start - to start the car
Stop - to stop the car
quit - to quit""")
    elif command == "quit":
        break
    else: print("Sorry, I don't understand that!")