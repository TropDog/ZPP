from datetime import datetime
import time

def read_file(file_name):
    with open(file_name, 'r+') as file:
        content = file.readlines()
        content_list = []
        for line in content:
            content_list.append(line.strip().split(';'))

    return content_list, file.closed

def get_work(content_list):
    index = 0
    for i in range(len(content_list)):
        if content_list[i][2] == 'pending':
            content_list[i][1] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content_list[i][2] = 'in_progress'
            index = i
            break
        else:
            index = 'no-work'

    return content_list, index
    

def to_string(content):
    new_content = ""
    s = ';'
    for line in content:
        line_string = s.join(line)
        line_string += '\n'
        new_content += line_string
    
    return new_content
    
    
def save_status(file_name, content):
    with open(file_name, 'w') as file:
        file.write(str(content))

    return file.closed

def finish_work(content_list, i):
    content_list[i][1] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_list[i][2] = 'done'
    return content_list, i

def work(file_name):
    content = read_file(file_name)[0]
    content_1, i = get_work(content)
    if i != 'no-work':
        content_string = to_string(content_1)
        save_status(file_name, content_string)

        time.sleep(5)
    
        content_2, i = finish_work(content_1, i)
        content_string = to_string(content_2)
        save_status(file_name, content_string)
        print(f'klient w linii {i+1} = done')
    else:
        print('waiting for clients')



while True:
    work('clients_line.txt')
