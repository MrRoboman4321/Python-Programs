import pygame, sys, random, math
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([500, 500])


G = 6.67e-11

def F(G, p1, p2):
    return ((G)(p1.m)(p2.m))/(getDist(p1, p2)*getDist(p1, p2))
    
def getDist(p1, p2):
    return math.sqrt(((p1.x - p2.x) * (p1.x - p2.x)) + ((p1.y - p2.y) * (p1.y - p2.y)))


class Particle():
    def __init__(self):
        self.x = random.randint(1, 500)
        self.y = random.randint(1, 500)
        self.m = random.randint(1e10, 1e11)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.PointRect = pygame.Rect(100, 100, 1, 1)
    def MoveParticle(self, x, y):
        self.PointRect.move(x, y)

p1 = Particle()
p2 = Particle()
surface = pygame.Surface((1000, 500))

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    dist = math.sqrt(dx*dx + dy*dy)
    F = G * p1.m * p2.m / (dist * dist)
    p1.ax = (dx / dist) * (F / p1.m)
    p1.ay = (dy / dist) * (F / p1.m)
    p2.ax = (-dx / dist) * (F / p2.m)
    p2.ay = (-dy / dist) * (F / p2.m)
    p1.vx += p1.ax
    p1.vy += p1.ay
    p2.vx += p2.ax
    p2.vy += p2.ay
	
    
    p1.x += p1.vx
    p1.y += p1.vy
    p2.x += p2.vx
    p2.y += p2.vy
    screen.fill([255, 255, 255], [p1.x, p1.y, 5, 5])
    screen.fill([255, 0, 0], [p2.x, p2.y, 5, 5])
    pygame.display.flip()	