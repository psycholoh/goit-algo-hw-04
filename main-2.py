import sys
from pathlib import Path


def get_cats_info(path):
    try:
        with open(path,'r', encoding='utf-8') as file:
            cats= []
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    Id,Name,Age = line.split(',')
                    cats.append({
                        'Id': Id,
                        'Name': Name,
                        'Age': Age
                    })
                except ValueError:
                    print(f"{line} - Невірний формат рядка")
        return cats
    except FileNotFoundError:
            print(f"Файл не знайдено: {path}")
cats_info = get_cats_info("cats.txt")
print(cats_info)



