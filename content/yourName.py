def your_name():
    name = ''
    while True:
        print('Please type your name. Or bye to exit')
        name = input()
        if name == 'bye':
            break
    print('Ok bye')


your_name()
