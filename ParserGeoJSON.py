from AbstractParserText import AbstractParserText
from ParserParameterSeparator import ParserParameterSeparator
from typing import List

class ParserGeoJSON(AbstractParserText):
    def __init__(self) -> None:
        super(ParserGeoJSON, self).__init__()

    def get_id(self) -> str:
        return "geojson"

    ## #######################################################################
    ## parsing
    ## #######################################################################

    def check_file(self, file):
        pass

    def get_fields(self, file) -> List[str]:
        return ["column1", "column2"]