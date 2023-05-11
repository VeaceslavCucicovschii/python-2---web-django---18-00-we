from .entities.User import User
from .entities.Post import Post
from .entities.Comment import Comment
from .entities.Message import Message
from .entities.Reaction import Reaction

from .IdentificationService import IdentificationService


class EntityFactory:
    
    def create(type, params, withId = True):
        
        for each in params:
            if isinstance(params[each], str):
                if params[each] == "":
                    raise TypeError(f"{each} cannot be NULL !!")

        match type:
            case "user":
                user = User(params["username"], params["email"], params["password"])
                
                if withId:
                    user.id = IdentificationService.getId()
            
                return user      
            
            case "post":
                post = Post(params["title"], params["body"], params["authorId"])

                if withId:
                    post.id = IdentificationService.getId()
            
                return post  

            case "comment":
                comment = Comment(params["body"], params["targetId"], params["authorId"])

                if withId:
                    comment.id = IdentificationService.getId()
            
                return comment  

            case "message":
                message = Message(params["body"], params["targetId"], params["authorId"])

                if withId:
                    message.id = IdentificationService.getId()
            
                return message  

            case "reaction":
                reaction = Reaction(params["type"], params["targetId"], params["authorId"])

                if withId:
                    reaction.id = IdentificationService.getId()
            
                return reaction  

            case _:
                raise TypeError(f"EntityFactory cannot create {type} type !!")