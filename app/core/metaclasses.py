
from datetime import datetime
from abc import ABCMeta


class ModelMeta(ABCMeta):

    def __new__(cls, name, bases, attrs):

        attrs["created_at"] = datetime.now()
        attrs["updated_at"] = datetime.now()

        return super().__new__(cls, name, bases, attrs)
