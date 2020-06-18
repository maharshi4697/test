from sys import exit
import sys
import configparser

class ConfigurationValidation():
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = configparser.ConfigParser()
        if(not self.config.read(self.config_file_path)):
            print("Configuration Path not correct")
            exit()

    def input_csv_check(self):
        if(self.config.get('CSVtoDB Config','input_csv')):
            return self.config.get('CSVtoDB Config','input_csv')
        else:
            print("Input CSV is blank")
            exit()

    def dialect_check(self):
        if(self.config.get('CSVtoDB Config','dialect')):
            return self.config.get('CSVtoDB Config','dialect')
        else:
            print("Dialect not set")
            exit()

    def username_check(self):
        if(self.config.get('CSVtoDB Config','username')):
            return self.config.get('CSVtoDB Config','username')
        else:
            print("Username not set")
            exit()

    def password_check(self):
        if(self.config.get('CSVtoDB Config','password')):
            return self.config.get('CSVtoDB Config','password')
        else:
            print("Password not set")
            exit()

    def host_name_check(self):
        if(self.config.get('CSVtoDB Config','host_name')):
            return self.config.get('CSVtoDB Config','host_name')
        else:
            print("Hostname not set")
            exit()

    def port_check(self):
        if(self.config.get('CSVtoDB Config','port')):
            return self.config.get('CSVtoDB Config','port')
        else:
            print("Port not set")
            exit()

    def database_check(self):
        if(self.config.get('CSVtoDB Config','database')):
            return self.config.get('CSVtoDB Config','database')
        else:
            print("Database not set")
            exit()

    def schema_name_check(self):
        if(self.config.get('CSVtoDB Config','schema_name')):
            return self.config.get('CSVtoDB Config','schema_name')
        else:
            print("Schema not set")
            exit()

    def staging_table_name_check(self):
        if(self.config.get('CSVtoDB Config','staging_table_name')):
            return self.config.get('CSVtoDB Config','staging_table_name')
        else:
            print("Staging table name not set")
            exit()

    def final_table_name_check(self):
        if(self.config.get('CSVtoDB Config','final_table_name')):
            return self.config.get('CSVtoDB Config','final_table_name')
        else:
            print("Final table name not set")
            exit()

    def primary_key_check(self):
        if(self.config.get('CSVtoDB Config','primary_key')):
            return self.config.get('CSVtoDB Config','primary_key')
        else:
            print("Primary Key not set")
            exit()
