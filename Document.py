class Document:
    def __init__(self, printer):
        self._printer = printer

    def print_document(self, text):
        self._printer.print_page(text)


class InkjetPrinter:
    def print_page(self, text):
        print("Документ был напечатан на 'Струйном принтере'")
        print(text)


class LaserPrinter:
    def print_page(self, text):
        print("Документ был напечатан на 'Лазерном принтере'")
        print(text)


if __name__ == "__main__":
    text = 'Текст документа'
    #Создаем объекты стратегий
    inkjekt_printer = InkjetPrinter()
    laser_printer = LaserPrinter()

    #Создаем объект документ чтобы напечатать его разными способами
    document1 = Document(laser_printer)
    document2 = Document(inkjekt_printer)

    #Печатаем
    document1.print_document(text)
    document2.print_document(text)

