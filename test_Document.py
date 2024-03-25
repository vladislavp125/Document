import unittest
from unittest.mock import patch
from Document import Document, InkjetPrinter, LaserPrinter


text = 'Текст документа'


class TestDocument(unittest.TestCase):
    def test_injkt(self):
        text = 'Текст документа'
        injkt = InkjetPrinter()
        doc = Document(injkt)
        with patch('builtins.print') as mocked_print:
            doc.print_document(text)
            mocked_print.assert_any_call("Документ был напечатан на 'Струйном принтере'")
            mocked_print.assert_any_call('Текст документа')

    def test_laser(self):
        text = 'Текст документа'
        laser = LaserPrinter()
        doc1 = Document(laser)
        with patch('builtins.print') as mocked_print:
            doc1.print_document(text)
            mocked_print.assert_any_call("Документ был напечатан на 'Лазерном принтере'")
            mocked_print.assert_any_call('Текст документа')


if __name__ == "__main__":
    unittest.main()