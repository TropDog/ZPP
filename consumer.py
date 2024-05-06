# Odbiera i wykonuje prace
from datetime import datetime
import time


def work(index):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("clients_line.txt", "r") as file:
            lines = file.readlines()
            if len(lines) != 0:
                klient_lista = lines[index].split(";")
                klient_lista[1] = current_datetime
                klient_lista[2] = 'in_progress'
                s = ';'
                klient_string = s.join(klient_lista)
                lines[index] = klient_string
                lines[index] += '\n'  # Dodaj znak nowej linii, aby uniknąć przylepiania do poprzedniej linii
                with open("clients_line.txt", "w") as file:
                    file.writelines(lines)
                    print(f"Linia {index + 1} została pobrana do pracy.")
            else:
                pass                 
    except FileNotFoundError:
        # Jeśli plik nie istnieje, pass
        pass
    
    time.sleep(10)
    
    try:
        with open("clients_line.txt", "r") as file:
            lines = file.readlines()
            klient_lista = lines[index].split(";")
            klient_lista[1] = current_datetime
            klient_lista[2] = 'done'
            s = ';'
            klient_string = s.join(klient_lista)
            lines[index] = klient_string
            lines[index] += '\n'  # Dodaj znak nowej linii, aby uniknąć przylepiania do poprzedniej linii
            with open("clients_line.txt", "w") as file:
                file.writelines(lines)
                print(f"Linia {index + 1} praca z klientem została zakończona")                      
    except FileNotFoundError:
        # Jeśli plik nie istnieje, pass
        pass

def get_pending_index_from_file():
    try:
        with open("clients_line.txt", "r") as file:
            lines = file.readlines()
            if len(lines)!= 0:
                for i in range(len(lines)):
                    klient = lines[i].split(";")
                    if klient[2] == 'pending\n':
                        work(i)
                    else:
                        print('nie pracuje')

    except FileNotFoundError:
        # Jeśli plik nie istnieje, pass
        pass

while True:
    get_pending_index_from_file()


    
