import math
import sys
import pandas as pd


def find_best_fits(fct, lst_best_fits, df_train, df_ideal):
    """
    Funktion zur Ermittlung der 'best Fits' aus den übergebenen idealen Funktionen mittels der übergebenen
    Trainingsdatensätze.
    Kriterium der Selektion: Least Square
    :param fct: Funktion aus Trainingsdatensatz
    :param lst_best_fits: Liste in welche die best Fits gespeichert werden
    :param df_train: Trainingsdatensatz (Dataframe)
    :param df_ideal: Datensatz der idealen Funktionen (Dataframe)
    :return: Liste mit den best Fits (Funktionen-/Spaltennamen)
    """
    least_square_min = sys.maxsize

    for column in df_ideal.columns:
        lst_quadAbweichung = []

        for row in df_train.index:
            quadAbweichung = (df_train[fct][row] - df_ideal[column][row]) ** 2
            lst_quadAbweichung.append(quadAbweichung)

        sumQuadAbweichung = sum(lst_quadAbweichung)

        if sumQuadAbweichung < least_square_min:
            least_square_min = sumQuadAbweichung
            ideal_fct = column

    lst_best_fits.append(ideal_fct)
    # TODO DELETE LOG
    print('best fit für Trainingsfunktion ' + fct + ' ist: ' + ideal_fct)

    return lst_best_fits


def validate_selection(lst_best_fits, df_ideal):
    """
    Zur Validierung der Selektion der in find_best_fits() ermittelten Funktionen (aus dem Trainingssatz) wird
    in dieser Methode für jede dieser best Fits durch alle Funktionen des Testdatensatzes durchiteriert und geprüft,
    ob die Abweichungen zwischen den Funktionen den Faktor sqrt(2) nicht übersteigt.
    :return: Dataframe mit den Werten der Testfunktionen, den dazugehörigen Idealfunktionen (falls vorhanden) und der
    entsprechenden Abweichung (falls vorhanden).
    """
    # test.csv in Dataframe lesen
    df_test = pd.read_csv('test.csv')

    # Daten der ideal.csv für die ermittelten best Fits holen
    data = df_ideal.loc[:, lst_best_fits]

    # Join auf die x-Werte der ermittelten best Fits und der Testfunktionen (csv)
    # um nur die relevanten Daten zu haben
    df_test_ideal = df_test.join(data, on='x')

    # Diff zwischen y Wert auf Test und y wert aus ideal
    for col_ideal in df_test_ideal.columns[2:]:
        for row in df_test_ideal.index:
            # für jeden y wert aus test den y wert aus ideal diff
            diff = abs(df_test_ideal['y'][row] - df_test_ideal[col_ideal][row])

            # darf Faktor sqrt2 nicht übersteigen >>  diff = sqrt(2) ist ok
            if diff <= math.sqrt(2):
                # Neue Spalte in Dataframe für die idealen Funktionen und die Abweichung anlegen
                df_test_ideal.loc[row, 'ideale Fkt'] = col_ideal
                df_test_ideal.loc[row, 'Delta Y'] = diff

    df_test_ideal.rename(columns={'x': 'X-Test', 'y': 'Y-Test'}, inplace=True)
    df_test_ideal.drop(df_test_ideal.columns[2:6], axis=1, inplace=True)

    return df_test_ideal
