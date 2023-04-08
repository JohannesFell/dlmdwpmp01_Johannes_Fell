import pandas as pd
import sqlalchemy as db
import model.constants as c


class Database:

    def __init__(self, conn_str, connection):
        self.conn_str = conn_str
        self.connection = connection

    def connectToDb(self):
        engine = db.create_engine(self.conn_str) 
        print('Engine: ', engine)

        # DB Verbindungsobjekt
        connection = engine.connect()
        self.connection = connection

        return self.connection

    def loadDataToDatabase(self, tablename, data):
        """
        Daten in die übergebene Tabelle laden
        :param tablename: Tabellennamen
        :param data: Dateinamen
        :return: NONE
        """

        if not isinstance(data, pd.DataFrame):
            # .csv-Datei in Tabelle laden
            df = pd.read_csv(data)
        else:
            df = data

        df.to_sql(con=self.connection.engine, name=tablename, if_exists='replace', index=False)

    def get_dataframe_from_Db(self, tablename):
        """
        Daten aus Datenbanktabelle laden
        :param tablename: Tabellennamen
        :return: Dataframe des Inhaltes der Tabelle
        """
        table_df = pd.read_sql_table(
            tablename,
            self.connection.engine
        )
        table_df.set_index(c.COLUMN_X, inplace=True)
        return table_df
