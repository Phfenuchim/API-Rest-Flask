from modules.access_control.service.base_service import BaseService
from modules.users.repositories.user_repository import UserRepository

class UserService(BaseService):
    def __init__(self, db):
        super().__init__(UserRepository(db))
        
    def authenticate_user(self, username, password):
        user = self.repository.get_by_username(username)
        if user and user.verify_password(password):
            return user
        return None