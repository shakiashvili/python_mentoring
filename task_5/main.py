from schema import Films, FilmsDatabaseManager


def main() -> None:
    try:
        manager = FilmsDatabaseManager()
        film1 = Films(title='Mimino', director='Giorgi Danelia',
                      release_year=1977)
        film2 = Films(title='Lord of the rings', director='Peter Jackson',
                      release_year=2003)
        film3 = Films(title='Father of soldier', director='Revaz Chkheidze',
                      release_year=1965)
        manager.add_film(film1)
        manager.add_film(film2)
        manager.add_film(film3)
        manager.update_film(film1, title='ANY TITLE')
        manager.get_films()
        manager.delete_films()
        manager.get_films()
    finally:
        manager.close_session()


main()
