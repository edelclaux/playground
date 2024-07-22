from AbstractParserParameter import AbstractParserParameter
from typing import List
from enum import Enum

class EncodingFormat(str, Enum):
    UTF_8 = "utf-8"
    ISO_8859_1 = "iso-8859-1"
    ISO_8859_15 = "iso-8859-15"

class ParserParameterEncoding(AbstractParserParameter):
    def __init__(self) -> None:
        super(ParserParameterEncoding, self).__init__()
        self.__encoding = EncodingFormat.ISO_8859_1

    def get_name(self) -> str:
        return "Encoding"

    def detect_value(self, file) -> None:
        # GEONATURE
        # with start_sentry_child(op="task", description="detect encoding"):
        #     imprt.detected_encoding = detect_encoding(f)

        self.__encoding = EncodingFormat.UTF_8

    def get_value(self) -> str:
        return self.__encoding

    def get_possible_values(self) -> List[str]:
        return [
            EncodingFormat.UTF_8,
            EncodingFormat.ISO_8859_1,
            EncodingFormat.ISO_8859_15,
        ]