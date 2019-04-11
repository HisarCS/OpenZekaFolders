import pygame
from threading import Thread
from time import sleep


class RemoteController:

    def __init__(self):

        pygame.init()
        pygame.joystick.init()

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        self.buttons = []
        self.lx = 0
        self.ly = 0
        self.rx = 0
        self.ry = 0

        self.isListening = False

    def startListening(self, frequency=100):
        self.frequency = frequency
        self.isListening = True
        Thread(target=self.__update__, args=()).start()
        self.isListening = True
        return self

    def __update__(self):

        while self.isListening:
            sleep(1.0/self.frequency)
            for e in pygame.event.get():
                if (e.type == pygame.JOYBUTTONDOWN and e.button not in self.buttons):
                    self.buttons.append(e.button)
                if (e.type == pygame.JOYBUTTONUP and e.button in self.buttons):
                    self.buttons.remove(e.button)
                if (e.type == pygame.JOYAXISMOTION):
                    if (e.axis == 0):
                        self.lx = e.value
                    elif (e.axis == 1):
                        self.ly = e.value
                    elif (e.axis == 2):
                        self.rx = e.value
                    elif (e.axis == 3):
                        self.ry = e.value

    def getLeftJoystick(self):
        return self.lx, self.ly

    def getRightJoystick(self):
        return self.rx, self.ry

    def getButtons(self):
        return self.buttons

    def readValues(self):
        return self.getLeftJoystick(), self.getRightJoystick(), self.getButtons()

    def disable(self):
        self.isListening = False


