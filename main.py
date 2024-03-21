from pathlib import Path

from problems import p1, p2, p3, p4, p5

root_path = Path(__name__).parent 
original_db = root_path / 'songs.csv'

def main() -> None:
    for p in (p1, p2, p3, p4, p5):
        p.solve(original_db)

if __name__ == "__main__":
    main()
