from pathlib import Path
from datetime import datetime

from src import Database


path = Path(__name__).parent / 'problems'

def solve(original: Path) -> None:
    db = Database(original)
    db.calc_streams(datetime(day=12, month=5, year=23))
    db.write_to(path / 'songs_new.csv')

    db.filter_by_date(datetime(day=1, month=1, year=2002), less_than=True, include=True)
    db.write_to(path / '1.csv')

