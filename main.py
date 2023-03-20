import model.database as database
import controller.functions
import view.visualize
import controller.check

if __name__ == '__main__':

    # Prüfen ob Dateien existieren
    controller.check.checkFiles('train.csv')
    controller.check.checkFiles('test.csv')
    controller.check.checkFiles('ideal.csv')

    # DB Verbindung herstellen
    __connectionStr__ = 'sqlite:///dlmdwpmp01.db'
    db_instance = database.Database(__connectionStr__, '')
    conn_meta = db_instance.connectToDb()
    metadata = conn_meta[1]

    # Trainings- und Idealfunktionen in DB speichern
    db_instance.loadDataToDatabase('Trainingsfunktionen', 'train.csv')
    db_instance.loadDataToDatabase('Idealfunktionen', 'ideal.csv')

    # Daten aus Datenbank laden
    df_train = db_instance.get_dataframe_from_Db('Trainingsfunktionen')
    df_ideal = db_instance.get_dataframe_from_Db('Idealfunktionen')

    # X-Werte der Trainingsfunktionen und der idealen Funktionen abgleichen
    controller.check.checkData(df_train, df_ideal)

    # best Fits finden (LeastSquare)
    # Liste für die best Fits
    lst_best_fits = []
    for fct in df_train.columns:
        controller.functions.find_best_fits(fct, lst_best_fits, df_train, df_ideal)

    # Validierung der best Fits anhand der Testfunktionen und Speicherung der Abweichung
    result = controller.functions.validate_selection(lst_best_fits, df_ideal)

    # Speichern der Ergebnisse in der DB
    db_instance.loadDataToDatabase('Validierung', result)

    # Outliers und Fits für die Visualisierung ermitteln
    dictionaries = controller.functions.get_outliers(result)

    # Visualisierung der best Fits
    controller.check.checkCount(df_train, lst_best_fits)
    view.visualize.visualize_best_fits(df_train, df_ideal, lst_best_fits)

    # Visualising der validierten Daten und deren Abweichungen
    view.visualize.visualize_results(dictionaries[0], dictionaries[1], df_ideal, lst_best_fits)
