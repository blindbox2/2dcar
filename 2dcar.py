import pygame

pygame.init()

# Classes


class color:  # color variables
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    White = (255, 255, 255)
    Green = (0, 255, 0)


class main:  # general setup variables
    resolution = (1200, 800)
    screen = pygame.display.set_mode(resolution)
    screen.fill(color.White)
    done = False


class track:  # track properties
    def __init__(self):
        self.x = 0.05 * main.resolution[0]
        self.y = 0.05 * main.resolution[1]
        self.length = 0.9 * main.resolution[0]
        self.height = 0.9 * main.resolution[1]
        self.width = 100

    def draw(self, screen):
        pygame.draw.rect(screen, color.Black, [self.x, self.y, self.length, self.height], 5)
        pygame.draw.rect(screen, color.Black, [self.x + 0.5 * self.width, self.y + 0.5 * self.width, self.length - self.width, self.height - self.width], 5)


class car(object):  # car properties
    def __init__(self):
        self.x = 200
        self.y = 200
        self.width = 20
        self.height = 30
        self.vel = 2
        self.color = (color.White)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 5)

# Functions


def draw(screen):  # draws all elements and updates the display
    screen.fill((255, 255, 255))
    track.draw(screen)
    car.draw(screen)
    pygame.display.update()


def collission():  # detects car collission with the track
    if(car.x > track.x and car.x + car.width < track.x + track.length) and car.y > track.y and car.y + car.height < track.y + track.height:
        if(car.x + car.width > track.x + track.width // 2 and car.x < track.x + track.length - track.width // 2 and car.y + car.height > track.y + track.width // 2 and car.y < track.y + track.height - track.width // 2):
            car.color = color.Red
        else:
            car.color = color.Green
    else:
        car.color = color.Red


def move():  # translates user input into movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        car.x += car.vel
    if keys[pygame.K_LEFT]:
        car.x -= car.vel
    if keys[pygame.K_UP]:
        car.y -= car.vel
    if keys[pygame.K_DOWN]:
        car.y += car.vel


# Main loop which runs the game
track = track()
car = car()
while not main.done:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.done = True

    move()
    collission()
    draw(main.screen)
