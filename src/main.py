import pygame

from vector import Vector2
from mutils import Grid2
from structures import Truss2

class Window:
    def __init__(self, screensize :tuple[int, int]=(1080, 720)) -> None:
        self.title :str = "Anatryss"
        self.screensize :tuple[int, int] = screensize

        self.grid :Grid2 = Grid2(framesize=Vector2(*self.screensize))
        self.system :list[Truss2] = list()

        self.running :bool = False

        # initialise pygame
        self.initialise()

    def initialise(self):
        _ = pygame.init()
        pygame.display.set_caption(self.title)
        self.screen :pygame.Surface = pygame.display.set_mode(self.screensize)

    def drawStructs(self):
        for truss in self.system:
            for member in truss.members:
                _ = pygame.draw.line(
                    self.screen,
                    color = "black",
                    start_pos = (member.start.pos * self.grid.gridsize * self.grid.zoom + self.grid.origin).as_tuple(),
                    end_pos = (member.end.pos * self.grid.gridsize * self.grid.zoom + self.grid.origin).as_tuple(),
                    width=3
                )

    def drawFrame(self):
        # clear screen
        _ = self.screen.fill("white")

        xGridlines, yGridlines = self.grid.renderGrid()
        for xpos in xGridlines:
             _  = pygame.draw.line(self.screen, '#a0a0a0', (xpos, 0), (xpos, self.screensize[1]), width=2)
        for ypos in yGridlines:
             _  = pygame.draw.line(self.screen, '#a0a0a0', (0, ypos), (self.screensize[0], ypos), width=2)

        self.drawStructs()

        pygame.display.flip()

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEWHEEL:
                self.grid.shiftGrid(Vector2(10*event.x, -10*event.y))

            pressed = pygame.key.get_pressed()
            # moving the grid
            if pressed[pygame.K_LEFT]:
                self.grid.shiftGrid(Vector2(10, 0))
            if pressed[pygame.K_RIGHT]:
                self.grid.shiftGrid(Vector2(-10, 0))
            if pressed[pygame.K_UP]:
                self.grid.shiftGrid(Vector2(0, 10))
            if pressed[pygame.K_DOWN]:
                self.grid.shiftGrid(Vector2(0, -10))

            # zoom
            if pressed[pygame.K_EQUALS]:
                self.grid.zoom *= 1.10
            if pressed[pygame.K_MINUS]:
                self.grid.zoom *= 0.90


    def run(self):
        self.running = True
        while self.running:
            self.checkEvent()
            self.drawFrame()
        pygame.quit()

if __name__ == '__main__':
    root = Window()

    t = Truss2()
    t.addJoint(Vector2(3, 3), label='A')
    t.addJoint(Vector2(4, 6), label='B')
    t.addJoint(Vector2(6, 6), label='C')
    t.addMember('A', 'B')
    t.addMember('A', 'C')
    t.addMember('B', 'C')
    root.system.append(t)

    root.run()
