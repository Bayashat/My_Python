import pygame
import random
pygame.init()

winWidth = 800
winHeight = 640
win = pygame.display.set_mode((winWidth, winHeight))
bg = pygame.Surface((winWidth, winHeight))  # width,height
bg.fill((193, 186, 186))  # color


class GameObject(object):
    def __init__(self, x=10, y=10, color=(255, 255, 255), speed=8):
        self.x = x
        self.y = y
        self.color = color
        self.up = True
        self.down = False
        self.left = False
        self.right = False
        self.speed = speed

    def direction(self, right=False, left=False, down=False, up=False):
        self.right = right
        self.left = left
        self.up = up
        self.down = down

    def move(self):
        if self.right:
            self.x += self.speed
        elif self.left:
            self.x -= self.speed

    def fall(self):
        pass


class Rectangle(GameObject):
    def __init__(self, x=10, y=10, color=(255, 255, 255), width=30, height=30):
        GameObject.__init__(self, x, y, color)
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))


class Circle(GameObject):
    def __init__(self, x=10, y=10, color=(255, 255, 255), radius=30, speed=8):
        GameObject.__init__(self, x, y, color, speed)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def fall(self):
        self.y += self.speed


def winUpdate():
    win.blit(bg, (0, 0))
    spawner()
    for go in gameObjects:
        go.draw()
        go.fall()
        if go.y > 640:
            gameObjects.remove(go)

    # pygame.draw.circle(win, (255, 0, 0), (400, 400), 50)
    # pygame.draw.circle(win, (0, 255, 0), (600, 400), 50)
    pygame.display.update()


FPS = 60
clock = pygame.time.Clock()
run = True


gameObjects = []

mainFigure = Rectangle(winWidth//2, 600, (171, 11, 11), 50, 25)
circ1 = Circle(300, 100, (255, 255, 255), 40)

gameObjects.extend([mainFigure])


def spawner():
    if len(gameObjects) < 10:
        gameObjects.append(Circle(random.randint(10, 700), random.randrange(
            0, 200, 30), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randrange(10, 50, 10), random.randrange(4, 20, 4)))


def runProg():
    global run
    while run:
        ms = clock.tick(FPS)  # FPS - fps, ms - millsec between frames
        winUpdate()
        keys = pygame.key.get_pressed()
        # for quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if keys[pygame.K_d] and mainFigure.x < winWidth - mainFigure.width:
            mainFigure.direction(right=True)
            mainFigure.move()
        elif keys[pygame.K_a] and mainFigure.x > 0:
            mainFigure.direction(left=True)
            mainFigure.move()


runProg()
pygame.quit()