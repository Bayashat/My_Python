##########   3. Ernur's version : sin cos 

import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Point:
    # constructed using a normal tupple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)
def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope *    index    * dash_length)
        end   = origin + (slope * (index + 1) * dash_length)
        pygame.draw.line(surf, color, start.get(), end.get(), width)

def draw_dashed_lines(surf, color, points , width,dash_length):
  for i in range(len(points)-1):
    draw_dashed_line(surf, color, points[i],points[i+1], width,dash_length)
    
  
def get_points(f,xrange , step , kx, ky, center):
  num = math.ceil( (xrange[1] - xrange[0]) / step )
  x_values = (x * step + xrange[0] for x in range(num + 1))
  func = ((kx * x, ky * f(x)) for x in x_values)
  points = tuple(map(lambda x : (x[0] + center[0], -x[1] + center[1]), func))
  return points

k = 2/3
xrange = (-3 * math.pi, 3*math.pi)
step = 0.1
kx = (2 * WIDTH / 3) / (6 * math.pi)
ky = (2 * HEIGHT / 3) / 2
center = (WIDTH //2, HEIGHT //2 )

sin_points = get_points(math.sin, xrange, step, kx, ky, center)
cos_points = get_points(math.cos, xrange, step, kx, ky, center)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    screen.fill((255,255,255))

    start = (1-k) / 2
    end = (k + (1-k) / 2)
    # Axis-s: 
    pygame.draw.line(screen, (0,0,0), (start * WIDTH, HEIGHT // 2), (end * WIDTH, HEIGHT // 2), 2)    # Y
    pygame.draw.line(screen, (0,0,0),  (WIDTH // 2, start * HEIGHT), (WIDTH // 2, end * HEIGHT), 2) # X
  
    # Edges: 
    pygame.draw.line(screen, (0,0,0), (start * WIDTH, start * HEIGHT), (end * WIDTH, start * HEIGHT), 2)   # Top 
    pygame.draw.line(screen, (0,0,0),  (end * WIDTH, start * HEIGHT), (end * WIDTH, end * HEIGHT), 2)     # Right
    pygame.draw.line(screen, (0,0,0), (end * WIDTH, end * HEIGHT), (start * WIDTH, end * HEIGHT), 2)      # under
    pygame.draw.line(screen, (0,0,0),  (start * WIDTH, end * HEIGHT), (start * WIDTH, start * HEIGHT), 2) # Left

    '''
     # or we can :
    bounding_points = ((start * WIDTH, start * HEIGHT),
                       (end * WIDTH, start * HEIGHT),
                       (end * WIDTH, end * HEIGHT),
                       (start * WIDTH, end * HEIGHT))
    pygame.draw.aalines(screen, (0,0,0), True, bounding_points, 4)
    '''
    # add 'aa'lines can make your graph more beautiful
    draw_dashed_lines(screen, (0,0,255), cos_points, 2,3)
    # pygame.draw.aalines(screen, (0,0,255), False, cos_points, 2)
    pygame.draw.aalines(screen, (255,0,0), False, sin_points, 2)


    pygame.display.flip()