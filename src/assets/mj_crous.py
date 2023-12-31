import pygame
import os
import math
from sp_Star import Star
import random
import Utils


class mj_crous():
    IMG_BG = pygame.image.load(os.path.dirname(__file__) + "/sprites/images/crous/crous_fond.png")

    def getTimeForLevelCrous(self, level):
        return ((math.e ** (2.5 - (0.25 * level))) * 0.4) + 1.5
    
    def __init__(self, level, screen):
        self.m_level = level
        self.screen = screen

    def run_miniJeu(self):

        #constantes son
        THEME = pygame.mixer.Sound(os.path.dirname(__file__) + "/sounds/gens_qui_parlent.mp3")
        CHANNEL_MJ = pygame.mixer.Channel(2) #son des gens en fond constant
        CHANNEL_MJ.play(THEME, loops=-1)


        # framerate = Utils.getFramerateForLevel(60, self.m_level)
        clock = pygame.time.Clock()
        timer = 0
        max_time = self.getTimeForLevelCrous(self.m_level)
        timer_width = 600
        

        sprite_group = pygame.sprite.Group()
        mid_x = self.screen.get_width() / 2
        mid_y = self.screen.get_height() / 2

        stars = []
        for i in range(self.m_level + 3):
            stars.append(newStar(200, 200, self.screen.get_width()-300,self.screen.get_height()-200, stars))  
        stars[0] = Star(stars[0].rect.x, stars[0].rect.y, True)

        sprite_group.add(stars)
        while (timer < max_time):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                     for sprite in sprite_group:
                        if sprite.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                            #sprite.kill()
                            CHANNEL_MJ.stop()
                            return sprite.type

            self.screen.blit(mj_crous.IMG_BG, (0,0))
            #^ screen.blit du background
            sprite_group.draw(self.screen)

            barre_w = timer_width * (1-(timer/max_time))
            loading_bar_rect = pygame.Rect(mid_x-(timer_width/2), mid_y-250, barre_w, 20)
            pygame.draw.rect(self.screen, "red", loading_bar_rect)
            pygame.draw.rect(self.screen, (0,0,0, 120), loading_bar_rect, 4)
            
            
            pygame.display.flip()
            
            timer += clock.tick(30)/1000
            
        CHANNEL_MJ.stop()
        return False
    

def newStar(tx, ty, dx, dy, o_sprites, deep = 1):
    x = random.randint(tx, dx)
    y = random.randint(ty, dy)
    overlap = [sprite for sprite in o_sprites if sprite.rect.collidepoint((x,y))]
    if (len(overlap) > 0 and deep > 10):
        return newStar(tx, ty, dx, dy, o_sprites, deep+1)
    return Star(x, y)

    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))

    # obj = mj_crous(1)
    # print("Resultat du mini jeu: ", obj.run_miniJeu())

    for i in range(10,20):
        obj = mj_crous(i, screen)
        print(f"Resultat du mini jeu: {obj.run_miniJeu()}")


    pygame.quit()
    print("Ok")
    