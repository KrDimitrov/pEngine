import pygame.locals, pygame.key
import Game.settings, Game.controlls

def handle(event):
    if(event.type == pygame.QUIT):
        quitGame()
    if(event.type == pygame.KEYDOWN):
        Game.controlls.KeyDown(event)
    if(event.type == pygame.KEYUP):
        Game.controlls.KeyUp(event)
    pass

def quitGame():
    Game.settings.gameTime_running = False
    Game.settings.gameRenderer_running = False

