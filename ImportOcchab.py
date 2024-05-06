from ImportAbstract import ImportAbstract

class ImportOcchab(ImportAbstract):
    def which_import(self) -> str:
        return "Import Occhab"
    
    def process_transient_data(self) -> None:
        print("[ModuleOcchab] process_transient_data")

    def check_transient_data(self) -> None:
        print("[ModuleOcchab] check_transient_data")

    def import_data_to_destination(self) -> None:
        print("[ModuleOcchab] import_data_to_destination")

    def remove_data_from_destination(self) -> None:
        print("[ModuleOcchab] remove_data_from_destination")

    def report_plot(self) -> None:
        print("[ModuleOcchab] report_plot")

    def compute_bounding_box(self) -> None:
        print("[ModuleOcchab] compute_bounding_box")
