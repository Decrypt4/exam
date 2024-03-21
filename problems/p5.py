from pathlib import Path
from datetime import datetime

from src import Database


path = Path(__name__).parent / 'problems'

def solve(original: Path) -> None:
    db = Database(original)
    db.write_to(path / '5.csv')

