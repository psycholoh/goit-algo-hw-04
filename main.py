import sys

from datetime import datetime
import colorama

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
                    total += int(salary)
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
                        'Age': int(Age)
                    })
                except ValueError:
                    print(f"{line} - Невірний формат рядка")
        return cats
    except FileNotFoundError:
            print(f"Файл не знайдено: {path}")
cats_info = get_cats_info("cats.txt")
print(cats_info)












if len(sys.argv) < 2:
    print("❌ Ти не передав шлях до папки. Спробуй ще раз.")
    sys.exit()

path = sys.argv[1]
print(f"✅ Отримано шлях: {path}")

dir_path = Path(path)
if not dir_path.exists():
    print(f"❌ Шлях '{path}' не існує.")
    exit()
if not dir_path.is_dir():
    print(f"{path} - це не директорія.")
    exit()
print(f"✅ Шлях '{path}' існує і це директорія.")

for item in dir_path.iterdir():
    if item.is_dir():
        print(Fore.BLUE + f"Директорія: {item.name}"+ Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"Файл: {item.name}"+ Style.RESET_ALL)










contacts = {}


def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added.")   

def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print("Contact updated.")
    else:
        print("Contact not found.")    

contacts = {}


def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added.")   

def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print("Contact updated.")
    else:
        print("Contact not found.")    

def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")



def parse_input(user_input):
    return user_input.strip().lower().split()


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input(">>> ")
        command_parts = parse_input(user_input)
        print("Parsed command:", command_parts)
        if not command_parts:
            print("Invalid command.")
            continue

        command = command_parts[0]

        if command == "add" and len(command_parts) == 3:    
            name = command_parts[1]
            phone = command_parts[2]
            add_contact(name, phone)
        elif command == "change" and len(command_parts) == 3:
            name = command_parts[1]
            phone = command_parts[2]
            change_contact(name, phone)

        elif command == "phone" and len(command_parts) == 2:
            name = command_parts[1]
            show_phone(name)    
        
        elif command == "all":
            if contacts:
                for name, phone in contacts.items():
                    print(f"{name}: {phone}")
                else:
                    print("No contacts found.")

        elif user_input.lower() in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()








