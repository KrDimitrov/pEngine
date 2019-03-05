from enum import Enum
import pygame.locals
import Game.ecs as ECS

class KeyFunctions(Enum):
    NONE = 0x00
    #ADD KEYS HERE
    STRAFE_RIGHT = 0x01
    STRAFE_LEFT = 0x02
    UP = 0x03
    DOWN = 0x04


pressed_keys = set()

#TODO make this read json
setting_keys = {
        KeyFunctions.STRAFE_LEFT: 97,
        KeyFunctions.STRAFE_RIGHT: 100,
        #KeyFunctions.STRAFE_LEFT: 276,
        #KeyFunctions.STRAFE_RIGHT: 275
        KeyFunctions.UP: 119,
        KeyFunctions.DOWN: 115
        }

def isPressed(key_function):
        return setting_keys.get(key_function, 0x404) in pressed_keys

# MOVEMENT LOGIC

        #No longer check for missing key setting, might add later

##### X AXIS
def StrafeLeft(velocityX, VelocityCapX, AccelerationX):
    if not velocityX <= -VelocityCapX:
        ECS.Entity.player_entity.VELOCITY_X = velocityX - AccelerationX
        ECS.Entity.player_entity.setDirty()
    print(velocityX)
    pass

def StrafeRight(velocityX, VelocityCapX, AccelerationX):
    if not velocityX >= VelocityCapX:
        ECS.Entity.player_entity.VELOCITY_X = velocityX + AccelerationX
        ECS.Entity.player_entity.setDirty()
    print(velocityX)
    pass

#TODO implement momentum?
def StrafeSlow(velocityX):
    if velocityX == 0:
        return
    if velocityX < 0:
        ECS.Entity.player_entity.VELOCITY_X = 0
    elif velocityX > 0:
        ECS.Entity.player_entity.VELOCITY_X = 0
        print("SLOW")
    pass

##### Y AXIS
def Up(velocityY, VelocityCapY, AccelerationY):
    if not velocityY <= -VelocityCapY:
        ECS.Entity.player_entity.VELOCITY_Y = velocityY - AccelerationY
        ECS.Entity.player_entity.setDirty()

def Down(velocityY, VelocityCapY, AccelerationY):
    if not velocityY >= VelocityCapY:
        ECS.Entity.player_entity.VELOCITY_Y = velocityY + AccelerationY
        ECS.Entity.player_entity.setDirty()

def SlowY(velocityY):
    if velocityY == 0: return
    if velocityY < 0:
        ECS.Entity.player_entity.VELOCITY_Y = 0
    elif velocityY > 0:
        ECS.Entity.player_entity.VELOCITY_Y = 0
#checks pressed keys and call their functions
def doKeys():
    #check pressed keys here
    strafe_left_pressed = isPressed(KeyFunctions.STRAFE_LEFT)
    strafe_right_pressed = isPressed(KeyFunctions.STRAFE_RIGHT)
    up_pressed = isPressed(KeyFunctions.UP)
    down_pressed = isPressed(KeyFunctions.DOWN)

    #TODO get rid of getatts
    velocityX = ECS.Entity.player_entity.VELOCITY_X
    velocityY = ECS.Entity.player_entity.VELOCITY_Y
    VelocityCapX = ECS.Entity.player_entity.VELOCITY_CAP_X
    VelocityCapY = ECS.Entity.player_entity.VELOCITY_CAP_Y

    AccelerationX = ECS.Entity.player_entity.ACCELERATION_X
    AccelerationY = ECS.Entity.player_entity.ACCELERATION_Y

    #slow down/stop if no keys pressed (x axis)
    if not strafe_left_pressed and not strafe_right_pressed:
        StrafeSlow(velocityX)
    else:
        if strafe_left_pressed: StrafeLeft(velocityX, VelocityCapX, AccelerationX)
        if strafe_right_pressed: StrafeRight(velocityX, VelocityCapX, AccelerationX)
    if not up_pressed and not down_pressed:
        SlowY(velocityY)
    else:
        if up_pressed: Up(velocityY, VelocityCapY, AccelerationY)
        if down_pressed: Down(velocityY, VelocityCapY, AccelerationY)



def KeyDown(event):
    pressed_keys.add(event.key)
    #if setting_keys.get(event.key, KeyFunctions.NONE) == KeyFunctions.STRAFE_LEFT:


def KeyUp(event):
    pressed_keys.remove(event.key)





