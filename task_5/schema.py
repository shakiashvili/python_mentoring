from sqlalchemy import Column, Integer, String, text, delete
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FilmsDatabaseManager(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)

    def __repr__(self):
        return f"""Film: {self.title}, Director: {self.director}, 
        Release Year {self.release_year}, ID: {self.id}"""
    
    @classmethod
    def get_all(cls, db_session) -> str:
        list_of_films = db_session.query(cls).all()
        for i in list_of_films:
            print(i)
    
    @classmethod
    def create(cls, db_session, **kwargs) -> None:
        new_film = cls(**kwargs)
        db_session.add(new_film)
        db_session.commit()
    
    @classmethod
    def delete(cls, db_session) -> None:
        db_session.execute(delete(cls))
        db_session.commit()

    @classmethod 
    def update(cls, db_session, film_id: int, **kwargs) -> None:
        if not kwargs:
            print('No argument is passed')
            return None
        db_session.query(cls).filter(cls.id == film_id).update(kwargs)
        db_session.commit()
