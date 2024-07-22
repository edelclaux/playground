from typing import List
class AbstractParserParameter():
    def __init__(self) -> None:
        pass

    def get_name(self) -> str:
        raise NotImplementedError

    def get_value(self) -> str:
        raise NotImplementedError

    def get_possible_values(self) -> List[str]:
        raise NotImplementedError

    def detect_value(self, file) -> None:
        raise NotImplementedError