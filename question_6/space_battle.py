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

    def defend(self, defender, damage, shield, hull):
        if isinstance(defender, Speeder):
            damage = damage * defender.dodge_attack()  # check if speeder dodges attack
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


def update(ship, shield, hull):
    if hull <= 0:
        print(ship.name, "has been destroyed.", "\n")
        alive_list.remove(ship)
        alive_list_name.remove(ship.name)

        return 0
    else:
        print(ship.name, "has not been destroyed. Shield:", shield, "Hull:", hull, "\n")
        return 1


def diagnostic(spaceship):
    print("///DIAGNOSTIC FOR:", spaceship.name)
    print("/ Laser Power:", spaceship.laser, "/ Shield:", spaceship.shield, "/ Hull:", spaceship.hull, "/")
    print("Type:", type(spaceship), "\n")


def battle_over(total):  # each letter refers to a ship
    if len(total) == 1:
        print(total[0].name, "has won!")
        return 0
    return 1


def random_fight(alive):

    ship_index_attack = random.randint(0, len(alive) - 1)  # choose any of the alive ships
    attacker = alive[ship_index_attack]
    re_add = alive.pop(ship_index_attack)
    ship_index_defend = random.randint(0, len(alive) - 1)  # choose any non-attacking alive ship
    defender = alive[ship_index_defend]
    alive.append(re_add)  # re-add attacker to list of alive ships
    print(attacker.name, "attacks", defender.name, "\n")
    return defender, shot(attacker) * attacker.laser


def shot(attacker):
    if isinstance(attacker, Warship):
        return attacker.high_powered_missile()
    else:
        return 1


if __name__ == "__main__":

    ShipA = Ship("Alfred", 30, 100, 4)  # Ships generated.
    ShipB = Ship("Betty", 30, 100, 4)
    ShipC = Ship("Chris", 30, 100, 4)
    ShipD = Warship("Destroyer", 30, 100, 4)
    ShipE = Speeder("Eager", 30, 100, 4)

    alive_list = [ShipA, ShipB, ShipC, ShipD, ShipE]
    alive_list_name = [ShipA.name, ShipB.name, ShipC.name, ShipD.name, ShipE.name]
    day = 1
    print("Let the games begin! \n ")

    while battle_over(alive_list) == 1:  # main code, battle occurs with one attack per day
        print("Day", day, "// Alive:", alive_list_name)
        defending_ship, damage = random_fight(alive_list)
        defending_ship.shield, defending_ship.hull = Ship.defend(defending_ship,
            defending_ship, damage, defending_ship.shield, defending_ship.hull)
        if update(defending_ship, defending_ship.shield, defending_ship.hull) == 1:  # check if a fatal hit has occurred
            diagnostic(defending_ship)
        day += 1

    print("Battle over.")




