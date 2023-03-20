import model.database as database
import controller.functions

if __name__ == '__main__':

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

    # best Fits finden (LeastSquare)
    # Liste für die best Fits
    lst_best_fits = []
    for fct in df_train.columns:
        controller.functions.find_best_fits(fct, lst_best_fits, df_train, df_ideal)

    # Validierung der best Fits anhand der Testfunktionen und Speicherung der Abweichung
    result = controller.functions.validate_selection(lst_best_fits, df_ideal)

    # Speichern der Ergebnisse in der DB
    db_instance.loadDataToDatabase('Validierung', result)

