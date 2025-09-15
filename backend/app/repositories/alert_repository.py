from sqlalchemy.orm import Session

class AlertRepository:
    def __init__(self, db: Session):
        self.db = db
    def get_all(self):
        return []
    def get_by_id(self, id: int):
        return None
