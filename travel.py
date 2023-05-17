class Traveler:
    def __init__(self, name, dob, address, email):
        self.name = name
        self.dob = dob
        self.address = address
        self.email = email

    def __str__(self):
        return self.name
    

class Trip:
    def __init__(self, destination, mode, length):
        self.destination = destination
        self.mode = mode
        self.length = length
        self.travelers = []

    def register(self, traveler):
        self.travelers.append(traveler)

    def __str__(self):
        return f'{self.destination} by {self.mode}'


matt = travel.Traveler("Matt", "01/01/01", "Mars", "matt@matt.com")
mars = Trip('Mars', 'Rocket', '6 mo')
mars.register(matt)
for traveler in mars.travelers:
    print(traveler)