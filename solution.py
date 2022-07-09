# define the Vehicle class
class Vehicle():

    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    
    def description(self):
        desc_str = f"{self.name} is a {self.color} {self.kind} worth ${self.value:,.2f}."
        return desc_str
# your code goes here
car1 = Vehicle('Fer', 'Convertible', 'Red', 60000)
car2 = Vehicle('Jump', 'Van', 'Blue', 10000)

# test code
print(car1.description())
print(car2.description()

