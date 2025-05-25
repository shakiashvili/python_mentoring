from sqlalchemy import create_engine, select, update, text
from sqlalchemy.orm import sessionmaker
from schema import Base, Films


engine = create_engine('sqlite:///films.db')
Base.metadata.create_all(engine) 


def main() -> None:
    Session = sessionmaker(bind=engine)
    session = Session()

    films = [
        Films(title='Mimino', director='Giorgi Danelia', release_year=1977),
        Films(title='Lord of the rings', director='Peter Jackson', 
              release_year=2003),
        Films(title='Father of soldier', director='Revaz Chkheidze', 
              release_year=1965)
    ]
    session.add_all(films)
    session.commit()

    stmt = update(Films).where(Films.id == 3).values(title='Soldier')
    session.execute(stmt)
    session.commit() 

    stmt = select(Films)
    results = session.execute(stmt)
    for row in results:
        print(row)

    session.execute(text('DELETE FROM films'))
    session.commit()

    session.close()


if __name__ == '__main__':
    main()