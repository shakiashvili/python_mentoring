import logging
from sqlalchemy import create_engine, Column, Integer, String
from typing import List, Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from logging_cfng import logs_config as conf


Base = declarative_base()
conf()


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)

    def __repr__(self):
        return f"""<Film(id={self.id}, title='{self.title}',
        director='{self.director}',
        release_year={self.release_year})>"""


class FilmsDatabaseManager:
    def __init__(self, db_name):
        self.dbname = db_name
        self.engine = create_engine(f"sqlite:///{db_name}")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)

    def add_film(self, film: Films) -> None:
        self.session.add(film)
        self.session.commit()
        logging.info(f'Film {film.title} is added')

    def get_films(self) -> List[Films]:
        films_list = self.session.query(Films).all()
        for film in films_list:
            logging.info(f"Film {film.title} directer by {film.director}")
        if not films_list:
            return []

    def delete_films(self) -> None:
        self.session.query(Films).delete()
        self.session.commit()
        logging.info("All Films are deleted")

    def update_film(self, film: Films, **kwargs) -> None:
        to_be_updated_film = self.__search_film(film)
        if to_be_updated_film:
            for key, value in kwargs.items():
                setattr(to_be_updated_film, key, value)
            self.session.commit()
        else:
            logging.error('Film is not found in the database')

    def __search_film(self, film: Films) -> Optional[Films]:
        return self.session.query(Films).filter_by(
            title=film.title, director=film.director,
            release_year=film.release_year).first()

    def close_session(self) -> None:
        self.session.close()
