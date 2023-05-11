from .Entity import Entity
from domain.TimeService import TimeService

class Message(Entity):
    def __init__(self, body, targetId, authorId):
        super().__init__()
        self.body = body
        self.targetId = targetId
        self.authorId = authorId
        self.createdAt = TimeService.getTime()
    
    def __str__(self):
        return f"Message < body = {self.body}, targetId = {self.targetId}, authorId = {self.authorId} >"