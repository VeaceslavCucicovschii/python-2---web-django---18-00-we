from .Entity import Entity
from domain.TimeService import TimeService

class User(Entity):
    def __init__(self, username, email, password):
        super().__init__()
        self.username = username
        self.email = email
        self.password = password
        self.registoredAt = TimeService.getTime()
        self.lastLoginAt = self.registoredAt        # no idea how to do (for now)
        self.online = False                         # no idea how to do (for now)
    
    def __str__(self):
        return f"User < username = {self.username}, email = {self.email}, online = {self.online} >"