from config import db_string
import sqlalchemy as sql
from sqlalchemy import Table, MetaData, Column, Integer, String, Date, Float

#CREATE ENGINE AND METADATA OBJECTS
engine = sql.create_engine(db_string)
metadata = MetaData()

#DEFINE TABLES
monitors = Table('monitors', metadata,
                 Column('monitor', String(100), primary_key = True),
                 Column('type_', String(100))
                     )

tags = Table('tags', metadata,
             Column('monitor', String(100), primary_key = True),
             Column('tag', String(100), primary_key = True),
             )

monitor_data = Table('monitor_data', metadata,
                     Column('monitor', String(100), primary_key = True),
                     Column('date_', Date(), primary_key = True),
                     Column('data_type', String(100), primary_key = True),
                     Column('data_value', Float)
                     )

users = Table('users', metadata,
              Column('username', String(30), primary_key =True),
              Column('first_name', String(30)),
              Column('last_name', String(30)),
              Column('email', String(50)),
              Column('password_', String(80)))


#DROP TABLE IF EXISTS, THEN CREATE TABLE
tables = [monitors, tags, monitor_data]
for table in tables:
    print(table.name)
    table.drop(engine, checkfirst = True)
    table.create(engine, checkfirst = True)
