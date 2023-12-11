import random

def choose_word(difficulty):
    words_easy = ["книга", "месяц", "ручка", "шарик", "олень", "носок"]
    words_medium = ["компьютер", "котенок", "банан", "автомобиль", "робот"]
    words_hard = ["экзопланета", "кальмар", "тринитротолуол", "гиперболоид", "магниторезистивность"]

    if difficulty == "easy":
        return random.choice(words_easy)
    elif difficulty == "medium":
        return random.choice(words_medium)
    elif difficulty == "hard":
        return random.choice(words_hard)
    else:
        raise ValueError("Некорректный уровень сложности")

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "\u2591"  # Символ для пустого места (░)
    return displayed_word

def hangman():
    lives_mapping = {"easy": 7, "medium": 5, "hard": 3}

    print("Добро пожаловать в игру 'Поле чудес'!")
    play_again = "да"

    while play_again.lower() == "да":
        difficulty = input("Выберите уровень сложности (easy, medium, hard): ").lower()
        if difficulty not in lives_mapping:
            print("Некорректный уровень сложности. Используется уровень easy.")
            difficulty = "easy"

        lives = lives_mapping[difficulty]
        word_to_guess = choose_word(difficulty)
        guessed_letters = set()

        while True:
            current_display = display_word(word_to_guess, guessed_letters)
            print(f"Отгаданное слово: {current_display}")
            print(f"Жизни: {lives}")

            guess = input("Введите букву или слово целиком: ").lower()

            if len(guess) == 1:
                if guess in guessed_letters:
                    print("Вы уже вводили эту букву. Попробуйте другую.")
                elif guess in word_to_guess:
                    print("Правильно! Буква есть в слове.")
                    guessed_letters.add(guess)
                else:
                    print("Неправильно! Такой буквы нет в слове.")
                    lives -= 1
            elif len(guess) == len(word_to_guess) and guess.isalpha():
                if guess == word_to_guess:
                    print("Поздравляем! Вы отгадали слово!")
                    break
                else:
                    print("Неправильно! Попробуйте еще раз.")
                    lives -= 1
            else:
                print("Некорректный ввод. Введите одну букву или слово целиком.")

            if set(guessed_letters) == set(word_to_guess):
                print(f"Отгаданное слово: {word_to_guess}")
                print("Поздравляем! Вы отгадали слово!")
                break

            if lives == 0:
                print(f"Извините, вы проиграли. Загаданное слово было: {word_to_guess}")
                break

        play_again = input("Хотите сыграть ещё раз? (да/нет): ")

if __name__ == "__main__":
    hangman()
