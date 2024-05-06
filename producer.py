# Odbieranie pracy i zapisywanie
from datetime import datetime

try:
    # Otwieramy plik w trybie do dopisywania (append)
    with open("clients_line.txt", "a") as file:
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Klient{file.tell()+1};{current_datetime};pending\n")
except FileNotFoundError:
    with open("clients_line.txt", "w") as file:
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Klient1;{current_datetime};pending\n")
