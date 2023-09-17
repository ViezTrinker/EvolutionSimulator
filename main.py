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

defaultenergy = 1.5

plt.ion()
fig = plt.figure()

delay = 0.1

# Classes
class Prey():
    def __init__(self, alive, x, y, speed, vision, consumption, attack, energy):
        self.alive = alive
        self.x = x
        self.y = y
        self.speed = speed
        self.vision = vision
        self.consumption = consumption
        self.attack = attack
        self.energy = energy
        self.normalize()
    def setvalues(self, alive, speed, vision, consumption, attack, energy):
        self.alive = alive
        self.speed = speed
        self.vision = vision
        self.consumption = consumption
        self.attack = attack
        self.energy = energy
    def normalize(self):
        alive = self.alive
        speed = self.speed / (self.speed + self.vision + self.consumption + self.attack) * maxstatprey
        vision = self.vision / (self.speed + self.vision + self.consumption + self.attack) * maxstatprey
        consumption = self.consumption / (self.speed + self.vision + self.consumption + self.attack) * maxstatprey
        attack = self.attack / (self.speed + self.vision + self.consumption + self.attack) * maxstatprey
        energy = self.energy
        self.setvalues(alive, speed, vision, consumption, attack, energy)


class Predator():
    def __init__(self, alive, x, y, speed, vision, consumption, attack, energy):
        self.alive = alive
        self.x = x
        self.y = y
        self.speed = speed
        self.vision = vision
        self.consumption = consumption
        self.attack = attack
        self.energy = energy
        self.normalize()

    def setvalues(self, alive, speed, vision, consumption, attack, energy):
        self.alive = alive
        self.speed = speed
        self.vision = vision
        self.consumption = consumption
        self.attack = attack
        self.energy = energy

    def normalize(self):
        alive = self.alive
        speed = self.speed / (self.speed + self.vision + self.consumption + self.attack) * maxstatpred
        vision = self.vision / (self.speed + self.vision + self.consumption + self.attack) * maxstatpred
        consumption = self.consumption / (self.speed + self.vision + self.consumption + self.attack) * maxstatpred
        attack = self.attack / (self.speed + self.vision + self.consumption + self.attack) * maxstatpred
        energy = self.energy
        self.setvalues(alive, speed, vision, consumption, attack, energy)

class Plant():
    def __init__(self, alive, x, y):
        self.alive = alive
        self.x = x
        self.y = y
    def setvalues(self, alive, x, y):
        self.alive = alive
        self.x = x
        self.y = y


def InitializeObjects():
    for x in range(numprey):
        prey[x] = Prey(random.random() <= aliveprobprey, random.random() * lengthx, random.random() * lengthy,
                       random.random() * maxspeed, random.random() * maxvision, random.random() * maxconsumption,
                       random.random() * maxattack, defaultenergy)

    for x in range(numpredator):
        predator[x] = Predator(random.random() <= aliveprobpred, random.random() * lengthx, random.random() * lengthy,
                               random.random() * maxspeed, random.random() * maxvision,
                               random.random() * maxconsumption, random.random() * maxattack, defaultenergy)

    for x in range(numplant):
        plant[x] = Plant(random.random() <= aliveprobplant, random.random() * lengthx, random.random() * lengthy)

def GetPositions():
    for x in range(numprey):
        preyposx[x] = prey[x].x * prey[x].alive
        preyposy[x] = prey[x].y * prey[x].alive
    for x in range(numpredator):
        predposx[x] = predator[x].x * predator[x].alive
        predposy[x] = predator[x].y * predator[x].alive
    for x in range(numplant):
        plantposx[x] = plant[x].x * plant[x].alive
        plantposy[x] = plant[x].y * plant[x].alive

def Plot():
    GetPositions()
    fig.clear()
    plt.title("Evolution Simulator")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0, lengthx)
    plt.ylim(0, lengthy)
    plt.grid()
    plt.plot(preyposx, preyposy, 'bo', markersize=2)
    plt.plot(predposx, predposy, 'rx', markersize=2)
    plt.plot(plantposx, plantposy, 'gs', markersize=2)
    fig.canvas.draw()
    fig.canvas.flush_events()

# START #
preyposx  = [0] * numprey
predposx  = [0] * numpredator
plantposx = [0] * numplant
preyposy  = [0] * numprey
predposy  = [0] * numpredator
plantposy = [0] * numplant

prey     = [0] * numprey
predator = [0] * numpredator
plant    = [0] * numplant

InitializeObjects()

# Main Loop
while True:
    # TODO: Implement the whole logic
    print("I am running")
    Plot()

    time.sleep(delay)

# End of program
print("Program finished")