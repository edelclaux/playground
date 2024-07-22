from AbstractParser import AbstractParser
from ParserNotFoundError import ParserNotFoundError
from werkzeug.exceptions import BadRequest
from ParserFactory import ParserFactory
from enum import Enum
from typing import List

class ImportFacade():
    def __init__(self) -> None:
        self.__file = None
        self.__parser = None
        self.__fields = []

    def upload(self, file) -> None:
        self.__file = file
        self.__parser = ParserFactory.get_parser_from_file(self.__file)
        print("-- Parser found: " + self.__parser.get_id())
        print("-- Default parameters")
        self.__parser.print_parameters()
        self.__parser.check_file(self.__file)
        self.__parser.detect_parameters_values(self.__file)
        print("-- Detected parameters")
        self.__parser.print_parameters()

    def decode(self):
        if not self.__parser:
            raise ParserNotFoundError
        self.__fields = self.__parser.get_fields(self.__file)
        self.__check_duplicate_fields()

    def __check_duplicate_fields(self) -> None:
        duplicates = set([col for col in self.__fields if self.__fields.count(col) > 1])
        if duplicates:
            raise BadRequest(f"Duplicates column names: {duplicates}")