class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]
    
    def add_passenger(self,name):
        if self.open_seats==0:
            return False
        else:
            self.passengers.append(name)
            return True
    
    def open_seats(self):
        return self.capacity-len(self.passengers)

flight=Flight(5)
people=["person1","person2","person3","person4"]

for person in people:
    success=flight.add_passenger(person)
    if success:
        print(f"{person} is added")
    else:
        print(f"there is no available seat for {person}")