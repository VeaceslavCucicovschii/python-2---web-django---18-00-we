from .EntityFactory import EntityFactory
from .IdentificationService import IdentificationService
from .entities.User import User
from .entities.Post import Post

class UserRepository:
    db = {
        "user" : [
            {
                "id" : "1",
                "username" : "jd",
                "email" : "jd@gmail.com",
                "password" : "123jd"
            },
            {
                "id" : "2",
                "username": "mark", 
                "email": "mark@gmail.com", 
                "password": "123mark"
            },
        ],

        "post" : [
            {
                "id" : "1",
                "title" : "new house",
                "body" : "...",
                "authorId" : "1"
            },
            {
                "id" : "2",
                "title" : "traveling",
                "body" : "...",
                "authorId" : "1"
            }
        ],
    }

    def getUser(id):
        for each in UserRepository.db["user"]:
            if each["id"] == id:
                user = EntityFactory.create("user", each, False)
                user.id = each["id"]
                return user

    def getPost(id):
        for each in UserRepository.db["post"]:
            if each["id"] == id:
                post = EntityFactory.create("post", each, False)
                post.id = each["id"]
                return post

    def getUserWithPosts(id):
        user = UserRepository.getUser(id)
        posts = []

        for each in UserRepository.db["post"]:
            if each["authorId"] == id:
                post = EntityFactory.create("post", each, False)
                post.id = each["id"]
                posts.append(post)
            
        user.posts = posts
        return user

    def getPostWithAuthor(id):
        post = UserRepository.getPost(id)
        author = UserRepository.getUser(post.authorId)

        post.author = author
        return post

    def getAllUsers():
        users = []

        for each in UserRepository.db["user"]:
            user = EntityFactory.create("user", each, False)
            user.id = each["id"]
            
            users.append(user)
            
        return users
    
    def getAllPosts():
        posts = []

        for each in UserRepository.db["post"]:
            post = EntityFactory.create("post", each, False)
            post.id = each["id"]
            
            posts.append(post)
            
        return posts
    
    def saveUser(user):
        if type(user) != User:
            raise TypeError("ERROR: saveUser argument must be of User type")
        
        user_data = {
            "id" : user.id,
            "username" : user.username,
            "email" : user.email,
            "password" : user.password,
        }

        UserRepository.db["user"].append(user_data)

    def savePost(post):
        if type(post) != Post:
            raise TypeError("ERROR: savePost argument must be of Post type")
        
        post_data = {
            "id" : post.id,
            "title" : post.title,
            "body" : post.body,
            "authorId" : post.authorId,
        }

        UserRepository.db["post"].append(post_data)

    def updateUser(user):
        for each in UserRepository.db["user"]:
            if each["id"] == user.id:
                each["username"] = user.username
                each["email"] = user.email
                each["password"] = user.password
    
                break

    def updatePost(post):
        for each in UserRepository.db["post"]:
            if each["id"] == post.id:
                each["title"] = post.title
                each["body"] = post.body
                each["authorId"] = post.authorId
    
                break

    def deleteUser(user):
        for each in UserRepository.db["user"]:
            if each["id"] == user.id:
                UserRepository.db["user"].remove(each)
                break

    def deletePost(post):
        for each in UserRepository.db["post"]:
            if each["id"] == post.id:
                UserRepository.db["post"].remove(each)
                break