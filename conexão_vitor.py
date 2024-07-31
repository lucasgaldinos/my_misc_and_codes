import pyodbc


class DatabaseSql():
    def __init__(self):
        print('Loading Database...')
        self.config = Config()
        self.connect()
 
    @property
    def connection(self):
        return self._connection
 
    @property
    def cursor(self):
        return self._cursor
 
    @property
    def error(self):
        try:
            return self._error
        except Exception:
            return None
 
    @error.setter
    def error(self, value):
        self._error = value
 
    def connect(self):
        try:
            connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.config.server + ';DATABASE=' + self.config.database + ';ENCRYPT=yes;UID=' + self.config.username + ';PWD=' + self.config.password + ';TrustServerCertificate=yes')
            self._connection = connection
            self._cursor = self.connection.cursor()
        except Exception as e:
            self._error = f"Não foi possivel connectar ao banco sql, {e}"
 
    def get_all_data(self):
        date = Dates.days_after(1, Dates.today())
        data = pd.read_sql(
            f"SELECT * FROM {self.config.database_checklist} where VERIFICADO <> 1 AND Numero_Serie is not null and Numero_Serie != '' and LTRIM(RTRIM(Numero_Serie)) != '' and Data_prog_Coleta = '{date}'",
            self.connection)
 
        return data
 
    def format_to_backup(self, data):
        column_rename_map = {
            "Numero_Serie": "chassi",
            "Transportadora": "company",
            "Local_Entrega": "local",
        }
 
        data = data[['Local_Entrega', 'Transportadora', 'Numero_Serie']]
 
        renamed_data = data.rename(columns=column_rename_map)
 
        return renamed_data
 
    def get_data_to_update(self):
        date = Dates.days_before(1, Dates.today())
        data = pd.read_sql(
            f"SELECT * FROM {self.config.database_checklist} where VERIFICADO = 1 and StatusTicket is null AND Numero_Serie is not null and Numero_Serie != '' and LTRIM(RTRIM(Numero_Serie)) != '' and Data_prog_Coleta = '{date}'",
            self.connection)
 
        return data
 
    def change_to_verified(self, row):
        query = f"UPDATE {self.config.database_checklist} SET VERIFICADO = 1 WHERE Numero_Serie = '{row['Numero_Serie']}' and Local_Entrega = '{row['Local_Entrega']}'"
        self.cursor.execute(query)
        self.connection.commit()
 
    def get_emails(self, transporter=''):
        data = []
        if transporter:
            transporter = transporter.upper()
            data = pd.read_sql(f"SELECT * FROM {self.config.database_contacts} where TRANSPORTADORA = '{transporter}'",
                               self.connection)
            data = list(data['EMAIL'])
 
        return data
 
    def create_new_column(self):
        cursor = self.connection.cursor()
        query = f"ALTER TABLE {self.config.database_checklist} ADD VERIFICADO BIT DEFAULT 0;"
        cursor.execute(query)
        self.connection.commit()
[12:56] Vitor Herbstrith
class Config():
    def __init__(self):
        self.server = 'FHZNCQSQLVCL2.jdnet.deere.com'
        self.database = 'CQ_SCF_PROJECTS'
        self.username = 'acq6188'
        self.password = 'yy5wrgb4'
        self.database_checklist = "CQ_RCI_SHIPPING"
        self.database_contacts = "CONTATOS_TRANSPORTADORAS"
        self.insert_table_name = "scf_cq_hub.logs_automation_checklist_facil"
        self.backup_table_name = "scf_cq_hub.backup_data_shipping"