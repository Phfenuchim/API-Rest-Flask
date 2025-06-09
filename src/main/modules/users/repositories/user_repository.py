from modules.access_control.repositories.base_repository import BaseRepository
from modules.users.domain.user_model import User

class UserRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(User, db)

    def get_by_username(self, username):
        return self.model.query.filter_by(username=username).first()