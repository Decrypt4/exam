from pathlib import Path

from src import Database


path = Path(__name__).parent / 'problems'

def solve(original: Path) -> None:
    db = Database(original)
    artist = input("Введите имя артиста")
    for song in db.table:
        if song.artist_name.lower() == artist.lower():
            print(f"У {song.artist_name} найдена песня: {song.track_name}")
            break
    else:
        print(f"К сожалению, ничего не удалось найти")
    db.write_to(path / '2.csv')

