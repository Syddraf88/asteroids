import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from shot import Shot
import json

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont(None, 48)
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    high_scores = []
    try:
        with open("champions.json", "r") as f:
            loaded_data = json.load(f)
            if isinstance(loaded_data, list):
                high_scores = loaded_data
            else:
                print("Warning: champions.json content is not a list. Starting with empty high scores. ")
    except FileNotFoundError:
        print("champions.json not found. Starting with empty high scores.")
    except json.JSONDecodeError:
        print("Error decoding champions.json. File might be corrupted. Starting with empty high scores.")
    except Exception as e:
        print(f"An unexpected error occurred loading high scores: {e}. Starting with empty high scores.")


    
    
   
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updatable.update(dt)
           
        for asteroid in asteroids:
           if asteroid.colision(player):
               if len(high_scores) < 5 or score > high_scores[4][1]:
                    initials = input("Enter Initials: ")
                    high_scores.append((initials, score))
                    high_scores = sorted(high_scores, key=lambda x: x[1], reverse=True)[0:5]
               print(f"Game over! You scored {score} points!")
               print("----- HIGH SCORES -----")
               for entry in high_scores:
                        print(f"Player: {entry[0]} Score: {entry[1]}")
               
               try:
                   with open("champions.json", "w") as f:
                    json.dump(high_scores, f)
               except Exception as e:
                   print(f"Failed to save high scores: {e}")
                         
               sys.exit()
               
                    
            
           for shot in shots:
               if asteroid.colision(shot):
                   shot.kill()
                   score += asteroid.split()
        
        screen.fill("black")
        
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (20, 20))

        for obj in drawable:
            obj.draw(screen)

        
        
        pygame.display.flip()
     
        ms_passed = clock.tick(60)
        dt = ms_passed / 1000


if __name__ == "__main__":

    main()