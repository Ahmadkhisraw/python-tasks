import module_02

if __name__ == "__main__":
    print("Пример использования:")
    print(f"Вероятность совпадения дней рождения для 23 человек: {module_02.birthday_experiment(1000):.2f}%")
    print(f"Процент выигрыша при изменении выбора в игре Монти Холла: {module_02.monty_hall(10000):.2f}%")