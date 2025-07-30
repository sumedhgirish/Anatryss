import pygame

from structures import Block2, Circle2
from vector import Vector2
from mutils import Grid2

class Window:
    def __init__(self, screensize :tuple[int, int]=(800, 600)) -> None:
        self.title :str = "Anatryss"
        self.screensize :tuple[int, int] = screensize

        self.grid :Grid2 = Grid2(framesize=Vector2(*self.screensize))
        self.system = list()
        self.selected = None
        self.pen_mode = None

        self.running :bool = False
        self.last_click = None
        self.is_dragging = False

        # initialise pygame
        self.initialise()

    def initialise(self):
        _ = pygame.init()
        pygame.display.set_caption(self.title)
        self.screen :pygame.Surface = pygame.display.set_mode(self.screensize)

    def createObject(self, start_pos, end_pos):
        if not self.pen_mode:
            return

        match (self.pen_mode):
            case 'block':
                self.system.append(Block2(start_pos, end_pos))
            case 'circle':
                self.system.append(Circle2(start_pos, end_pos))
            case _:
                return

    def checkSelection(self, mousepos):
        for obj in reversed(self.system):
            if obj.containsPoint(mousepos - self.grid.origin):
                self.selected = obj
                break
        else:
            self.selected = None

    def drawFrame(self):
        # clear screen
        _ = self.screen.fill("white")

        xGridlines, yGridlines = self.grid.renderGrid()
        for xpos in xGridlines:
             _  = pygame.draw.line(self.screen, '#a0a0a0', (xpos, 0), (xpos, self.screensize[1]), width=2)
        for ypos in yGridlines:
             _  = pygame.draw.line(self.screen, '#a0a0a0', (0, ypos), (self.screensize[0], ypos), width=2)

        for obj in self.system:
            obj.draw(self.screen, self.grid.origin)
            if obj == self.selected:
                obj.color = "#40e0d0"
            else:
                obj.color = "#000000"

        pygame.display.flip()

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEWHEEL:
                self.grid.shiftGrid(Vector2(10*event.x, -10*event.y))

            # dragging
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.last_click = Vector2(*pygame.mouse.get_pos()) - self.grid.origin
                    self.is_dragging = True
                if event.button == 3:
                    pass

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.is_dragging = False
                    self.createObject(self.last_click, Vector2(*pygame.mouse.get_pos()) - self.grid.origin)
                if event.button == 3:
                    self.checkSelection(Vector2(*pygame.mouse.get_pos()))

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

            # selecting different pen modes
            if pressed[pygame.K_b]:
                self.pen_mode = 'block'
            if pressed[pygame.K_c]:
                self.pen_mode = 'circle'
            if pressed[pygame.K_x]:
                self.pen_mode = None


    def run(self):
        self.running = True
        while self.running:
            self.checkEvent()
            self.drawFrame()
        pygame.quit()

if __name__ == '__main__':
    root = Window()
    root.run()
