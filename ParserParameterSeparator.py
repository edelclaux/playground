from AbstractParserParameter import AbstractParserParameter
from typing import List
from enum import Enum

class Separator(str, Enum):
    COMMA = ","
    SEMICOLON = ";"

class ParserParameterSeparator(AbstractParserParameter):
    def __init__(self) -> None:
        super(ParserParameterSeparator, self).__init__()
        self.__separator = Separator.SEMICOLON

    def get_name(self) -> str:
        return "Separator"

    def get_possible_values(self) -> List[str]:
        return [
            Separator.COMMA,
            Separator.SEMICOLON
        ]

    def get_value(self) -> str:
        return self.__separator

    def detect_value(self, file) -> None:
        # GEONATURE
        # with start_sentry_child(op="task", description="detect separator"):
        # imprt.detected_separator = detect_separator(
        #     f,
        #     encoding=imprt.encoding or imprt.detected_encoding,
        # )
        self.__separator = Separator.COMMA