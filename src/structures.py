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
    def __init__(self, origin :Vector2) -> None:
        self.origin :Vector2 = origin
        self.joints :dict[str, Joint2] = dict()
        self.members :set[Member2] = set()

    def addJoint(self, pos :Vector2, label :str):
        """ Add a joint to a truss system, wrt to its origin. """
        self.joints[label] = Joint2(pos - self.origin)

    def addMember(self, labelA :str, labelB :str):
        if all([labelA in self.joints, labelB in self.joints]):
            self.members.add(Member2(self.joints[labelA], self.joints[labelB]))
