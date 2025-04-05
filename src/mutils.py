from vector import Vector2

class Grid2:
    def __init__(self, framesize :Vector2, gridsize :int = 100):
        self.framesize :Vector2 = framesize

        self.zoom :float = 1
        self.gridsize :int = gridsize

        self.origin :Vector2 = Vector2(0, 0)

    def shiftGrid(self, delta :Vector2):
        self.origin -= delta

    def renderGrid(self) -> tuple[tuple[int, ...], tuple[int, ...]]:
        startX = self.origin.x % (self.gridsize * self.zoom)
        startY = self.origin.y % (self.gridsize * self.zoom)
        return (
            tuple(range(int(startX), int(self.framesize.x - startX + self.zoom*self.gridsize), int(self.zoom * self.gridsize))),
            tuple(range(int(startY), int(self.framesize.y - startY + self.zoom*self.gridsize), int(self.zoom * self.gridsize))),
        )

