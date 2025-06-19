import random
import os
import time


def play():
    os.system('clear')
    print("You get three chances, answer wisely\n\n")
    r = random.randint(1,5)
    c = 0
    for i in range(3):
        answer = int(input("enter you guess: "))
        if answer == r:
            print("Congratulations you Won the game 😃 !!!");
            break
        else:
            print("wrong guess! try again 😔")
            c += 1

    if c == 3 :
        print(f"\n\nyou lose 🤣\n\n the number was {r}")

    time.sleep(1)

    os.system('clear')

    return
    

def guess_game():
    while 1:
        os.system('clear')
        question = input("Do you want to play? (y/n): ").lower()

        if question == 'y':
            play()
        elif question == 'n':
            exit(0)
        else:
            print("invalid input detected\n")


if __name__ == "__main__":
    guess_game()
    exit(0)

