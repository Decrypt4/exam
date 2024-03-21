from datetime import datetime
from pathlib import Path

from src.songs import calc_streams

root_path = Path(__name__).parent 


def main() -> None:
    cond_dt = datetime(year=2002, month=1, day=1)
    with open(root_path / 'songs.txt', 'r+', encoding='utf8') as file:
        lines = file.readlines()[1:]
    
    with open(root_path / 'songs_new.txt', 'a+', encoding='utf8') as file:
        for line in lines:
            streams, artist_name, track_name, date = line.split(';')

            day, month, year = list(map(int, date.split('.')))
            dt = datetime(year=year, month=month, day=day)
            if dt <= cond_dt:
                streams = calc_streams(artist_name, track_name, dt)
                data = (str(streams), artist_name, track_name, date)
                file.write(';'.join(data))



if __name__ == "__main__":
    main()