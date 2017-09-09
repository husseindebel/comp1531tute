class Vehicle:

    @abstract_method
    def move(self):
        pass


class Car(Vehicle):
   def move(self):
     print("car moving..")

class Bike(Vehicle):
    def move(self):
      print("bike moving..")

class Buss(Vehicle):
    
    def move(self):
        print("891 is moving")

class Traveller():
    def __init__(self, transport):
        self._transport = transport

    def start_journey(self):
        self._transport.move()

sam = Traveller(Bus())
sam.start_journey()
