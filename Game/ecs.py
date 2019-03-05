from enum import Enum
from collections import deque

class Entity:
    player_entity = 0
    textured_list = []
    dirty_textured_list = []
    moveable_list = []
    collidable_list = []
    def setDirty(self):
        if self.dirty: return
        Entity.dirty_textured_list.append(self)
        self.dirty = True
    def unsetDirty(self, rect):
        if not self.dirty: return
        Entity.dirty_textured_list.remove(self)
        self.clean_rect = rect
        self.dirty = False
    def __init__(self, eid, type_list, components_list):
        self.eid = eid
        self.dirty = False
        self.clean_rect = 0
        #Parse Components
        for component in components_list:
            if isinstance(component.componentType, ComponentNames):
                setattr(self, component.componentType.name, component.value)
            elif isinstance(component.componentType, str):
                setattr(self, component.componentType, component.value)
            else:
                raise TypeError("BROKEN ENTITY with eid " + str(eid) +
                        "\n!!The Component name should be either a Component Type, or a string!!")
        #Check if the entity has Positinal components passed, if not raise error
        try:
            getattr(self, ComponentNames.POS_X.name)
            getattr(self, ComponentNames.POS_Y.name)

        except AttributeError:
            raise ValueError("BROKEN ENTITY with eid " + str(self.eid) +
                        "\nThis Entity has a missing Position Component!")
        #Parse types and check for missing type specific components
        for type in type_list:
            if type == EntityType.COLLIDABLE:
                #TODO COLLISION LOGIC AND SHIT
                Entity.collidable_list.append(self)
            if type == EntityType.MOVEABLE:
                try:
                    getattr(self, ComponentNames.VELOCITY_X.name)
                    getattr(self, ComponentNames.VELOCITY_Y.name)
                except AttributeError:
                    raise ValueError("BROKEN ENTITY with eid " + str(self.eid) +
                        "\nMISSING VELOCITY COMPONENTS")
                try:
                    getattr(self, ComponentNames.ACCELERATION_X.name)
                    getattr(self, ComponentNames.ACCELERATION_Y.name)
                except AttributeError:
                    raise ValueError("BROKEN ENTITY with eid " + str(self.eid) +
                        "\nMISSING ACCELERATION COMPONENTS!!! ")
                try:
                    getattr(self, ComponentNames.VELOCITY_CAP_X.name)
                    getattr(self, ComponentNames.VELOCITY_CAP_Y.name)
                except AttributeError:
                    raise ValueError("BROKEN ENTITY with eid " + str(self.eid) +
                        "\nMISSING VELOCITY_CAP COMPONENTS!!")

                Entity.moveable_list.append(self)
            if type == EntityType.TEXTURED:
                try:
                    getattr(self, ComponentNames.TEXTURE.name)
                except AttributeError:
                    raise ValueError("BROKEN ENTITY with eid " + str(self.eid) +
                        "\nMISSING TEXTURE COMPONENT!!!")

                Entity.textured_list.append(self)
            if type == EntityType.PLAYER_ENTITY:
                Entity.player_entity = self
        self.setDirty()


class Component:
    def __init__(self, componentType, value):
        self.componentType = componentType
        self.value = value


class EntityType(Enum):
    MOVEABLE = 1
    TEXTURED = 2
    COLLIDABLE = 3
    PLAYER_ENTITY = 4

class ComponentNames(Enum):
    TEXTURE = "texture"
    POS_X = "PosX"
    POS_Y = "PosY"
    VELOCITY_Y = "VelocityY"
    VELOCITY_X = "VelocityX"
    ACCELERATION_X = "AccelerationX"
    ACCELERATION_Y = "AccelerationY"
    VELOCITY_CAP_X = "VelocityCapX"
    VELOCITY_CAP_Y = "VelocityCapY"

    def __str__(self):
        return self.name



