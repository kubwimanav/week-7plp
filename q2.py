class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    
    def move(self):
        return "Moving in some way"
    
    def describe(self):
        return f"{self.name} (Max speed: {self.max_speed})"


class Car(Vehicle):
    def __init__(self, name, max_speed, fuel_type):
        super().__init__(name, max_speed)
        self.fuel_type = fuel_type
    
    def move(self):
        return f"The {self.name} is driving on the road at {self.max_speed} mph using {self.fuel_type}."


class Plane(Vehicle):
    def __init__(self, name, max_speed, max_altitude):
        super().__init__(name, max_speed)
        self.max_altitude = max_altitude
    
    def move(self):
        return f"The {self.name} is flying through the air at {self.max_speed} mph, reaching {self.max_altitude} feet."


class Boat(Vehicle):
    def __init__(self, name, max_speed, boat_type):
        super().__init__(name, max_speed)
        self.boat_type = boat_type
    
    def move(self):
        return f"The {self.name} is sailing across the water at {self.max_speed} knots. It's a {self.boat_type}."


# Creating different vehicles
tesla = Car("Tesla Model S", 155, "electricity")
boeing = Plane("Boeing 747", 570, 45000)
yacht = Boat("Luxury Yacht", 30, "motor yacht")

# Demonstrating polymorphism
vehicles = [tesla, boeing, yacht]

print("Each vehicle moves in its own way:")
for vehicle in vehicles:
    print(f"{vehicle.describe()}: {vehicle.move()}")