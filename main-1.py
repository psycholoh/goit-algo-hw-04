import sys
from pathlib import Path
from colorama import init, Fore, Style


def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            for line in file:
                line = line.strip()  
                if not line:
                    continue

                try:
                    name, salary = line.split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка обробки рядка: {line}")
                    continue

            if count == 0:
                return (0, 0)

            average = total / count
            return (total, average)

    except FileNotFoundError:
        print(f"Файл не знайдено: {path.txt}")
        return (0, 0)

total, average = total_salary("path.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

