from sqlalchemy import Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)

    def __repr__(self):
        return f"""Film: {self.title}, Director: {self.director}, 
        Release Year {self.release_year}, ID: {self.id}"""
