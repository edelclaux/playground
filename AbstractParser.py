from typing import List
from AbstractParserParameter import AbstractParserParameter
import json

class AbstractParser():
    __parameters: List[AbstractParserParameter]

    def __init__(self) -> None:
        self.__parameters = []

    def get_id(self) -> str:
        raise NotImplementedError

    def add_parameter(self, parameter: AbstractParserParameter) -> None:
        self.__parameters.append(parameter)

    def detect_parameters_values(self, file) -> None:
        for parameter in self.__parameters:
            parameter.detect_value(file)

    ## #######################################################################
    ## Parameters api
    ## #######################################################################

    def get_parameters_as_json(self):
        return [
            {
                'name': parameter.get_name(),
                'candidates': parameter.get_possible_values(),
                'value': parameter.get_value()
            }

            for parameter in self.__parameters
        ]

    def set_parameters_from_json(self, json):
        # blabla json
        pass

    def print_parameters(self) -> None:
        print(json.dumps(self.get_parameters_as_json(), indent=4))

    ## #######################################################################
    ## parsing
    ## #######################################################################

    def check_file(self, file) -> bool:
        raise NotImplementedError

    def get_fields(self, file) -> List[str]:
        raise NotImplementedError