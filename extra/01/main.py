from random import randint

flag = 1
trys = 0
random_number = randint(0, 100)
# print(random_number)
while flag:
    text_input = input("Ввод пользователя: ")
    if text_input.strip().lower() == "выход":
        exit(0)
    
    user_input = int(text_input)

    if user_input == random_number:
        flag = 0
    elif user_input < random_number:
        flag = 1
        print("Ваше число меньше!")
    else:
        flag = 1
        print("Ваше число больше!")
    trys += 1

print(f"Поздравляем! Вы угадали число за {trys} попытки!")