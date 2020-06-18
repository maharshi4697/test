import pandas
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
from psycopg2 import extensions,connect
import csv
from io import StringIO

class PopulateTables:
    def __init__(self, schema_name, engine):
        self.schema_name = schema_name
        read_committed = extensions.ISOLATION_LEVEL_READ_COMMITTED  #Set Isolation Level
        self.conn = engine.raw_connection()
        self.conn.set_isolation_level(read_committed)
        self.cur = self.conn.cursor()

    def populate_staging(self, data, staging_table_name):
        self.staging_table_name = staging_table_name
        self.cur.execute(" TRUNCATE TABLE "+ self.schema_name + "." + self.staging_table_name + ";")
        output = StringIO()
        writer = csv.writer(output, delimiter='\t')
        lis=data.values.tolist()
        writer.writerows(lis)
        output.seek(0)
        self.cur.copy_from(output, self.schema_name+"." + self.staging_table_name, null="")
        return str(self.cur.rowcount)

    def check_primary_key(self, primary_key, final_table_name):
        self.final_table_name = final_table_name
        self.primary_key = primary_key
        self.cur.execute(""" SELECT  column_name
                        FROM    information_schema.key_column_usage
                        WHERE   table_name = '""" + self.final_table_name + """'
                        AND     constraint_schema = '""" + self.schema_name + """'
                        AND     constraint_name = '""" + self.final_table_name + """_pkey';
                    """)
        pk=self.cur.fetchone()
        if(not pk):
           self.cur.execute(""" ALTER TABLE """ + self.schema_name + "." + self.final_table_name +
                       """ ADD PRIMARY KEY (""" + self.primary_key + """);""")
        if(pk and self.primary_key!=pk[0]):
           self.cur.execute(""" ALTER TABLE """ + self.schema_name + "." + self.final_table_name +
                       """ DROP CONSTRAINT """ + (self.final_table_name+'_pkey') + """;""")
           self.cur.execute(""" ALTER TABLE """ + self.schema_name + "." + self.final_table_name +
                       """ ADD PRIMARY KEY (""" + self.primary_key + """);""")
        self.cur.execute(""" CREATE INDEX idx ON """ + self.schema_name + "." + self.final_table_name +
                    """(""" + self.primary_key + """);""")      # Create Index

    def populate_final_table(self, columns):
        self.columns = columns
        self.cur.execute("""SELECT * FROM """ + self.schema_name + "." + self.final_table_name)
        initial_rows=self.cur.rowcount
        self.cur.execute("""
            WITH temp1 AS
            (
                SELECT     *
                        ,ROW_NUMBER () OVER( PARTITION BY """ + self.primary_key + """ ) AS rank
                FROM     """ + self.schema_name + "." + self.staging_table_name +
        """ ), temp2 as
            (
                SELECT      DISTINCT ON (""" + self.primary_key + """)
                         *
                FROM      temp1
                ORDER BY """ + self.primary_key +
                         """,rank desc
            )
            INSERT INTO """ + self.schema_name + "." + self.final_table_name +
        """(""" + self.primary_key + ',' + ','.join([i for i in self.columns]) + """)"""
        """ SELECT """ + self.primary_key + ',' + ','.join([i for i in self.columns]) +
        """ FROM   temp2
            ON     CONFLICT (""" + self.primary_key + """)
            DO
                UPDATE
                SET    (""" + (','.join([i for i in self.columns])) + """) =
                       (""" + (','.join([('excluded.'+i) for i in self.columns])) + """);
        """)
        final_rows=self.cur.rowcount
        return str(final_rows - initial_rows)

    def commit_and_close_connection(self):
        self.conn.commit()
        self.conn.close()
        self.cur.close()
