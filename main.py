from ast import pattern
from math import cos, radians, sin
import pygame as pg

vec = pg.Vector2

class Pen():
    def __init__(self) -> None:
        self.lower = circles[-1]
        pass

    def draw(self):
        penpos = self.lower.penpos()

        if len(ink) > DIM[0]/2: ink.pop(-1)
        ink.insert(0, penpos.y)

        if len(patternInk) > patternLen: patternInk.pop(-1)
        patternInk.insert(0, penpos)

        pg.draw.circle(disp, (255,255,255), penpos, 5)
        pg.draw.line(disp, (255,255,255), penpos, (DIM[0]/2, penpos.y))



class Circle():
    def __init__(self, frequency, amplitude, start_angle = 0) -> None:
        self.angle = radians(start_angle)
        self.frequency = frequency
        self.amplitude = abs(amplitude)
        self.centre = vec(0,0)
        pass

    def penpos(self):
        return self.centre+vec(
            (self.amplitude*cos(self.angle)),
            (self.amplitude*sin(self.angle))
        )

    def draw(self):
        self.centre = circles[circles.index(self)-1].penpos() if circles.index(self) > 0 else vec(150, DIM[1]/2)
        pg.draw.circle(disp, (255,255,255), self.centre, self.amplitude, 1)

    def update(self):
        try: self.angle+=1/self.frequency
        except: pass
        pass



DIM = (600, 400)
FPS = 60


pg.init()

disp = pg.display.set_mode(DIM)
clock = pg.time.Clock()



circles=[
    Circle(10, 40),
    Circle(5, 25),
    Circle(2.5, 25/2)
]


circles = [
    Circle(10/(2*n+1), 50/(2*n+1)) for n in range(20)
]


circles = [
    Circle(10/(n+1), 40/(n+1)) for n in range(20)
]

circles = [Circle(f, a, s) for f, a, s in [
    (20, 80, 0),
    (-20, 40, 0),
    (20, 40, 0),
]]


pen = Pen()

ink = []
patternInk = []

patternLen = 1000

running = True
while running:
    disp.fill((0,0,0))
    pg.draw.line(disp, (100,100,100), (DIM[0]/2, DIM[1]/2), (DIM[0], DIM[1]/2))
    pg.draw.line(disp, (100,100,100), (DIM[0]/2, 0), (DIM[0]/2, DIM[1]))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    for x in circles: x.draw(); x.update()
    pen.draw()
    try: 
        pg.draw.lines(disp, (100,100,255), False, [[x+DIM[0]/2,y] for x, y in enumerate(ink)])
        pg.draw.lines(disp, (100,100,225), False, patternInk)
    except: pass


    pg.display.update()
    clock.tick(FPS)

        
