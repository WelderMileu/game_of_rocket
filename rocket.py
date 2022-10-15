#!/usr/bin/python3
try:
    import pygame

except Exception as err:
    print(err)

pygame.init()

class Simple:
    def __init__(self):
        self.running = True
        self.screen_width = 700
        self.screen_height = 500
        self.rocket_image = pygame.image.load('./assets/img/rocket-png-40794.png')
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)).convert_alpha()

    def rocket_control(self):
        px = 20
        py = 20
        
        # bug ...
        # is not get my image of rocket
        rect = self.rocket_image.get_rect()
        rect.x = px
        rect.y = py

        self.screen.blit(self.rocket_image, rect)
        pygame.display.flip()

    def window_game(self):
        pygame.display.set_caption('Game of rocket')
        pygame.display.set_icon(self.rocket_image)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            Simple.rocket_control()
            pygame.display.update()

    def init_game(self):
        try:

            Simple.window_game()

        except Exception as err:
            print(err)

if __name__ == '__main__':
    Simple = Simple()
    Simple.init_game()
