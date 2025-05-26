import pygame
from vector import Vector2
from typing import override

class Joint2:
    def __init__(self, position :Vector2) -> None:
        self.pos :Vector2 = position

    @override
    def __hash__(self):
        return hash(self.pos)

class Member2:
    def __init__(self, start :Joint2, end :Joint2) -> None:
        self.start :Joint2 = start
        self.end :Joint2 = end

    @override
    def __hash__(self):
        return hash((self.start, self.end))

class Truss2:
    def __init__(self) -> None:
        self.joints :dict[str, Joint2] = dict()
        self.members :set[Member2] = set()

    def addJoint(self, pos :Vector2, label :str):
        """ Add a joint to a truss system, wrt to its origin. """
        self.joints[label] = Joint2(pos)

    def addMember(self, labelA :str, labelB :str):
        if all([labelA in self.joints, labelB in self.joints]):
            self.members.add(Member2(self.joints[labelA], self.joints[labelB]))

class Block2:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.color = "#000000"

        diff = self.start - self.end
        self.size = Vector2(abs(diff.x), abs(diff.y))
        self.rect = pygame.Rect(self.start.x, self.start.y, self.size.x, self.size.y)

    def draw(self, screen, origin) -> None:
        self.rect.x = self.start.x + origin.x
        self.rect.y = self.start.y + origin.y
        pygame.draw.rect(screen, self.color, self.rect, 5)

    def containsPoint(self, point):
        return self.rect.collidepoint(point.x, point.y)
