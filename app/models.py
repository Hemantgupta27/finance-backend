
from sqlalchemy import Column, String, Float, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base
import enum, datetime, uuid

class Role(str, enum.Enum):
    ADMIN="ADMIN"
    ANALYST="ANALYST"
    VIEWER="VIEWER"

class RecordType(str, enum.Enum):
    INCOME="INCOME"
    EXPENSE="EXPENSE"

class User(Base):
    __tablename__="users"
    id = Column(String, primary_key=True, default=lambda:str(uuid.uuid4()))
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(Enum(Role))

class Record(Base):
    __tablename__="records"
    id = Column(String, primary_key=True, default=lambda:str(uuid.uuid4()))
    amount = Column(Float)
    type = Column(Enum(RecordType))
    category = Column(String)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(String, ForeignKey("users.id"))
