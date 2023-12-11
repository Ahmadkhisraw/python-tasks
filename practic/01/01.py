import random

def monty_hall_simulation(num_simulations):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_simulations):
        chosen_door = random.randrange(1, 4)

        prize_door = random.randrange(1, 4)

        remaining_doors = [door for door in [1, 2, 3] if door != chosen_door and door != prize_door]
        door_opened = random.choice(remaining_doors)

        stay_wins += chosen_door == prize_door

        switch_wins += (6 - chosen_door - door_opened) == prize_door

    stay_win_percentage = stay_wins / num_simulations * 100
    switch_win_percentage = switch_wins / num_simulations * 100

    return stay_win_percentage, switch_win_percentage

if __name__ == "__main__":
    num_simulations = 100000
    stay_win_percentage, switch_win_percentage = monty_hall_simulation(num_simulations)
    print(f"При оставании при своем выборе выигрыш происходит в {stay_win_percentage:.2f}% случаев.")
    print(f"При изменении выбора выигрыш происходит в {switch_win_percentage:.2f}% случаев.")