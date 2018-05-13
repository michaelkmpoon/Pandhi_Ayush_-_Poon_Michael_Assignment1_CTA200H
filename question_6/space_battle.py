import random

class Ship:
    """
    This is the main Ship class for all ships, including
    standard spaceships, warships and speeders which each have
    a name, laser power, shield strength and hull strength.
    """

    def __init__(self, name, laser, shield, hull):
        """Basic attributes of each spaceship"""
        self.name = name
        self.laser = laser
        self.shield = shield
        self.hull = hull

    def defend(self, damage, shield, hull):
        if shield > 0:  # shield still exists
            shield -= damage
            if shield < 0:  # if damage breaks shield
                hull += 0.5 * shield
                shield = 0
        else:
            hull += 0.5 * shield  # shield at 0, only hull takes hit
        return shield, hull


class Warship(Ship):
    """
    Warships additionally have high powered missiles which 
    fire 30% of the time.
    """

    def __init__(self, name, laser, shield, hull, missiles):
        super().__init__(name, laser, shield, hull)
        self.missiles = missiles


class Speeder(Ship):
    """
    Speeders additionally dodge 50% of incoming attacks.
    """

    def __init__(self, name, laser, shield, hull, chance):
        super().__init__(name, laser, shield, hull)
        self.chance = chance


def update(name, shield, hull):
    if hull <= 0:
        print(name, " has been destroyed.")
        return 0
    else:
        print(name, "has not been destroyed. Shield:", shield, "Hull:", hull)


ShipA = Ship("Alfred", 30, 100, 100)  # Ships generated.
ShipB = Ship("Betty", 30, 100, 100)
ShipC = Ship("Chris", 30, 100, 100)
ShipD = Warship("Destroyer", 30, 100, 100, 50)
ShipE = Speeder("Eager", 30, 100, 100, 0.5)

ShipA.shield, ShipA.hull = ShipA.defend(ShipB.laser, ShipA.shield, ShipA.hull)

print(ShipA.shield, ShipA.hull)

update(ShipA.name, ShipA.shield, ShipA.hull)




