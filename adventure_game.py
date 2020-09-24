# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:00:55 2020

@author: John Ouyang
"""


import time
import random


def print_delay(string):
    print(string)
    time.sleep(1)


def selection(message, options):
    choice = input(message)
    if choice not in options:
        choice = selection(message, options)
    return choice


def returnField(armory, enemy_creature, SpecifiedWeapon):
    print_delay("You run back into the field."
                "Luckily, you don't seem to have been followed.")
    playGame(SpecifiedWeapon, armory, enemy_creature)


def victoriousFight(enemy_creature, SpecifiedWeapon):
    print_delay(f"As the {enemy_creature} moves to attack"
                f", you unsheath your new {SpecifiedWeapon}.")
    print_delay(f"The new supreme {SpecifiedWeapon} shines brightly"
                " in your hand as you brace yourself for the attack.")
    print_delay(f"But the {enemy_creature} takes one"
                "look at your shiny new toy and runs away!")
    print_delay(f"You have rid the town of the {enemy_creature}. "
                "You are victorious!")
    print_delay("GAME OVER!")
    AskplayAgain()


def failedFight(enemy_creature):
    print_delay("You do your best...")
    print_delay(f"but your dagger is no match for the {enemy_creature}.")
    print_delay("You have been defeated!")
    print_delay("GAME OVER!")

    AskplayAgain()


def enterHouse(enemy_creature, armory, SpecifiedWeapon):
    print_delay("You approach the door of the house")
    print_delay(f"You are about to knock when the door "
                f"opens and out steps a {enemy_creature}.")
    print_delay(f"Eep! This is the {enemy_creature}'s house!")
    print_delay(f"The {enemy_creature} attacks you!")

    if SpecifiedWeapon in armory:
        Fight_or_Run = selection("Would you like to (1) fight"
                                 " or (2) run away?", ["1", "2"])

        if Fight_or_Run == "1":
            victoriousFight(enemy_creature, SpecifiedWeapon)

        elif Fight_or_Run == "2":
            returnField(armory, enemy_creature, SpecifiedWeapon)

    else:

        print_delay("You feel a bit under-prepared for this"
                    ", what with only having a tiny dagger.")

        Fight_or_Run = selection("Would you like to (1) "
                                 "fight or (2) run away?", ["1", "2"])
        if Fight_or_Run == "1":
            failedFight(enemy_creature)
        elif Fight_or_Run == "2":
            returnField(armory, enemy_creature, SpecifiedWeapon)

    return


def alreadyHaveArmory():
    print_delay("You peer cautiously into the cave.")
    print_delay("You've been here before, and gotten "
                "all the good stuff. It's just an empty cave now.")


def enterCave(armory, enemy_creature, SpecifiedWeapon):
    if SpecifiedWeapon not in armory:
        getSwordinArmory(armory, SpecifiedWeapon)

    else:
        alreadyHaveArmory()

    print_delay("You walk back out to the field.")
    playGame(SpecifiedWeapon, armory, enemy_creature)
    return


def playGame(SpecifiedWeapon, armory, enemy_creature):

    print_delay("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.")
    choice = selection("what would you like to do?\n"
                       "(Please enter 1 or 2).\n", ["1", "2"])
    if choice == "1":
        enterHouse(enemy_creature, armory, SpecifiedWeapon)

    elif choice == "2":
        enterCave(armory, enemy_creature, SpecifiedWeapon)

    return


def getSwordinArmory(armory, SpecifiedWeapon):
    print_delay("You peer cautiously into the cave.")
    print_delay("It turns out to be only a very small cave.")
    print_delay("Your eye catches a glint of metal behind a rock.")
    print_delay(f"You have found the magical {SpecifiedWeapon}!")
    print_delay(f"You discard your silly old dagger "
                f"and take the {SpecifiedWeapon} with you.")
    armory.append(SpecifiedWeapon)


def newGame():
    armory = []
    enemy_creatures = ["dragon", "Thanos", "demon", "bandit", "ogre"]
    enemy_creature = random.choice(enemy_creatures)
    weaponLibrary = ["sword", "katana", "claymore", "Kris sword"]
    SpecifiedWeapon = random.choice(weaponLibrary)

    print_delay("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.  ")
    print_delay(f"Rumor has it that a {enemy_creature} is"
                " somewhere around here, and has been"
                " terrifying the nearby village.")
    print_delay("In front of you is a house.\n"
                "To your right is a dark cave.\n"
                "In your hand you hold your trusty "
                "(but not very effective) dagger.\n")

    playGame(SpecifiedWeapon, armory, enemy_creature)


def AskplayAgain():
    playAgain = selection("Would you like to play again? (y/n)", ["y", "n"])
    if playAgain == "n":
        return
    elif playAgain == "y":
        print_delay("Excellent! Restarting the game ...")
        newGame()


def main():
    newGame()


main()
