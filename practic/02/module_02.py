import random

def birthday(num_people):
    birthdays = set()

    for _ in range(num_people):
        bday = random.randint(1, 28)
        
        if bday in birthdays:
            return True
        birthdays.add(bday)

    return False

def birthday_experiment(num_iterations):
    successful_experiments = 0

    for _ in range(num_iterations):
        if birthday(23):
            successful_experiments += 1

    return (successful_experiments / num_iterations) * 100

def monty_hall(num_simulations):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_simulations):
        chosen_door = random.randint(1, 3)

        prize_door = random.randint(1, 3)

        stay_wins += chosen_door == prize_door

        switch_wins += random.choice([door for door in [1, 2, 3] if door != chosen_door and door != prize_door]) == prize_door

    stay_win_percentage = stay_wins / num_simulations * 100
    switch_win_percentage = switch_wins / num_simulations * 100

    return stay_win_percentage, switch_win_percentage