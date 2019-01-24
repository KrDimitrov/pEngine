import Game.settings
from Game.controlls import doKeys
import Game.ecs as ECS
import pygame.time as time
from collections import deque
# temp
import pygame.image

render_clock = time.Clock()


def init():
    pepega = pygame.image.load("./smol_pepega.png").convert_alpha()
    ECS.Entity(1, [ECS.EntityType.TEXTURED, ECS.EntityType.MOVEABLE, ECS.EntityType.PLAYER_ENTITY], [
        ECS.Component(ECS.ComponentNames.TEXTURE, pepega),
        ECS.Component(ECS.ComponentNames.POS_X, 100.0),
        ECS.Component(ECS.ComponentNames.POS_Y, 150.0),
        ECS.Component(ECS.ComponentNames.VELOCITY_X, 0.0),
        ECS.Component(ECS.ComponentNames.VELOCITY_Y, 0.0),
        ECS.Component(ECS.ComponentNames.ACCELERATION_X, 0.05),
        ECS.Component(ECS.ComponentNames.ACCELERATION_Y, 0),
        ECS.Component(ECS.ComponentNames.VELOCITY_CAP_X, 0.15),
        ECS.Component(ECS.ComponentNames.VELOCITY_CAP_Y, 1)
    ])

    ECS.Entity(2, [ECS.EntityType.TEXTURED, ECS.EntityType.MOVEABLE],
               [
        ECS.Component(ECS.ComponentNames.TEXTURE, pepega),
        ECS.Component(ECS.ComponentNames.POS_X, 10.0),
        ECS.Component(ECS.ComponentNames.POS_Y, 350.0),
        ECS.Component(ECS.ComponentNames.VELOCITY_X, 0.1),
        ECS.Component(ECS.ComponentNames.VELOCITY_Y, 0),
        ECS.Component(ECS.ComponentNames.ACCELERATION_X, 0),
        ECS.Component(ECS.ComponentNames.ACCELERATION_Y, 0),
        ECS.Component(ECS.ComponentNames.VELOCITY_CAP_X, 1),
        ECS.Component(ECS.ComponentNames.VELOCITY_CAP_Y, 1)
    ])


def draw(screen):
    render_clock.tick(Game.settings.fps_limit)
    rects = deque()
    for entity in ECS.Entity.dirty_textured_list:
         if entity.clean_rect != 0:
             rects.append(screen.fill((0, 0, 0), entity.clean_rect))
         rect = screen.blit(entity.texture,
                            (int(entity.PosX),
                             int(entity.PosY)))
         rects.append(rect)
         entity.unsetDirty(rect)
    # TODO this impacts performance heavily! OPTIMIZE!!!!
    pygame.display.update(rects)
    #print(render_clock.get_fps())
    #print(getattr(player, ECS.ComponentNames.VELOCITY_X.value))
    pass
