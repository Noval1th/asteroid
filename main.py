import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version:{pygame.version.ver}. \nScreen size: \nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    gameClock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        gameClock.tick(60)
        dt = gameClock.tick(60)/1000.0
        
        


if __name__ == "__main__":
    main()
