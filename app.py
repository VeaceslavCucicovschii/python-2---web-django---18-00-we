from domain.UserRepositiry import UserRepository
from domain.EntityFactory import EntityFactory

user = UserRepository.getUserWithPosts("1")

print(user.posts)