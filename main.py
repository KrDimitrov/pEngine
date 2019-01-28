import pygame
from Game import settings as Settings
from Game import renderer as Renderer
from Game.events import handle as HandleEvent
import Game.gametime

#


def main():
    pygame.init()


    pygame.display.set_caption(Settings.window_caption)
    screen = pygame.display.set_mode(Settings.window_size, pygame.DOUBLEBUF)

    #TODO make this level dependant, aka, multiple level support and shit
    Renderer.init()

    while Settings.gameRenderer_running:
        for event in pygame.event.get():
            HandleEvent(event)
        Game.gametime.tick()
        Renderer.draw(screen)

    pygame.quit()


if __name__ == "__main__":
    main()

