import pandas as pd

#PLAYER TABLE FUNCTIONS
def height_to_inches(height):
    '''Converts height to inches'''
    #Strange encoding causes 6'4" to appear ' 6\x924\x94\xa0\xa0'
    try:
        temp = height.strip()
    except AttributeError:
        return height
    try:
        inches = float(temp[0])*12 + float(temp[2])
    except IndexError:
        return height
    return inches

def get_draft_year(draft):
    '''Returns year player was drafted'''
    if draft == '\\N': #if draft info is blank
        return draft
    draft = draft.strip()
    return draft[:draft.find(' ')]

def get_draft_round(draft):
    '''Returns the round that the player was picked in the draft.'''
    if draft == '\\N':
        return draft
    draft = draft.strip()
    return draft[draft.find('Round')+6:draft.find('(')-1]

def get_draft_pick(draft):
    '''Returns the players pick number during his round in the draft.'''
    if draft == '\\N':
        return draft
    draft = draft.strip()
    return draft[draft.find('(') + 1: draft.find(')')]

#GAME_STATS TABLE FUNCTIONS
def get_home(opponent):
    '''Returns True if it was a home game'''
    if 'at' in opponent:
        return False
    return True

def clean_opponent(opponent):
    '''Removes "at " from opponent column, which tells whether it was home or away game'''
    return opponent.replace('at ','')

def get_win(result):
    '''Returns true if game was a win'''
    if 'W' in result:
        return True
    return False

def get_points(result):
    '''Returns points scored by player's team.'''
    return result[result.find(' ') + 1: result.find('-')]

def get_opponent_points(result):
    '''Returns points scored by opposing team.'''
    return result[result.find('-') + 1 :]

def get_game_id


if __name__ == '__main__':
    #READ AND PREP DATA
    players = pd.read_csv('players.dat', sep = '\t', encoding = 'latin')
    players['Draft_Year'] = players['DRAFT'].apply(get_draft_year)
    players['Draft_Round'] = players['DRAFT'].apply(get_draft_round)
    players['Draft_Pick'] = players['DRAFT'].apply(get_draft_pick)

    game_stats = pd.read_csv('game_stats.dat', sep = '\t')
    game_stats['Home_Game'] = game_stats['OPPONENT'].apply(get_home)
    game_stats['OPPONENT'] = game_stats['OPPONENT'].apply(clean_opponent)
    game_stats['Win'] = game_stats['RESULT'].apply(get_win)
    game_stats['Points'] = game_stats['RESULT'].apply(get_points)
    game_stats['Opponent_Points'] = game_stats['RESULT'].apply(get_opponent_points)

    season_stats = pd.read_csv('season_stats.dat', sep = '\t', encoding = 'ISO-8859-1')

    #WRITE DATA
    players.to_csv('../prepped/players.dat', sep = '\t')
    game_stats.to_csv('..prepped/game_stats.dat', sep = '\t')
    season_stats.to_csv('..prepped/season_stats.dat', sep = '\t')
