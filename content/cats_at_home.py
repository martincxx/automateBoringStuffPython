def cats_at_home(cats):
    if cats >= 4:
        print('That\'s a lot of cats')
    else:
        print('That\'s not that many cats')

def read():
    print('How many cats do you have?')
    numCats = input()
    try:
        cats_at_home(int(numCats))
    except ValueError:
        print('That\'s not a valid number of cats')


read()