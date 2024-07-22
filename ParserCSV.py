from AbstractParserText import AbstractParserText
from ParserParameterSeparator import ParserParameterSeparator
from typing import List

class ParserCSV(AbstractParserText):
    def __init__(self) -> None:
        super(ParserCSV, self).__init__()
        self.add_parameter(ParserParameterSeparator())

    def get_id(self) -> str:
        return "csv"

    ## #######################################################################
    ## parsing
    ## #######################################################################

    def check_file(self, file):
        # GEONATURE
        # csvfile = TextIOWrapper(BytesIO(imprt.source_file), encoding=imprt.encoding)
        # csvreader = csv.reader(csvfile, delimiter=imprt.separator)
        # try:
        #     while True:  # read full file to ensure that no encoding errors occur
        #         next(csvreader)
        # except UnicodeError:
        #     raise BadRequest(
        #         description="Erreur d’encodage lors de la lecture du fichier source. "
        #         "Avez-vous sélectionné le bon encodage de votre fichier ?"
        #     )
        # except StopIteration:
        #     pass
        pass

    def get_fields(self, file) -> List[str]:
        # GEONATURE
        # csvfile = TextIOWrapper(BytesIO(imprt.source_file), encoding=imprt.encoding)
        # csvreader = csv.reader(csvfile, delimiter=imprt.separator)
        # columns = next(csvreader)
        return ["column1", "column2"]