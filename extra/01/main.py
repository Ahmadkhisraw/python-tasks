from random import randint

flag = 1
random_number = None
while flag:
    random_number = randint(0, 100)
    user_input = int(input("Guess a number between 0 and 100: "))

    if user_input == random_number:
        flag = 0
    elif user_input < random_number:
        flag = 1
        print("Too low")
    else:
        flag = 1
        print("Too high")

print(f"Correct! The number was {random_number}")