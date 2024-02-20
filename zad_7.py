import requests
import json

class Brewery:
    def __init__(self,id:str,name:str,brewery_type:str,address_1:str,
                 address_2:str,address_3:str,city:str,state_province:str,
                 postal_code:str,country:str,longitude:str,latitude:str,
                 phone:str,website_url:str,state:str,street:str):
        self.id =id
        self.name=name,
        self.brewery_type=brewery_type,
        self.address_1=address_1,
        self.address_2=address_2,
        self.address_3=address_3,
        self.city=city,
        self.state_province=state_province,
        self.postal_code=postal_code,
        self.country=country,
        self.longitude=longitude,
        self.latitude=latitude,
        self.phone=phone,
        self.website_url=website_url,
        self.state=state,
        self.street=street

    def __str__(self):
        return f"Brewery ID: {self.id}\nName: {self.name}\nType: {self.brewery_type}\nAddress: {self.address_1}, {self.address_2}, {self.address_3}, {self.city}, {self.state_province}, {self.postal_code}, {self.country}\nLocation: ({self.longitude}, {self.latitude})\nPhone: {self.phone}\nWebsite: {self.website_url}\nState: {self.state}\nStreet: {self.street}"
    
    def create_brewery(id, name, brewery_type, address_1, address_2, address_3, city, state_province, postal_code, country, longitude, latitude, phone, website_url, state, street):
        return Brewery(id, name, brewery_type, address_1, address_2, address_3, city, state_province, postal_code, country, longitude, latitude, phone, website_url, state, street)
    
    def api_connection():
        response_API = requests.get('https://api.openbrewerydb.org/v1/breweries/random?size=20')
        data = response_API.text
        json_data = json.loads(data)
        return json_data

breweries = []
for brewery in Brewery.api_connection():
    new_brewery = Brewery.create_brewery(brewery['id'], brewery['name'], brewery['brewery_type'], brewery['address_1'], brewery['address_2'], brewery['address_3'], brewery['city'], brewery['state_province'], brewery['postal_code'], brewery['country'], brewery['longitude'], brewery['latitude'], brewery['phone'], brewery['website_url'], brewery['state'], brewery['street'])
    breweries.append(new_brewery)

for brewery in breweries:
    print(str(brewery))
    print("-------------")


    