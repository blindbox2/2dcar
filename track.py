import pygame
from math import degrees, sin, cos

pygame.init()


class color:  # color variables
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    White = (255, 255, 255)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)


class main:  # general setup variables
    resolution = (1200, 800)
    screen = pygame.display.set_mode(resolution)
    screen.fill(color.White)
    done = False


class rect(object):
    def __init__(self):
        self.width = 60
        self.height = 90
        self.degree = degrees(90)
        self.leftTop = [400, 400]
        self.position = position(self.leftTop, self.width, self.height)
        self.middle = middle(self.position, self.width, self.height)

    def draw(self, screen):
        pygame.draw.polygon(screen, color.Blue, self.position, 5)
        pygame.draw.polygon(screen, color.Blue, next(self.position, self.width, self.height, 5), 5)


def draw(screen):  # draws all elements and updates the display
    screen.fill(color.White)
    track.draw(screen)
    pygame.display.update()


def position(start, width, height):
    position = []
    position.append(start)
    position.append([start[0] + width, start[1]])
    position.append([start[0] + width, start[1] + height])
    position.append([start[0], start[1] + height])
    return position


def next(a, width, height, degree):
    start = a[0]
    test = position(start, width, height)
    rot = rotate(test, degree)
    dif = abs(rot[3][0] - test[3][0])

    print(dif)
    for i in range(3):
        rot[i][0] += dif

    return rot


def middle(position, width, height):
    x = position[0][0] + width // 2
    y = position[0][1] + height // 2
    middle = [x, y]
    return middle


def relativePosition(coordinates, middle):
    relativeCoordinates = []
    for coordinate in range(len(coordinates)):
        relativeCoordinates.append([coordinates[coordinate][0] - middle[0], coordinates[coordinate][1] - middle[1]])
    return relativeCoordinates


def rotate(position, degree):
    degree = degrees(degree)
    pos = []
    relativeCoordinates = relativePosition(position, track.middle)
    for corner in range(len(relativeCoordinates)):
        x = track.middle[0] + (cos(degree) * relativeCoordinates[corner][0] + -sin(degree) * relativeCoordinates[corner][1])
        y = track.middle[1] + (sin(degree) * relativeCoordinates[corner][0] + cos(degree) * relativeCoordinates[corner][1])
        pos.append([x, y])
    return pos


track = rect()
clock = pygame.time.Clock()
while not main.done:
    dt = clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.done = True

    draw(main.screen)
