class Flight():

    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        self.passengers.append(name)

    def open_seats(self):
        return self.capacity - len(self.passengers)
