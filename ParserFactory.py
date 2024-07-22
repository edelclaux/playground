from AbstractParser import AbstractParser
from ParserCSV import ParserCSV
from ParserGeoJSON import ParserGeoJSON
from ParserNotFoundError import ParserNotFoundError
import pathlib
from enum import Enum
from typing import List

class Format(str, Enum):
    CSV = "csv"
    GEOJSON = "geojson"

class ParserFactory():
    @staticmethod
    def get_parser_from_format(format: str) -> AbstractParser:
        if format == Format.CSV:
            return ParserCSV()
        if format == Format.GEOJSON:
            return ParserGeoJSON()
        raise ParserNotFoundError()

    @staticmethod
    def get_parser_from_file(filepath) -> AbstractParser:
        file_ext = pathlib.Path(filepath).suffix.removeprefix('.')
        return ParserFactory.get_parser_from_format(file_ext)

    @staticmethod
    def get_available_format() -> List[Format]:
        return [
            Format.CSV,
            Format.GEOJSON
        ]
