import pandas as pd
import sqlalchemy


url = sqlalchemy.engine.url.URL('mysql', username='root', password='mypw', host='localhost', port=3306, database='fantasy', query=None)

engine = sqlalchemy.create_engine(url)

players = pd.DataFrame.from_csv('Players.txt', sep = '\t')

players.to_sql('players', engine, 'mysql', if_exists = 'append')
