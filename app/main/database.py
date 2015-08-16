from .. import db
import pandas as pd
from sqlalchemy import text

class DataFetcher():
    def get_positions(self):
        q = text(
            '''SELECT DISTINCT current_position FROM players;
            '''
            )
        positions = pd.read_sql_query(q, db.engine)
        return positions

    def get_profile(self, player_id = 1):
        q = text(
            '''SELECT season, stat_type, value from season_stats
            WHERE player_id =':id_';
            ''').bindparams(id_=player_id)
        profile = pd.read_sql_query(q, db.engine)
        return profile

    def get_players(self, position = 'WR', team = None):
        q = text(
            '''SELECT first_name || ' ' || last_name as name, player_id FROM players
            WHERE current_position=:position
            ORDER BY last_name;
            '''
            ).bindparams(position=position)
        players = pd.read_sql_query(q, db.engine)
        return players

    def get_average(self):
        q = text(
            '''SELECT stat_type, AVG(value) FROM season_stats
            LEFT JOIN players USING (player_id)
            WHERE season = '2014'
            AND current_position = 'WR'
            GROUP BY stat_type;
            ''')
        average = pd.read_sql_query(q, db.engine)
        return average
