import unittest
from unittest.mock import patch
from Document import Document, InkjetPrinter, LaserPrinter


class TestDocument(unittest.TestCase):
    def test_injkt(self):
        injkt = InkjetPrinter()
        doc = Document(injkt)
        with patch('builtins.print') as mocked_print:
            doc.print_document()
            mocked_print.assert_called_once_with("Документ был напечатан на 'Струйном принтере'")

    def test_laser(self):
        laser = LaserPrinter()
        doc1 = Document(laser)
        with patch('builtins.print') as mocked_print:
            doc1.print_document()
            mocked_print.assert_called_once_with("Документ был напечатан на 'Лазерном принтере'")


if __name__ == "__main__":
    unittest.main()