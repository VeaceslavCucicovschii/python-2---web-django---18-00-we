from .Entity import Entity
from domain.TimeService import TimeService

class Post(Entity):
    def __init__(self, title, body, authorId):
        super().__init__()
        self.title = title
        self.body = body
        self.createdAt = TimeService.getTime()
        self.updatedAt = self.createdAt
        self.authorId = authorId

    def __str__(self):
        return f"Post < title = {self.title}, body = {self.body}, authorId = {self.authorId} >"
