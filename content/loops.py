def while_example():
    spam = 0
    while spam < 5:
        print("hello world")
        spam += 1


while_example()


def identify_yourself():
    name = ''
    while name != "bye":
        print("What's your name? Or say bye to leave me")
        name = input()
    print("Ok, bye")


identify_yourself()
