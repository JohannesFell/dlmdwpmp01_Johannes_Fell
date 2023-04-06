import unittest
import controller.check
import model.constants as c
import pandas as pd
from controller.exceptionHandling import FileNotFoundInDirectoryError, TooManyColumnsForVisualization


# eine Testklasse definieren, die die TestCases von unittest erbt
class MyUnitTestCases(unittest.TestCase):

    # eine Testfunktion für die Prüfung, ob die Dateien vorhanden sind
    def test_files_exists(self):
        testFileTrain = controller.check.checkFiles(c.FILE_TRAIN)
        testFileTest = controller.check.checkFiles(c.FILE_TEST)
        testFileIdeal = controller.check.checkFiles(c.FILE_IDEAL)

        self.assertEqual(testFileTrain, True, 'Datei existiert existiert.')
        self.assertEqual(testFileTest, True, 'Datei existiert existiert.')
        self.assertEqual(testFileIdeal, True, 'Datei existiert existiert.')

        # Wir erwarten einen FileNotFoundInDirectoryError, wenn die Datei nicht existiert
        with self.assertRaises(FileNotFoundInDirectoryError):
            controller.check.checkFiles('Error.file')

    def test_count_Columns(self):
        df_test1_OK = pd.DataFrame(columns=['Eins', 'Zwei', 'Drei', 'Vier'])
        list_test2_OK = ['Eins', 'Zwei', 'Drei', 'Vier']

        df_test3_ERROR = pd.DataFrame(columns=['Eins', 'Zwei', 'Drei', 'Vier', 'Fuenf'])
        list_test4_ERROR = ['Eins', 'Zwei', 'Drei', 'Vier', 'Fuenf']

        self.assertEqual(controller.check.checkCount(df_test1_OK, list_test2_OK), True, '4 Spalten/Einträge ist der '
                                                                                        'erwartete Wert für die '
                                                                                        'Visualisierung')

        with self.assertRaises(TooManyColumnsForVisualization):
            controller.check.checkCount(df_test3_ERROR, list_test4_ERROR)


# dieses Skript im unittest-Kontext ausführen
if __name__ == '__main__':
    unittest.main()
