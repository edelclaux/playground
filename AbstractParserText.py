from AbstractParser import AbstractParser
from ParserParameterEncoding import ParserParameterEncoding
from ParserParameterSeparator import ParserParameterSeparator

class AbstractParserText(AbstractParser):
    def __init__(self) -> None:
        super(AbstractParserText, self).__init__()
        self.add_parameter(ParserParameterEncoding())