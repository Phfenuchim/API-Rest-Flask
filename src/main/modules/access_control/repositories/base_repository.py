# src/main/modules/api_paysmart/repositories/base_repository.py

class BaseRepository:
    def __init__(self, model, db):
        self.model = model
        self.db = db

    def get(self, id):
        return self.model.query.get(id)

    def list(self):
        return self.model.query.all()

    def create(self, data):
        obj = self.model(**data)
        self.db.session.add(obj)
        self.db.session.commit()
        return obj

    def update(self, obj, data):
        for key, value in data.items():
            setattr(obj, key, value)
        self.db.session.commit()
        return obj

    def delete(self, obj):
        self.db.session.delete(obj)
        self.db.session.commit()

