class DatabaseDatabricks():
    def __init__(self):
        print('Loading Database from Databricks...')
        self.connection = self.token
        self.config = Config()

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, tk):
        # try:
        connection = sql.connect(server_hostname="deere-edl.cloud.databricks.com",
                                 http_path="sql/protocolv1/o/701067943002101/0930-153945-czl7xymb",
                                 access_token=tk)
        self._connection = connection
        # except Exception as e:
        #    self._error = f"Não foi possivel connectar ao databricks, {e}"

    @property
    def error(self):
        try:
            return self._error
        except Exception:
            return None

    @error.setter
    def error(self, value):
        self._error = value

    def query(self, operation, to_dict=True, counter=0):
        try:
            result = pd.read_sql(operation, self.connection)
            if to_dict:
                result = result.to_dict('records')
            return result
        except DatabaseError:
            if counter >= 10:
                raise ConnectionAbortedError(
                    "O Servidor tentou realizar muitas conexões sem exito com o databricks")
            self.connection = self.token
            counter += 1
            return self.query(operation, to_dict, counter)
        # except Exception as e:
        #    return {"Error": e}

    def insert_logs(self, data):
        error = ""
        for _ in range(10):
            try:
                cursor = self.connection.cursor()
                cursor.execute(
                    f"INSERT INTO {
                        self.config.insert_table_name} (concatenation, chassi, log, date) VALUES (%s, %s, %s, %s)",
                    (data['concatenation'], data['chassi'], data['log'], data['date']))

                break
            except Exception as e:
                error = e
                time.sleep(10)
        else:
            raise ConnectionAbortedError(
                f'Não está sendo possivel adicionar dados de logs à tabela {error}')

    def update_old_data(self, new_data):
        # Alterar para ser mais eficiente
        cursor = self.connection.cursor()

        delete_query = f"DELETE FROM {self.config.backup_table_name}"
        cursor.execute(delete_query)

        insert_query = f"INSERT INTO {
            self.config.backup_table_name} (chassi, company, local) VALUES (%s, %s, %s)"

        for index, row in new_data.iterrows():
            cursor.execute(
                insert_query, (row['chassi'], row['company'], row['local']))

        self.connection.commit()
        cursor.close()

    def get_old_data(self):
        data = self.query(
            f'''select * from {self.config.backup_table_name}''', False)

        return data

    def get_emails(self, cliente, local):
        data = self.query(f'''SELECT acct_nm, acct_lgl_nm, f_city, customer_to_acct_email FROM edl_current.core_channel_master_acctdetail where mru = '2000' and acct_category = 61
    and customer_to_acct_email is NOT NULL
    and (acct_nm = "{cliente}" or acct_lgl_nm = "{cliente}")
    and f_city = "{local}"''')

        return data
