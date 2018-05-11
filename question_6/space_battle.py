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


class Warship(Ship)
    """
    Warships additionally have high powered missiles which 
    fire 30% of the time.
    """
