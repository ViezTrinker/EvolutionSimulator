import matplotlib.pyplot as plt
import time
import random

# Declarations
numprey         = 2000
numpredator     = 2000
numplant        = 2000
lengthx         = 100
lengthy         = 100
maxspeed        = 10
maxvision       = 10
maxconsumption  = 10
maxattack       = 10

maxstatprey = 40
maxstatpred = 40

aliveprobprey  = 0.1
aliveprobpred  = 0.1
aliveprobplant = 0.5

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
        self.normalize()
    def setvalues(self, speed, vision, consumption, attack):
        self.speed = speed
        self.vision = vision
        self.consumption = consumption
        self.attack = attack
    def normalize(self):
        speed = self.speed / (self.speed + self.vision + self.consumption + self.attack) * maxstatprey
        vision = self.vision / (self.speed + self.vision + self.consumption + self.attack) * maxstatprey
        consumption = self.consumption / (self.speed + self.vision + self.consumption + self.attack) * maxstatprey
        attack = self.attack / (self.speed + self.vision + self.consumption + self.attack) * maxstatprey
        self.setvalues(speed, vision, consumption, attack)


class Predator():
    def __init__(self, alive, x, y, speed, vision, consumption, attack):
        self.alive = alive
        self.x = x
        self.y = y
        self.speed = speed
        self.vision = vision
        self.consumption = consumption
        self.attack = attack
        self.normalize()

    def setvalues(self, speed, vision, consumption, attack):
        self.speed = speed
        self.vision = vision
        self.consumption = consumption
        self.attack = attack

    def normalize(self):
        speed = self.speed / (self.speed + self.vision + self.consumption + self.attack) * maxstatpred
        vision = self.vision / (self.speed + self.vision + self.consumption + self.attack) * maxstatpred
        consumption = self.consumption / (self.speed + self.vision + self.consumption + self.attack) * maxstatpred
        attack = self.attack / (self.speed + self.vision + self.consumption + self.attack) * maxstatpred
        self.setvalues(speed, vision, consumption, attack)

class Plant():
    def __init__(self, alive, x, y):
        self.alive = alive
        self.x = x
        self.y = y

def InitializeObjects():
    for x in range(numprey):
        prey[x] = Prey(random.random() <= aliveprobprey, random.random() * lengthx, random.random() * lengthy,
                       random.random() * maxspeed, random.random() * maxvision, random.random() * maxconsumption,
                       random.random() * maxattack)

    for x in range(numpredator):
        predator[x] = Predator(random.random() <= aliveprobpred, random.random() * lengthx, random.random() * lengthy,
                               random.random() * maxspeed, random.random() * maxvision,
                               random.random() * maxconsumption, random.random() * maxattack)

    for x in range(numplant):
        plant[x] = Plant(random.random() <= aliveprobplant, random.random() * lengthx, random.random() * lengthy)

# Create objects

prey     = [0] * numprey
predator = [0] * numpredator
plant    = [0] * numplant

# START #
InitializeObjects()
# Main Loop
while True:
    # TODO: Implement the whole logic
    print("I am running")

    # TODO: Plot graph in the right way
    # plt.plot([1, 2])
    # plt.show()

    time.sleep(1)

# End of Program
print("Program finished")