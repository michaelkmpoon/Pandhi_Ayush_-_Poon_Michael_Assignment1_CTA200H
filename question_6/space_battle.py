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

    def __init__(self, name, laser, shield, hull):
        super().__init__(name, laser, shield, hull)

    def high_powered_missile(self):
        if random.randint(1, 10) < 4:  # 30% chance of high powered missile
            return 1.3
        return 1


class Speeder(Ship):
    """
    Speeders additionally dodge 50% of incoming attacks.
    """

    def __init__(self, name, laser, shield, hull):
        super().__init__(name, laser, shield, hull)

    def dodge_attack(self):
        if random.randint(1, 10) < 6:  # 50% chance of dodging attack
            return 0
        return 1


def update(name, shield, hull):
    if hull <= 0:
        print(name, " has been destroyed.")
        return 0
    else:
        print(name, "has not been destroyed. Shield:", shield, "Hull:", hull)


def diagnostic(spaceship):
    print("///DIAGNOSTIC FOR:", spaceship.name)
    print("/ Laser Power:", spaceship.laser, "/ Shield:", spaceship.shield, "/ Hull:", spaceship.hull, "/")
    print("Type:", type(spaceship))

def battle_over(A, B, C, D, E):  #  each letter refers to a ship
    total = [A, B, C, D, E]
    death_count = 0
    for each in total:  # check how many ships are destroyed
        if each.hull == 0:
            death_count += 1
        if death_count == 4:
            return 0
        return 1

ShipA = Ship("Alfred", 30, 100, 100)  # Ships generated.
ShipB = Ship("Betty", 30, 100, 100)
ShipC = Ship("Chris", 30, 100, 100)
ShipD = Warship("Destroyer", 30, 100, 100)
ShipE = Speeder("Eager", 30, 100, 100)

print("Let the games begin!")
while battle_over(ShipA, ShipB, ShipC, ShipD, ShipE) == 1:
    print("done")




