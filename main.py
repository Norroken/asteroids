# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame           #Imports pygame module
import player

from constants import * #import in variable constants from constants.py

# Main function 
def main():
    pygame.init()   #initiate pygame when the program is run
    fps = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #define screen size by the constants
    player_sprite = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    
    # Main infinite loop that is the body of the game, 
    while True:
        #Event handler for quitting the game
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                return

        
        screen.fill("black") #Sets screen background to black
        player_sprite.draw(screen) #Invokes player every frame
        player_sprite.update(dt)
        pygame.display.flip() #refreshes the scene every loop
        dt = (fps.tick(60)/1000)
        


# ensures main function is only called when the file is run directly 
if __name__ == "__main__":
    main()

