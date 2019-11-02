import pygame
from math import sin, cos, radians

pygame.init()


class color:  # color variables
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    White = (255, 255, 255)
    Yellow = (255, 255, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)
    colors = [Black, Red, Yellow, Green, Blue]


class main:  # general setup variables
    resolution = (1200, 800)
    screen = pygame.display.set_mode(resolution)
    screen.fill(color.White)
    done = False


class track(object):
    def __init__(self):
        self.width = 60
        self.height = 90
        self.start = [400, 400]
        self.toDraw = []

    def draw(self, screen):
        for rectangle in self.toDraw:
            pygame.draw.polygon(screen, color.colors[self.toDraw.index(rectangle)], rectangle)


def draw(screen):  # draws all elements and updates the display
    screen.fill(color.White)
    track.draw(screen)
    pygame.display.update()


def straight(start, direction, length):
    rectangles = [position(start)]

    for rectangle in range(length):
        if direction == 'horizontal':
            start = rectangles[rectangle][1]
        else:
            start = [rectangles[rectangle][0][0], rectangles[rectangle][0][1] - track.height]
        rectangles.append(position(start))

    return rectangles


def corner(start, degree, direction):
    rectangles = [position(start)]
    numberOfRectangles = int(degree // 22.5)

    for rectangle in range(numberOfRectangles):
        if(direction == 'right'):
            degree = 22.5
            corners = rotate(rectangles[rectangle], degree)
            difx = rectangles[rectangle][0][0] - corners[3][0]
            dify = corners[3][1] - rectangles[rectangle][0][1]

            for corner in corners:
                corner[0] += difx
                corner[1] -= dify

        else:
            degree = -22.5
            corners = rotate(rectangles[rectangle], degree)
            difx = corners[2][0] - rectangles[rectangle][1][0]
            dify = corners[2][1] - rectangles[rectangle][1][1]

            for corner in corners:
                corner[0] -= difx
                corner[1] -= dify

        rectangles.append(corners)
    return rectangles


def position(start):
    position = []
    position.append(start)
    position.append([start[0] + track.width, start[1]])
    position.append([start[0] + track.width, start[1] + track.height])
    position.append([start[0], start[1] + track.height])
    return position


def rotate(position, degree):
    degree = radians(degree)
    centre = middle(position)
    pos = []
    relativeCoordinates = relativePosition(position, centre)
    for i in range(len(relativeCoordinates)):
        x = centre[0] + (cos(degree) * relativeCoordinates[i][0] + -sin(degree) * relativeCoordinates[i][1])
        y = centre[1] + (sin(degree) * relativeCoordinates[i][0] + cos(degree) * relativeCoordinates[i][1])
        pos.append([x, y])
    return pos


def middle(position):
    x = position[0][0] + track.width // 2
    y = position[0][1] + track.height // 2
    middle = [x, y]
    return middle


def relativePosition(coordinates, centre):
    relativeCoordinates = []
    for coordinate in range(len(coordinates)):
        relativeCoordinates.append([coordinates[coordinate][0] - centre[0], coordinates[coordinate][1] - centre[1]])
    return relativeCoordinates


clock = pygame.time.Clock()
track = track()
track.toDraw = straight(track.start, 'vertical', 3)
while not main.done:
    dt = clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.done = True

    draw(main.screen)
