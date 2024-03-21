from datetime import datetime

from .utils import convert_seconds_to_days


static_dt = datetime(day=12, month=5, year=23)

def calc_streams(artist_name: str, track_name: str, date: datetime) -> int:
    """calc stream by formula
    
    :param artist_name: the artist name
    :type artist_name: str
    :param track_name: the track name
    :type track_name: str
    :param date: date of release
    :type date: datetime
    """
    a = convert_seconds_to_days((static_dt - date).total_seconds()) 
    b = len(artist_name) + len(track_name)
    x = int((a / b) * 10000)
    return (x * -1) if x < 0 else x
