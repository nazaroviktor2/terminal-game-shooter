"""Models games."""

import os
import time

from colorama import Style

from .heroes import Hero


class GameTerminal:
    """Class for terminal shooter game."""

    EMPTY_SIM = " "
    TIME_TO_UPDATE_GAME_FIELD = 0.07

    def __init__(self, size_x: int, size_y: int, hero1: Hero, hero2: Hero):
        """Create a game.

        Args:
            size_x:int - size game field by x (height).
            size_y:int - size game field by y (weight).
            hero1: Hero - player one hero.
            hero2: Hero - player two hero.
        """
        self.size_x = size_x
        self.size_y = size_y
        self.hero1 = hero1
        self.hero2 = hero2
        self.__field = [[GameTerminal.EMPTY_SIM] * size_y for _ in range(size_x)]  # create empty game field
        self.__winner = None

    def generate_empty_field(self):
        """Generate game field with empty symbol."""
        self.__field = [[GameTerminal.EMPTY_SIM] * self.size_y for _ in range(self.size_x)]

    def spawn_heroes(self):
        """Add heroes to game field."""
        for hero in self.hero1, self.hero2:

            # check if hero out of the game field
            if hero.pos_x > self.size_x - 1:
                hero.pos_x = self.size_x - 1
            elif hero.pos_x < 0:
                hero.pos_x = 0
            if hero.pos_y > self.size_y - 1:
                hero.pos_y = self.size_y - 1
            elif hero.pos_y < 0:
                hero.pos_y = 0
            self.__field[hero.pos_x][hero.pos_y] = hero.short_name[0]  # firth symbol

    def spawn_used_weapons(self):
        """Add used weapons to game field."""
        # hero1 weapons
        for weapon in self.hero1.get_used_weapons():
            weapon.move()  # weapon every time moves

            #  if weapon hits hero2
            if weapon.pos_x == self.hero2.pos_x and weapon.pos_y == self.hero2.pos_y:
                self.hero2.health -= weapon.damage

                # TODO add to weapon bool field penetration if the weapon can pass through the target
                penetration = True
                if not penetration:
                    # the weapon doesn't penetration, so after the hit is destroyed
                    self.hero1.to_destroy_weapon(weapon)

            # if weapon into game field
            elif 0 <= weapon.pos_x < self.size_x and 0 <= weapon.pos_y < self.size_y:
                self.__field[weapon.pos_x][weapon.pos_y] = weapon.icon

            # if weapon out of the game field
            else:
                self.hero1.to_destroy_weapon(weapon)

        # hero2 weapons
        for weapon2 in self.hero2.get_used_weapons():
            weapon2.move()  # weapon every time moves

            #  if weapon hits hero1
            if weapon2.pos_x == self.hero1.pos_x and weapon2.pos_y == self.hero1.pos_y:
                self.hero1.health -= weapon2.damage
                # TODO add to weapon bool field penetration if the weapon can pass through the target
                penetration = True
                if not penetration:
                    # the weapon doesn't penetration, so after the hit is destroyed
                    self.hero2.to_destroy_weapon(weapon2)

            # if weapon into game field
            elif 0 <= weapon2.pos_x < self.size_x and 0 <= weapon2.pos_y < self.size_y:
                self.__field[weapon2.pos_x][weapon2.pos_y] = weapon2.icon

            # if weapon out of the game field
            else:
                self.hero2.to_destroy_weapon(weapon2)

    def display_field(self):
        """Display game field to shell."""
        for index, hero in enumerate([self.hero1, self.hero2]):
            print(hero.display_color + "Герой {0}: ".format(index + 1) + str(hero))
        print(Style.RESET_ALL)
        for field_value in self.__field:
            print(" ".join(map(str, field_value)))

    def check_for_win(self):
        """Check someone wins."""
        if self.hero1.health == 0 and self.hero2.health > 0:
            self.__winner = self.hero2.name
            return True

        elif self.hero2.health == 0 and self.hero1.health > 0:
            self.__winner = self.hero1.name
            return True

        elif self.hero2.health == 0 and self.hero1.health == 0:
            self.__winner = "ничья"
            return True
        return False

    def play(self):
        """Runs game into shell."""
        while self.__winner is None:
            os.system('clear')
            self.generate_empty_field()
            self.spawn_heroes()
            self.spawn_used_weapons()
            self.check_for_win()
            self.display_field()
            time.sleep(GameTerminal.TIME_TO_UPDATE_GAME_FIELD)

        print("Победитель {0}".format(self.__winner))

    def get_winner(self) -> str:
        """Return game winner.

        Returns:
            str - player's name who win
        """
        return self.__winner
