import pandas as pd
import argparse
from helpers.ConfigurationValidator import ConfigurationValidation
from helpers.CreateConnection import CreateConnection
from helpers.PopulateTables import PopulateTables

class ImportCSVtoDB():
    def configuration(self, file):
        valid = ConfigurationValidation(config_file_path = file)
        self.input_csv = valid.input_csv_check()
        self.dialect = valid.dialect_check()
        self.username = valid.username_check()
        self.password = valid.password_check()
        self.host_name = valid.host_name_check()
        self.port = valid.port_check()
        self.database = valid.database_check()
        self.schema_name = valid.schema_name_check()
        self.staging_table_name = valid.staging_table_name_check()
        self.final_table_name = valid.final_table_name_check()
        self.primary_key = valid.primary_key_check()

    def input_and_modify(self):
        self.df=pd.read_csv(self.input_csv)
        self.df=self.df.replace(r'\n',  ' ', regex=True)
        self.columns=[]
        for i in self.df.columns:
            if i!=self.primary_key:
                self.columns.append(i)

    def create(self):
        table_creator = CreateConnection(
                            dialect = self.dialect,
                            username = self.username,
                            password = self.password,
                            host_name = self.host_name,
                            port = self.port,
                            database = self.database,
                        )
        self.engine = table_creator.create_engine()
        table_creator.create_schema(self.schema_name)
        table_creator.create_table(self.df, self.staging_table_name)
        table_creator.create_table(self.df, self.final_table_name)

    def populate(self):
        tables_data = PopulateTables(self.schema_name, self.engine)
        self.staging_inserts = tables_data.populate_staging(self.df, self.staging_table_name)
        tables_data.check_primary_key(self.primary_key, self.final_table_name)
        self.final_inserts = tables_data.populate_final_table(self.columns)
        tables_data.commit_and_close_connection()

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-c",
            "--configuration",
            dest="config",
            type=str,
            metavar="<str>",
            required=True,
            help="Configuration Path for Script",
        )
        args = parser.parse_args()
        ImportCSVtoDB.configuration(self, args.config)
        ImportCSVtoDB.input_and_modify(self)
        ImportCSVtoDB.create(self)
        ImportCSVtoDB.populate(self)
        print("Data Copied to " + self.final_table_name + " Successfully.")
        print(self.staging_inserts + " rows inserted in staging table.")
        print(self.final_inserts + " rows inserted in final table.")
        exit()

if __name__ == '__main__':
    ImportCSVtoDB().main()
