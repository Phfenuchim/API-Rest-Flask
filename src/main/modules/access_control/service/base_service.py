class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get(self, id):
        return self.repository.get(id)

    def list(self):
        return self.repository.list()

    def create(self, data):
        return self.repository.create(data)

    def update(self, id, data):
        obj = self.repository.get(id)
        return self.repository.update(obj, data)

    def delete(self, id):
        obj = self.repository.get(id)
        return self.repository.delete(obj)
