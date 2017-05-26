from zsl.db.model.raw_model import ModelBase

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey, String
from sqlalchemy.orm import relationship

from time_tracker.models.serializable import TimeEntry as TimeEntryAppModel
from time_tracker.models.serializable import User as UserAppModel

Base = declarative_base(cls=ModelBase)


class User(Base):
    __app_model__ = UserAppModel

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    fullname = Column(String)
    email = Column(String)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}', fullname=" \
               f"'{self.fullname}')>"


class TimeEntry(Base):
    __app_model__ = TimeEntryAppModel

    __tablename__ = 'time_entry'

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    what = Column(Text)
    user_id = Column(Integer, ForeignKey(User.id))

    user = relationship('User')

    def __repr__(self):
        return f"<TimeEntry(id={self.id}, start_time='{self.start_time}'," \
               f"end_time='{self.end_time}', what='{self.what}')>"




