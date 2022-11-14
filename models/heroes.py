"""Models of heroes."""

from colorama import Style, Fore

from .weapons import Weapon


class Hero:
    """Class for basic hero."""

    COLOR_DEFAULT = Style.NORMAL
    COLOR_RED = Fore.RED
    COLOR_GREEN = Fore.GREEN

    VECTOR_UP = "UP"
    VECTOR_DOWN = "DOWN"
    VECTOR_RIGHT = "RIGHT"
    VECTOR_LEFT = "LEFT"

    def __init__(self, name: str, short_name: str, pos_x: int, pos_y: int, weapon: Weapon, ammunition: int,
                 display_color: str, health: int = 3):
        """Create a hero.

        Args:
            name: str - name of the weapon.
            short_name: str - a symbol for display.
            pos_x: int - position by x of the weapon.
            pos_y: int - position by y of the weapon.
            weapon: Weapon - hero's weapon.
            ammunition: int - how many shots can the hero fire.
            display_color: str - color for display.
            health: int - hero's health.
        """
        self.ammunition = ammunition
        self.weapon = weapon
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.name = name
        self.short_name = short_name
        self.health = health
        self.__WEAPONS_USED = []
        self.display_color = display_color
        self.__last_move_vector = None

    def __str__(self):
        """Makes hero to str."""
        current_ammunition = self.ammunition - len(self.__WEAPONS_USED)
        return "{0}: оружие - {1}({4}), {2}  {3}".format(self.name, self.weapon.name, '❤' * self.health,
                                                         self.weapon.icon * current_ammunition,
                                                         self.weapon.damage)

    def move_down(self):
        """Change hero's position to a lower one."""
        self.__pos_x += 1
        self.__last_move_vector = Hero.VECTOR_DOWN

    def move_up(self):
        """Change hero's position to an upper one."""
        self.__pos_x -= 1
        self.__last_move_vector = Hero.VECTOR_UP

    def move_right(self):
        """Change hero's position to a right one."""
        self.__pos_y += 1
        self.__last_move_vector = Hero.VECTOR_RIGHT

    def move_left(self):
        """Change hero's position to a left one."""
        self.__pos_y -= 1
        self.__last_move_vector = Hero.VECTOR_LEFT

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

    def to_destroy_weapon(self, weapon: Weapon):
        """Destroy used weapon.

        Args:
            weapon: Weapon - some used weapon.
        """
        if weapon in self.__WEAPONS_USED:
            self.__WEAPONS_USED.remove(weapon)

    def to_fire(self, vector: str = None):
        """Create new hero's weapon.

        Args:
            vector:str - weapon motion vector.
        """
        if len(self.__WEAPONS_USED) < self.ammunition:  # if the hero have free ammunition
            if vector is None:
                # TODO weapon's vector must be last hero move's vector (DONE)
                vector = self.__last_move_vector  # basic hero vector
            new_weapon = Weapon(name=self.weapon.name,
                                icon=self.weapon.icon,
                                damage=self.weapon.damage,
                                vector=vector,
                                pos_x=self.__pos_x,
                                pos_y=self.pos_y
                                )
            new_weapon.move()  # after spawn immediately moves
            self.__WEAPONS_USED.append(new_weapon)  # add to used weapons

    def get_used_weapons(self):
        """Get current used weapons.

        Returns:
            list - list of used weapons.
        """
        return self.__WEAPONS_USED

    pos_x = property(getter_pos_x, setter_pos_x)
    pos_y = property(getter_pos_y, setter_pos_y)
