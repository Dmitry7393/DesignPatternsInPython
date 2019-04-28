from exporter import *
from workers import *

def main():
    xml_exporter = XMLExporter()
    json_exporter = JSONExporter()
    developer = Developer()
    developer.export_data(xml_exporter)

    tester = Tester()
    tester.export_data(json_exporter)


if __name__ == "__main__":
    main()