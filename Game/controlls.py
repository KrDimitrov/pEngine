from enum import Enum
import pygame.locals
import Game.ecs as ECS

class KeyFunctions(Enum):
    NONE = 0x00
    #ADD KEYS HERE
    STRAFE_RIGHT = 0x01
    STRAFE_LEFT = 0x02


pressed_keys = set()

#TODO make this read json
setting_keys = {
        KeyFunctions.STRAFE_LEFT: 97,
        KeyFunctions.STRAFE_RIGHT: 100
        #KeyFunctions.STRAFE_LEFT: 276,
        #KeyFunctions.STRAFE_RIGHT: 275
        }

def isPressed(key_function):
        return setting_keys.get(key_function, 0x404) in pressed_keys

# MOVEMENT LOGIC

        #No longer check for missing key setting, might add later

def StrafeLeft(velocityX, VelocityCapX, AccelerationX):
    if not velocityX <= -VelocityCapX:
        setattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value, velocityX - AccelerationX)
    ECS.Entity.player_entity.setDirty()
    print(velocityX)
    pass

def StrafeRight(velocityX, VelocityCapX, AccelerationX):
    if not velocityX >= VelocityCapX:
        setattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value, velocityX + AccelerationX)
    ECS.Entity.player_entity.setDirty()
    print(velocityX)
    pass

#TODO implement momentum?
def StrafeSlow(velocityX):
    if velocityX == 0:
        return
    if velocityX < 0:
        setattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value, 0)
    elif velocityX > 0:
        setattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value, 0)
        print("SLOW")
    pass

#checks pressed keys and call their functions
def doKeys():
    #check pressed keys here
    strafe_left_pressed = isPressed(KeyFunctions.STRAFE_LEFT)
    strafe_right_pressed = isPressed(KeyFunctions.STRAFE_RIGHT)

    #TODO get rid of getattr
    velocityX = getattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value)
    velocityY = getattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_Y.value)
    VelocityCapX = getattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_CAP_X.value)
    VelocityCapY = getattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_CAP_Y.value)

    AccelerationX = getattr(ECS.Entity.player_entity, ECS.ComponentNames.ACCELERATION_X.value)
    AccelerationY = getattr(ECS.Entity.player_entity, ECS.ComponentNames.ACCELERATION_Y.value)

    #slow down/stop if no keys pressed (x axis)
    if not strafe_left_pressed and not strafe_right_pressed:
        StrafeSlow(velocityX)
        return

    if strafe_left_pressed:
        StrafeLeft(velocityX, VelocityCapX, AccelerationX)
        pass
    if strafe_right_pressed:
        StrafeRight(velocityX, VelocityCapX, AccelerationX)
        pass




def KeyDown(event):
    pressed_keys.add(event.key)
    #if setting_keys.get(event.key, KeyFunctions.NONE) == KeyFunctions.STRAFE_LEFT:


def KeyUp(event):
    pressed_keys.remove(event.key)





