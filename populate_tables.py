import pandas as pd
from config import db_string
import sqlalchemy as sql

engine = sqlalchemy.create_engine(db_string)

players = pd.read_csv('prepped/players.dat', sep = '\t', index_col = 0)
game_stats = pd.read_csv('prepped/game_stats.dat', sep = '\t', index_col = 0)
season_stats = pd.read_csv('prepped/season_stats.dat', sep = '\t', encoding = 'ISO-8859-1', index_col = 0)

print('Inserting players...')
players.to_sql('players', engine, if_exists = 'replace')
print('Inserting game_stats...')
game_stats.to_sql('game_stats', engine, if_exists = 'replace', chunksize = 1000)
print('Inserting season_stats...')
season_stats.to_sql('season_stats', engine, if_exists = 'replace', chunksize = 1000)


