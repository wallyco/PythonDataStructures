class Drone(object):

    def __init__(self):
        self.droneSpeed = 0.0
        self.droneHeight = 0.0

    def accelerate(self):
        self.droneSpeed += 10

    def decelerate(self):
        if self.droneSpeed != 0:
            self.droneSpeed -= 10

    def ascend(self):
        self.droneHeight += 10

    def decend(self):
        if self.droneHeight != 0:
            self.droneHeight -= 10

    def toString(self):
        print("Drone Speed ( %s ) | ( %s ) Drone Height" % (self.droneSpeed, self.droneHeight))



