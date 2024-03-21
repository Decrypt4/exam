from pathlib import Path
from datetime import datetime

from src import Database


path = Path(__name__).parent / 'problems'

def solve(original: Path) -> None:
    db = Database(original)
    db.sort_by_date()
    db.write_to(path / '2.csv')

