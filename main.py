# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# Importing note with example:
# import the connect_database function
# and the database_version variable from database.py into the current file
# from database import connect_database, database_version
# you can also use * to import everything (from database import *), but it's not
#reccomended as it makes the code harder to read and debug


from constants import *


def main():
    pygame.init()
    #for smaller projects its fine to use wildcard import(*)
    #but on larger projects you could get conflicting import names
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while screen == screen:
        pygame.fill(0,0,0)
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")


if __name__ == "__main__":
    main()
