from app.database.db import SessionLocal


class DatabaseSingleton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.session = SessionLocal()
        return cls._instance

    def get_session(self):
        return self.session

    def close(self):
        self.session.close()
        DatabaseSingleton._instance = None