from ImportAbstract import ImportAbstract

class ImportSynthese(ImportAbstract):

    def which_import(self) -> str:
        return "Import Synthese"

    def process_transient_data(self) -> None:
        print("[ModuleSynthese] process_transient_data")

    def check_transient_data(self) -> None:
        print("[ModuleSynthese] check_transient_data")

    def import_data_to_destination(self) -> None:
        print("[ModuleSynthese] import_data_to_destination")

    def remove_data_from_destination(self) -> None:
        print("[ModuleSynthese] remove_data_from_destination")

    def report_plot(self) -> None:
        print("[ModuleSynthese] report_plot")

    def compute_bounding_box(self) -> None:
        print("[ModuleSynthese] compute_bounding_box")
