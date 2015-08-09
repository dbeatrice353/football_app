from .. import db
import pandas as pd

class DataFetcher():
    def get_positions(self):
        positions = pd.read_sql_query(
            '''SELECT DISTINCT current_position FROM players;
            ''', db.engine
            )
        return positions

    def get_profile(self, player):
        profile = pd.read_sql_query(
            '''SELECT week_number, stat_type, stat_value from player_stats
            WHERE player_name = '%s';
            ''' % player,
            db.engine
            )
        return profile

    def get_players(self, position):
        players = pd.read_sql_query(
            '''SELECT DISTINCT name_ FROM players
            WHERE position = '%s'
            ''' %position, db.engine
            )
        return players
