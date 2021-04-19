from random import randint

NUM_MIN: int = 1
NUM_MAX: int = 1000


def imagine_number():
    print(f"Please, think of a number between {NUM_MIN} and {NUM_MAX}, and I will guess it in under 10 guesses.\n")
    return None


def guess_number():
    min = NUM_MIN
    max = NUM_MAX
    while True:
        guess = (max + min) // 2
        print(f"I guess {guess}")
        try:
            guess_res = int(input("1 - too much \n2 - too little \n3 - I guessed\n"))
        except:
            print("Invalid input!")
            return None
        if guess_res == 3:
            print("I won!")
            return None
        if min == max:
            print('You cheat!')
            return None
        if guess_res == 1:
            max = guess
        elif guess_res == 2:
            min = guess


imagine_number()
guess_number()
