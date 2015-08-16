from .. import db
import pandas as pd

class DataFetcher():
    def get_positions(self):
        positions = pd.read_sql_query(
            '''SELECT DISTINCT current_position FROM players;
            ''', db.engine
            )
        return positions

    def get_profile(self, player_id = 1):
        profile = pd.read_sql_query(
            '''SELECT season, stat_type, value from season_stats
            WHERE player_id = '%s';
            ''' % player_id,
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

    def get_average(self):
        average = pd.read_sql_query(
        '''SELECT stat_type, AVG(value) FROM season_stats
        LEFT JOIN players USING (player_id)
        WHERE season = '2014'
        AND current_position = 'WR'
        GROUP BY stat_type;
        ''', db.engine
        )
        return average
