import sys
import colorama
from pathlib import Path
from colorama import init, Fore, Style





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





