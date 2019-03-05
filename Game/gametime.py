import Game.settings as Settings
import Game.ecs as ECS
import Game.controlls
import pygame.time as time

game_clock = time.Clock()

def tick():
  dt = game_clock.tick(0)
  Game.controlls.doKeys()
  doMovement(dt)

# moves all entities by their velocity
def doMovement(dt):
    for entity in ECS.Entity.moveable_list:
        
        PosX = entity.POS_X
        PosY = entity.POS_Y
        VelocityX = entity.VELOCITY_X
        VelocityY = entity.VELOCITY_Y

        entity.POS_X = PosX + VelocityX * dt
        entity.POS_Y = PosY + VelocityY * dt
        entity.setDirty()

