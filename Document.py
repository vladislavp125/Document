class Document:
    def __init__(self, printer):
        self._printer = printer

    def print_document(self):
        self._printer.print_page()


class InkjetPrinter:
    def print_page(self):
        print("Документ был напечатан на 'Струйном принтере'")


class LaserPrinter:
    def print_page(self):
        print("Документ был напечатан на 'Лазерном принтере'")


if __name__ == "__main__":

    #Создаем объекты стратегий
    inkjekt_printer = InkjetPrinter()
    laser_printer = LaserPrinter()

    #Создаем объект документ чтобы напечатать его разными способами
    document1 = Document(laser_printer)
    document2 = Document(inkjekt_printer)

    #Печатаем
    document1.print_document()
    document2.print_document()

