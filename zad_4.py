class Property:
    def __init__(self,area:str, rooms:int, price: float, address:str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    
    def __str__(self):
        return f"Property Details:\nArea: {self.area}\nNumber of Rooms: {self.rooms}\nPrice: {self.price}\nAddress: {self.address}"

class House(Property):
    def __init__ (self, area: str, rooms: int, price: float, address: str, plot:int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Property type - House:\n{super().__str__()}\nPlot Area: {self.plot}"

class Flat(Property):
    def __init__(self, area: str, rooms: int, price: float, address: str, floor:int) -> None:
        self.floor = floor
        super().__init__(area, rooms, price, address)

    def __str__(self):
        return f"Property type - Flat\n{super().__str__()}\nFloor: {self.floor}"


house1 = House("Katowice", 3, 123.5, 'address1', 500)
flat1 = Flat("Katowice", 3, 123.5, 'address1',3)

print(str(flat1))
print(str(house1))