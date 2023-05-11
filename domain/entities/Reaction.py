from .Entity import Entity
from domain.TimeService import TimeService

class Reaction(Entity):
    def __init__(self, type, targetId, authorId):
        super().__init__()
        self.type = type
        self.targetId = targetId
        self.authorId = authorId
        self.createdAt = TimeService.getTime()
    
    def __str__(self):
        return f"Reaction < type = {self.type}, targetId = {self.targetId}, authorId = {self.authorId} >"