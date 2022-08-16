from random import randint


class GuessGame:
    def __init__(self, name):
        self.secretNumber = randint(1, 20)
        self.name = name

    def play_game(self):
        print('Well, ' + self.name + ', I\'m thinking of a number between 1 and 20')
        for guessesTaken in range(1, 7):
            print('Take a guess.')
            try:
                guess = int(input())
                if guess < self.secretNumber:
                    print('Your guess is too low')
                elif guess > self.secretNumber:
                    print('Your guess is too high')
                else:
                    break
            except ValueError:
                print("Hey, " + self.name + ", that\'s not a number!")

        if guess == self.secretNumber:
            print('Good job, ' + self.name + '! You guessed it in ' + str(guessesTaken) + ' guesses!')
        else:
            print('Nope. The number I was thinking of was ' + str(self.secretNumber))


def main():
    print('Hello, what\'s your name?')
    name = input()
    game = GuessGame(name)
    game.play_game()


main()
