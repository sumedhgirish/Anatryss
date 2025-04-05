import pygame

from vector import Vector2
from mutils import Grid2

class Window:
    def __init__(self, screensize :tuple[int, int]=(1080, 720)) -> None:
        self.title :str = "Anatryss"
        self.screensize :tuple[int, int] = screensize

        self.grid :Grid2 = Grid2(framesize=Vector2(*self.screensize))

        self.running :bool = False

        # initialise pygame
        self.initialise()

    def initialise(self):
        _ = pygame.init()
        pygame.display.set_caption(self.title)
        self.screen :pygame.Surface = pygame.display.set_mode(self.screensize)

    def drawFrame(self):
        # clear screen
        _ = self.screen.fill("white")

        xGridlines, yGridlines = self.grid.renderGrid()
        for xpos in xGridlines:
             _  = pygame.draw.line(self.screen, 'black', (xpos, 0), (xpos, self.screensize[1]), width=2)
        for ypos in yGridlines:
             _  = pygame.draw.line(self.screen, 'black', (0, ypos), (self.screensize[0], ypos), width=2)

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
                self.grid.shiftGrid(Vector2(-10, 0))
            if pressed[pygame.K_RIGHT]:
                self.grid.shiftGrid(Vector2(10, 0))
            if pressed[pygame.K_UP]:
                self.grid.shiftGrid(Vector2(0, -10))
            if pressed[pygame.K_DOWN]:
                self.grid.shiftGrid(Vector2(0, 10))

            # zoom
            if pressed[pygame.K_EQUALS]:
                self.grid.zoom *= 1.25
            if pressed[pygame.K_MINUS]:
                self.grid.zoom *= 0.75


    def run(self):
        self.running = True
        while self.running:
            self.checkEvent()
            self.drawFrame()
        pygame.quit()

if __name__ == '__main__':
    root = Window()
    root.run()
