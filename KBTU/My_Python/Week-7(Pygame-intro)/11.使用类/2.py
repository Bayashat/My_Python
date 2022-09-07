import pygame

pygame.init()

winWidth = 800
winHeight = 640
win = pygame.display.set_mode((winWidth, winHeight))
bg = pygame.Surface((winWidth, winHeight))  # width,height
bg.fill((193, 186, 186))  # color


class GameObject(object):
    def __init__(self, x=10, y=10, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.color = color


class Rectangle(GameObject):
    def __init__(self, x=10, y=10, color=(255, 255, 255), width=30, height=30):
        GameObject.__init__(self, x, y, color)
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))


class Circle(GameObject):
    def __init__(self, x=10, y=10, color=(255, 255, 255), radius=30):
        GameObject.__init__(self, x, y, color)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def winUpdate():
    win.blit(bg, (0, 0))
    for go in gameObjects:
        go.draw()
    pygame.draw.circle(win, (255, 0, 0), (400, 400), 50)
    pygame.draw.circle(win, (0, 255, 0), (600, 400), 50)
    pygame.display.update()


FPS = 60
clock = pygame.time.Clock()
run = True


gameObjects = []

rect1 = Rectangle(250, 250, (255, 255, 255), 30, 30)
rect2 = Rectangle(200, 230, (255, 0, 255), 30, 30)
rect3 = Rectangle(100, 100, (255, 255, 0), 30, 30)
circ1 = Circle(300, 100, (255, 255, 255), 40)

gameObjects.extend([rect1, rect2, rect3, circ1])


def runProg():
    global run
    while run:
        ms = clock.tick(FPS)  # FPS - fps, ms - millsec between frames
        winUpdate()

        # for quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


runProg()
pygame.quit()