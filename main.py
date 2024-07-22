from ParserNotFoundError import ParserNotFoundError
from ImportFacade import ImportFacade

files = ["fichier.csv", "fichier.hop", "fichier.geojson"]

for file in files:
    print("\n-- ---------------------------------------------------------------")
    print("-- FILE: " + file)
    print("-- ---------------------------------------------------------------")
    try:
        facade = ImportFacade()
        facade.upload(file)
        data = facade.decode()
    except ParserNotFoundError:
        print("-- Parser not found")
