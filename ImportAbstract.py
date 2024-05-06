from abc import ABC, abstractmethod

class ImportAbstract(ABC):
    @abstractmethod
    def which_import(self) -> str:
        pass
    @abstractmethod
    def process_transient_data(self) -> None:
        pass

    @abstractmethod
    def check_transient_data(self) -> None:
        pass

    @abstractmethod
    def import_data_to_destination(self) -> None:
        pass

    @abstractmethod
    def remove_data_from_destination(self) -> None:
        pass

    @abstractmethod
    def report_plot(self) -> None:
        pass

    @abstractmethod
    def compute_bounding_box(self) -> None:
        pass
