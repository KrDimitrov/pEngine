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
        
        PosX = getattr(entity, ECS.ComponentNames.POS_X.value)
        PosY = getattr(entity, ECS.ComponentNames.POS_Y.value)
        VelocityX = getattr(entity, ECS.ComponentNames.VELOCITY_X.value)
        VelocityY = getattr(entity, ECS.ComponentNames.VELOCITY_Y.value)

        setattr(entity, ECS.ComponentNames.POS_X.value, PosX + VelocityX * dt)
        setattr(entity, ECS.ComponentNames.POS_Y.value, PosY + VelocityY * dt)
        entity.setDirty()

