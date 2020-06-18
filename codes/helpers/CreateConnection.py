import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
import pandas as pd


class CreateConnection:
    def __init__(self, dialect, username, password, host_name, port, database):
        self.dialect = dialect
        self.username = username
        self.password = password
        self.host_name = host_name
        self.port = port
        self.database = database
        self.engine_url = self.dialect + '://' + self.username + ':' + self.password + '@' + self.host_name + ':' + self.port + '/' + self.database
        
    def create_engine(self):
        self.engine = create_engine(self.engine_url)
        return self.engine
        
    def create_schema(self, schema_name):
        self.schema_name = schema_name
        if not self.engine.dialect.has_schema(self.engine, self.schema_name):
            self.engine.execute(sqlalchemy.schema.CreateSchema(self.schema_name))

    def create_table(self, data, table_name):
        self.table_name = table_name
        data_df = data.head(0)
        data_df.to_sql(
            self.table_name,
            self.engine,
            self.schema_name,
            if_exists = "append",
            index=False,
        )
