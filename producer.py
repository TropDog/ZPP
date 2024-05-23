import requests

list_of_urls = []

with open('img_urls.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        list_of_urls.append(line.strip())

print(list_of_urls)

for line in list_of_urls:
    url = f'http://127.0.0.1:8000/with_rabbit/{line}'
    response = requests.get(url)

    print(f'{response.status_code} : {response}')