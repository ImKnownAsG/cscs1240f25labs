class Car:
    make = None
    wheels = 4
    transmission = ""
    
    def __init__(self, make, wheels, trans):
        self.make = make
        self.wheels = wheels
        self.transmission = trans

theCar = list()
theCar.append( Car('Ford', 5, 'Auto') )
theCar.append( Car('Nissan', 3, 'Manual') )

engines = [thisCar.make for thisCar in theCar]

print(engines)

print([thisCar.make for thisCar in theCar])
