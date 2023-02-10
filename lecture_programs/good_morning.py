def greeter():
    time_of_day = ["morning", "evening", "nigth"]

    for time in time_of_day:
        print("Good " + time)
        feel = input("How are you feeling? ")
        print("I'm happy to hear that you are feeling " + feel)

greeter()
