from config.database import Base
from sqlalchemy import Column, String, Integer

class Command(Base):

    __tablename__ = "commands"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    category = Column(String)