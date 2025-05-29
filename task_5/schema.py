from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


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
    def __init__(self):
        self.engine = create_engine('sqlite:///films.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()

    def add_film(self, film: Films) -> None:
        self.session.add(film)
        self.session.commit()
        return film

    def get_films(self) -> list:
        films_list = self.session.query(Films).all()
        for film in films_list:
            print(film)
        if not films_list:
            print(None)

    def delete_films(self) -> None:
        self.session.query(Films).delete()
        self.session.commit()
        print("All Films are deleted")

    def update_film(self, film: Films, **kwargs) -> None:
        to_be_updated_film = self.__search_film_id(film)
        if to_be_updated_film:
            for key, value in kwargs.items():
                setattr(to_be_updated_film, key, value)
            self.session.commit()
            return to_be_updated_film

    def __search_film_id(self, film: Films) -> None:
        return self.session.query(Films).filter_by(
            title=film.title, director=film.director,
            release_year=film.release_year).first()

    def close_session(self) -> None:
        self.session.close()
