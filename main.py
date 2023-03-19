import model.database as database

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

