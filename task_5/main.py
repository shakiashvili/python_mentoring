from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base
from schema import FilmsDatabaseManager as Films


engine = create_engine('sqlite:///films.db')
Base.metadata.create_all(engine) 


def main() -> None:
    Session = sessionmaker(bind=engine)
    session = Session()

    Films.create(db_session=session, title='Mimino',
                 director='Giorgi Danelia', release_year=1977)
    Films.create(db_session=session, title='Lord of the rings', 
                 director='Peter Jackson', release_year=2003)
    Films.create(db_session=session, title='Father of soldier',
                 director='Revaz Chkheidze', release_year=1965)

    Films.update(db_session=session, film_id=1, title='Mmino')
    Films.get_all(db_session=session)
    Films.delete(db_session=session)
    session.close()


main()