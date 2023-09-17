import matplotlib.pyplot as plt
import time

# Declarations
numprey      = 2000
numpredator  = 2000
numplant     = 2000
lenghtx      = 100
lengthy      = 100

# Classes

class Prey():
    def __init__(self, alive, x, y, speed, vision, consumption, attack):
        self.alive = alive
        self.x = x
        self.y = y
        self.speed = speed
        self.vision = vision
        self.consumption = consumption
        self.attack = attack

class Predator():
    def __init__(self, alive, x, y, speed, vision, consumption, attack):
        self.alive = alive
        self.x = x
        self.y = y
        self.speed = speed
        self.vision = vision
        self.consumption = consumption
        self.attack = attack

class Plant():
    def __init__(self, alive, x, y):
        self.alive = alive
        self.x = x
        self.y = y

# Create objects

prey     = [0] * numprey
predator = [0] * numpredator
plant    = [0] * numplant

for x in range(numprey):
    # TODO: initialize in the right way
    prey[x] = Prey(True, 1, 2, 3, 4, 5, 6)

for x in range(numpredator):
    # TODO: initialize in the right way
    predator[x] = Predator(True, 1, 2, 3, 4, 5, 6)

for x in range(numplant):
    # TODO: initialize in the right way
    plant[x] = Plant(True, 1, 2)

# Main Loop

while True:
    # TODO: Implement the whole logic
    print("I am running")

    # TODO: Plot graph in the right way
    plt.plot([1, 2])
    plt.show()

    time.sleep(1)

# End of Program
print("Program finished")