import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    """Функция читает содержимое CSV файла,
    парсит его и преобразовывает в структуру данных JSON"""
    line = []
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            line.append(row)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(line, indent=4)
        jsonf.write(jsonString)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
