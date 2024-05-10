# Odbiera i wykonuje prace
from datetime import datetime
import time


def get_work(lines):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
    if len(lines) != 0:
        for index in range(len(lines)):
            klient = lines[index].split(";")
            if klient[2] == 'pending\n':
                klient[1] = current_datetime
                klient[2] = 'in_progress'
                s = ';'
                klient_string = s.join(klient)
                lines[index] = klient_string
                lines[index] += '\n'  # Dodaj znak nowej linii, aby uniknąć przylepiania do poprzedniej linii
                return str(lines), index
    else:
        pass          
    
def save_work(lines, index):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
    if len(lines) != 0:
        klient = lines[index].split(";")
        klient[1] = current_datetime
        klient[2] = 'done'
        s = ';'
        klient_string = str(s.join(klient))
        lines[index] = klient_string
        lines[index] += '\n'  # Dodaj znak nowej linii, aby uniknąć przylepiania do poprzedniej linii
        return str(lines)
    else:
        pass   


def get_pending_index_from_file():
    try:
        with open("clients_line.txt", "r+") as file:
            lines = file.readlines()
            content, index = get_work(lines)
            file.write(content)
            print(f'praca z klientem {index +1} rozpoczęta')

            time.sleep(10)

            lines = file.readlines()
            file.write(save_work(lines, index))
            print(f'praca z klientem {index +1} zakończona')

    except FileNotFoundError:
        file.close()

while True:
    get_pending_index_from_file()


    
