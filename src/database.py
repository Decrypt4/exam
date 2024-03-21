from datetime import datetime
from typing import List
from pathlib import Path
from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Song:
    id: UUID
    streams: int
    artist_name: str
    track_name: str
    datetime: datetime


class Database:
    """Работа с базой данных песен"""
    def __init__(self, db: Path) -> None:
        self.db = db
        self._content = open(db, 'r+', encoding='utf8').readlines()
        if len(self._content) < 1:
            raise ValueError(
                "Database is empty")

        self._titles = self._content[0].replace("\n", "")
        self._content = self._convert_to_models(self._content[1:])

    def _convert_seconds_to_days(self, seconds: int) -> int:
        """Переводит секунды в дни
        
        :param seconds: общее количество секунд
        :type seconds: int
        :return: количество дней
        """
        return seconds // 60 // 60 // 24

    @property
    def title(self) -> List[str]:
        """Возвращает секцию с названиями колонок таблицы"""
        return self._titles

    @property
    def table(self) -> List[Song]:
        """Возвращает таблицу с данными песни
        
        :return: Список песен
        :return type: List[Song]
        """
        return self._content
    
    def _convert_to_models(self, content: List[str]) -> List[Song]:
        """Возвращает таблицу с данными песни
        
        :return: Список песен
        :return type: List[Song]
        """
        songs = []
        for line in content:
            streams, artist_name, track_name, date = line.split(';')
            day, month, year = tuple(map(int, date.split(".")))
            songs.append(Song(uuid4(), int(streams), artist_name, track_name, datetime(year, month, day)))
        return songs

    def sort_by_date(self, reverse: bool = False) -> None:
        """Сортирует песни по дате (от меньшей даты к большей)
        
        :param reverse: Нужно ли сделать реверс и отсортировать от большой к меньшей
        :type reverse: bool
        """
        ...

    def filter_by_date(self, datetime: datetime, less_than: bool = False, include: bool = False) -> None:
        """Фильтрует песни по дате
        
        :param datetime: Ключевая дата
        :type datetime: datetime
        :param less_than: Отфильтрованные песни должны быть меньше чем ключевая?
        :param less_than: bool
        :param include: Отфильтрованные песни должны включать ключевую?
        :param include: bool
        """
        table = self.table
        self._content = []
        for song in table:
            if not include and song.datetime == datetime:
                continue

            if (less_than and song.datetime <= datetime) \
            or (not less_than and song.datetime >= datetime):
                self._content.append(song)

    def _calc_streams_for_song(self, artist_name: str, track_name: str, date: datetime, static_dt: datetime) -> int:
        """Высчитывает просмотры для указанной песни

        :param artist_name: имя артиста
        :type artist_name: str
        :param track_name: название трека
        :type track_name: str
        :param date: дата релиза
        :type date: datetime
        """
        a = self._convert_seconds_to_days((static_dt - date).total_seconds()) 
        b = len(artist_name) + len(track_name)
        x = int((a / b) * 10000)
        return (x * -1) if x < 0 else x
    
    def calc_streams(self, static_dt: datetime) -> None:
        """Высчитывает просмотры для всех песен таблицы
        
        :param static_dt: параметр для придуманной формулы
        """
        for index, song in enumerate(self.table):
            streams = self._calc_streams_for_song(song.artist_name, song.track_name, song.datetime, static_dt)
            song.streams = streams
            self._content[index] = song

    def _convert_from_model(self, song: Song) -> str:
        """Переводит dataclass в строку
        
        :param song: Объект песни
        :type song: Song 
        """
        dt = f'{song.datetime.day}.{song.datetime.month}.{song.datetime.year}'
        return f"{song.streams};{song.artist_name};{song.track_name};{dt}"

    def write_to(self, path: Path) -> None:
        """Записывает базу данных в указанном пути (должен быть файлом)
        
        :param path: Путь к файлу
        :type path: Path
        """
        content = [self.title]
        for song in self.table:
            content.append(self._convert_from_model(song))

        with open(path, 'w+', encoding='utf8') as file:
            file.write('\n'.join(content))
