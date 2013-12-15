import pygame, sys, random, math
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([1000, 700], pygame.FULLSCREEN)


G = 6.67e-11

def F(G, p1, p2):
    return ((G)(p1.m)(p2.m))/(getDist(p1, p2)*getDist(p1, p2))
    
def getDist(p1, p2):
    return math.sqrt(((p1.x - p2.x) * (p1.x - p2.x)) + ((p1.y - p2.y) * (p1.y - p2.y)))


class Particle():
    def __init__(self):
        self.x = random.randint(1, 1000)
        self.y = random.randint(1, 700)
        self.m = random.randint(1e10, 1e11)
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.color = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]
        self.PointRect = pygame.Rect(100, 100, 1, 1)
    def MoveParticle(self, x, y):
        self.PointRect.move(x, y)

pa = Particle()
pb = Particle()
pc = Particle()
pd = Particle()
pe = Particle()
pf = Particle()
pl = [pa, pb, pc, pd, pe, pf]

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
    for p1 in pl:
        for p2 in pl:
            if p1 is not p2:
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                dist = math.sqrt(dx*dx + dy*dy)
                F = G * p1.m * p2.m / (dist * dist)
                
                p1.ax = (dx / dist) * (F / p1.m)
                p1.ay = (dy / dist) * (F / p1.m)
                
                p1.vx += p1.ax
                p1.vy += p1.ay
                
                p1.x += p1.vx
                p1.y += p1.vy
	pf.x, pf.y = pygame.mouse.get_pos()
    for p in pl:
		screen.fill(p.color, [p.x, p.y, 10, 10])
    pygame.display.flip()           