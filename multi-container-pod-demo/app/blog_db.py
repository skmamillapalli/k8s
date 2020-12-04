# DB Interaction practise scripts, Cartesian product and joins

import sqlite3
import traceback
import pymysql

class SqlDB:
    def __init__(self):
        # Create a new db if one doesnt exists
        self.conn=pymysql.connect(host='192.168.64.4',user='root', password='password', charset='utf8mb4',port=31238)
        # Get cursor object
        self.cursor = self.conn.cursor()

    def add_state_table(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS StateData(Sno INTEGER PRIMARY KEY \
                            AUTOINCREMENT, Name TEXT, Count TEXT)")
            self.cursor.executemany("INSERT INTO StateData(Name, Count) VALUES(?, ?)", covid_cases_per_state)
            self.conn.commit()
        except Exception as e:
            print(str(e))
            traceback.print_exc()

    def describe_table(self, table_name):
        try:
            state_list = self.cursor.execute(f"SELECT * FROM {table_name}").fetchall()
            for state in state_list:
                print(state)
        except Exception as e:
            print(str(e))
            traceback.print_exc()
    
    def remove_table(self, table_name):
        try:
            self.cursor.execute(f"DROP Table {table_name}")
        except Exception as e:
            print(str(e))
            traceback.print_exc()
    
    def add_region_table(self):
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS RegionMapping(Sno INTEGER PRIMARY KEY \
                            AUTOINCREMENT, Region TEXT, State TEXT)")
            self.cursor.executemany("INSERT INTO RegionMapping(State, Region) VALUES(?, ?)", region_state_mapping)
            self.conn.commit()
        except Exception as e:
            print(str(e))
            traceback.print_exc()

    def describe_cases_per_region(self):
        try:
            # Cartestian porduct
            data_per_region=self.cursor.execute("SELECT Region, SUM(Count) \
                                 FROM StateData, RegionMapping WHERE \
                                 StateData.Name=RegionMapping.State \
                                 GROUP BY Region")
            # Join
            data_per_region=self.cursor.execute("SELECT Region, SUM(Count) \
                                 FROM StateData JOIN RegionMapping ON StateData.Name=RegionMapping.State \
                                 GROUP BY Region")
            for row in data_per_region:
                print(row)
        except Exception as e:
            print(str(e))
            traceback.print_exc()

db=SqlDB()
db.remove_table('StateData')
db.remove_table('RegionMapping')
db.add_state_table()
db.add_region_table()
db.describe_table('StateData')
db.describe_table('RegionMapping')
db.describe_cases_per_region()
