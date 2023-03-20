import sys


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
