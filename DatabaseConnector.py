import psycopg2


class DatabaseConnector:
    def __init__(self, host, database, user, password, port='5432'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        return psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password,
                                port=self.port)
