import re

def process_journal(input_file):
    try:
        file = open(input_file, 'r')
        content = file.read()
        file.close()

        entries = []
        lines = content.split('\n')
        for line in lines:
            if 'Рейс' in line:
                match = re.search(r'Рейс (\d+) (прибыл|отправился) из (.+?) в (\d{2}:\d{2}:\d{2})', line)
                if match:
                    train_number = match.group(1)
                    operation = "прибыл" if 'прибыл' in match.group(2) else "отправился"
                    city = match.group(3)
                    time = match.group(4)
                    entries.append(f"[{time}] Поезд № {train_number} {operation} в {city}")

        return entries
    except Exception as e:
        raise e

def write_journal(entries, output_file):
    try:
        file = open(output_file, 'w', encoding='utf-8')
        for entry in entries:
            file.write(entry + '\n')
        file.close()
    except Exception as e:
        raise e

try:
    entries = process_journal('journal.txt')
    write_journal(entries, 'transformed_journal.txt')
except FileNotFoundError:
    print("Файл не найден")
except Exception as e:
    print(e)