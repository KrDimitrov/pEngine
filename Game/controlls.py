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

class PlayerControls(object):
    def __init__(self):
        #No longer check for missing key setting, might add later

    def StrafeLeft(self):
        if not self.velocityX <= -self.VelocityCapX:
            setattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value, self.velocityX - self.AccelerationX)
        ECS.Entity.player_entity.setDirty()
        print(self.velocityX)
        pass

    def StrafeRight(self):
        if not self.velocityX >= self.VelocityCapX:
            setattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value, self.velocityX + self.AccelerationX)
        ECS.Entity.player_entity.setDirty()
        print(self.velocityX)
        pass

    def StrafeSlow(self):
        if self.velocityX == 0:
            return
        if self.velocityX < 0:
            setattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value, 0)
        elif self.velocityX > 0:
            setattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value, 0)
            print("SLOW")
        pass

    #checks pressed keys and call their functions
    def checkKeys(self, pressed_keys):
        #check pressed keys here
        strafe_left_pressed = isPressed(KeyFunctions.STRAFE_LEFT)
        strafe_right_pressed = isPressed(KeyFunctions.STRAFE_RIGHT)

        #wot this? maybe improve?
        self.velocityX = getattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_X.value)
        self.checkKeysvelocityY = getattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_Y.value)
        self.VelocityCapX = getattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_CAP_X.value)
        self.VelocityCapY = getattr(ECS.Entity.player_entity, ECS.ComponentNames.VELOCITY_CAP_Y.value)

        self.AccelerationX = getattr(ECS.Entity.player_entity, ECS.ComponentNames.ACCELERATION_X.value)
        self.AccelerationY = getattr(ECS.Entity.player_entity, ECS.ComponentNames.ACCELERATION_Y.value)

        #slow down/stop if no keys pressed (x axis)
        if not strafe_left_pressed and not strafe_right_pressed:
            self.StrafeSlow()
            return

        if strafe_left_pressed:
            self.StrafeLeft()
            pass
        if strafe_right_pressed:
            self.StrafeRight()
            pass



playerControls = PlayerControls()

def KeyDown(event):
    pressed_keys.add(event.key)
    #if setting_keys.get(event.key, KeyFunctions.NONE) == KeyFunctions.STRAFE_LEFT:


def KeyUp(event):
    pressed_keys.remove(event.key)


def doKeys():
    playerControls.checkKeys(pressed_keys)
    pass



