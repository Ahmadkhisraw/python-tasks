def read_number(file):
    return int(file.readline())

def read_numbers_from_file(file_name):
    file = None
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        return [], False

    numbers = []
    try:
        number_of_items = read_number(file)
        if number_of_items <= 0:
            return [], False
        
        while number_of_items:
            numbers.append(read_number(file))
            number_of_items -= 1
    except ValueError:
        return [], False

    file.close()

    return numbers, True

if __name__ == "__main__":
    numbers, success = read_numbers_from_file('numbers.txt')
    if success:
        print(numbers)
    else:
        print("an error occured during reading the file")