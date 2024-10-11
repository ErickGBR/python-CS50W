class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p = Point(2,3)
print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity) :
        self.capacity = capacity
        self.passenger = []
    def add_passenger(self, name) :
        if not self.open_seats() :
            return False
        self.passenger.append(name)
        return True
    def open_seats(self) :
        return self.capacity - len(self.passenger)

flight = Flight(3)
people = ["Harry", "Ron", "Hermione","Ginny"]

for person in people :
    success = flight.add_passenger(person)
    if success :
        print(f"added {person} to flight is successfully")
    else:
        print(f"No available seat for {person}")