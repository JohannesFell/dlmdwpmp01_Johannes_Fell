import os
from controller.exceptionHandling import FileNotFoundInDirectoryError, XValuesNotIdenticalError, \
    TooManyColumnsForVisualization


def checkFiles(filename):
    """
    Funktion zur Prüfung, ob im aktuellen Arbeitsverzeichnis die übergebene Datei vorhanden ist.
    :param filename: Dateiname
    :return: True, wenn Datei im Arbeitsverzeichnis vorhanden ist
    """
    directory = os.path.abspath(os.getcwd())

    if not os.path.exists(directory + '/' + filename):
        raise FileNotFoundInDirectoryError('Datei: ' + filename + ' im Verzeichnis ' + directory + ' nicht gefunden!')
    else:
        return True


def checkData(df_train, df_ideal):
    """
    Funktion zur Prüfung, ob die X-Werte der übergebenen Dataframes identisch sind.
    :param df_train: Trainingsdatensatz
    :param df_ideal: Datensatz mit idealen Funktionen
    """
    list_x_values_df_train = df_train.index.tolist()
    list_x_values_df_ideal = df_ideal.index.tolist()

    if not list_x_values_df_train == list_x_values_df_ideal:
        raise XValuesNotIdenticalError('Die X-Werte der Training-Datensätze und die X-Werte der idealen Funktionen '
                                       'sind nicht identisch')


def checkCount(df_train, lst_best_fits):
    """
    Funktion zur Prüfung, ob der übergebene Trainingsdatensatz und die Liste mit den idealen Funktionen
    (Bedingung:Least-Square) 4 Spalten besitzen.
    Sinn der Prüfung ist, die Visualisierung, welche von 4 Funktionen ausgeht.
    :param df_train: Trainingsdatensatz
    :param lst_best_fits: Liste der gefundenen idealen Funktionen unter der Bedingung "Least-Square"
    :return: True, wenn das Dataframe und die Liste eine Länge (Spalten) von 4 aufweisen.
    """
    if not len(df_train.columns) == 4:
        raise TooManyColumnsForVisualization('Zur Visualisierung sind nur 4 Spalten zugelassen. Spalten '
                                             'Trainingsdatensatz: ' + str(len(df_train.columns)))

    if not len(lst_best_fits) == 4:
        raise TooManyColumnsForVisualization('Zur Visualisierung sind nur 4 Spalten zugelassen. Spalten '
                                             'BestFits aus ideale Funktionen: ' + str(len(df_train.columns)))

    return True
