import pygame

class Window:
    def __init__(self, screensize :tuple[int, int]=(1080, 720)) -> None:
        self.title :str = "Anatryss"
        self.screensize :tuple[int, int] = screensize

        self.running :bool = False
        # initialise pygame
        self.initialise()

    def initialise(self):
        _ = pygame.init()
        pygame.display.set_caption(self.title)
        self.screen :pygame.Surface = pygame.display.set_mode(self.screensize)

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.checkEvent()
        pygame.quit()

if __name__ == '__main__':
    root = Window()
    root.run()
