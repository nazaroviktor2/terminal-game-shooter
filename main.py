import threading
import time
import keyboard

from models.games import GameTerminal
from models.heroes import Hero
from models.weapons import Weapon

# size of game field
N_X = 15
N_Y = 10

# create some weapons
weapon_hero_1 = Weapon("звезда", "*", 1, Weapon.VECTOR_RIGHT, -1, -1)
weapon_hero_2 = Weapon("колесо", "0", 1, Weapon.VECTOR_LEFT, -1, -1)

# create some hero
hero_1 = Hero("Alibo", "A", 0, 0, weapon_hero_1, 3, Hero.COLOR_RED)
hero_2 = Hero("Michelin", "M", 0, N_Y - 1, weapon_hero_2, 3, Hero.COLOR_GREEN)

# create game
game = GameTerminal(N_X, N_Y, hero_1, hero_2)

# start game
play = threading.Thread(target=game.play)
play.start()

# check controllers
while game.get_winner() is None:
    # hero1 move
    if keyboard.is_pressed('w'):
        hero_1.move_up()

    if keyboard.is_pressed('s'):
        hero_1.move_down()

    if keyboard.is_pressed('a'):
        hero_1.move_left()

    if keyboard.is_pressed('d'):
        hero_1.move_right()

    # hero2 move
    if keyboard.is_pressed('up'):
        hero_2.move_up()

    if keyboard.is_pressed('down'):
        hero_2.move_down()

    if keyboard.is_pressed('left'):
        hero_2.move_left()

    if keyboard.is_pressed('right'):
        hero_2.move_right()

    # hero1 shoot
    if keyboard.is_pressed("space"):  # default
        hero_1.to_fire()
        keyboard.block_key("space")

    # hero2 shoot
    if keyboard.is_pressed("right shift") or keyboard.is_pressed("0"):  # default
        hero_2.to_fire()
        keyboard.block_key("right shift")
        keyboard.block_key("0")

    keyboard.unhook_all()
    time.sleep(0.1)
