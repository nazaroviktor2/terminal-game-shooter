"""Models weapons."""


class Weapon(object):
    """Class for basic ranged weapon."""

    VECTOR_UP = "UP"
    VECTOR_DOWN = "DOWN"
    VECTOR_RIGHT = "RIGHT"
    VECTOR_LEFT = "LEFT"

    def __init__(self, name: str, icon: str, damage: int, vector: str, pos_x: int, pos_y: int) -> None:
        """Create a weapon.

        Args:
            name: str - name of the weapon.
            icon: str - a symbol for display.
            damage: int - the weapons' damage.
            vector: str - motion vector.
            pos_x: int - position by x of the weapon.
            pos_y: int - position by y of the weapon.
        """
        self.__pos_y = pos_y
        self.__pos_x = pos_x
        self.damage = damage
        self.vector = vector
        self.name = name
        self.icon = icon

    def move(self):
        """Change position of the weapon by vector."""
        if self.vector == Weapon.VECTOR_UP:
            self.__pos_x -= 1

        elif self.vector == Weapon.VECTOR_DOWN:
            self.__pos_x += 1

        elif self.vector == Weapon.VECTOR_LEFT:
            self.__pos_y -= 1

        elif self.vector == Weapon.VECTOR_RIGHT:
            self.__pos_y += 1

    def getter_pos_x(self):
        """Get current value of pos_x.

        Returns:
            float - current value of pos_x.
        """
        return self.__pos_x

    def setter_pos_x(self, pos_x):
        """Setter for pos_x.

        Args:
            pos_x: float - new value for pos_x.

        Raises:
            ValueError : if new value not be integer.
        """
        try:
            self.__pos_x = int(pos_x)
        except ValueError:
            raise ValueError("Pos_x must be int, not {0}".format(type(pos_x)))

    def getter_pos_y(self):
        """Get current value of pos_y.

        Returns:
            float - current value of pos_y.
        """
        return self.__pos_y

    def setter_pos_y(self, pos_y):
        """Setter for pos_y.

        Args:
            pos_y: float - new value for pos_y.

        Raises:
            ValueError : if new value not be integer.
        """
        try:
            self.__pos_y = int(pos_y)
        except ValueError:
            raise ValueError("Pos_y must be int, not {0}".format(type(pos_y)))

    pos_x = property(getter_pos_x, setter_pos_x)
    pos_y = property(getter_pos_y, setter_pos_y)
