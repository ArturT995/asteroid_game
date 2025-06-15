import pygame
#for smaller projects its fine to use wildcard import(*)
#but on larger projects you could get conflicting import names
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shooting import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x,y)
    
    Shot.containers = (updatable, drawable, shots)
    

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                return
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")


if __name__ == "__main__":
    main()
