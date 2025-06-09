from flask_jwt_extended import get_jwt_identity
from sqlalchemy.sql import text

class PolicyGuard:
    def __init__(self, db):
        self.db = db

    def has_permission(self, resource, action):
        user_id = get_jwt_identity()
        sql = text("""
            SELECT 1
            FROM user_roles ur
            JOIN policies p ON ur.role_id = p.role_id
            WHERE ur.user_id = :user_id
              AND p.resource = :resource
              AND p.action = :action
            LIMIT 1
        """)
        result = self.db.session.execute(sql, {
            "user_id": user_id,
            "resource": resource,
            "action": action
        }).fetchone()
        return bool(result)
