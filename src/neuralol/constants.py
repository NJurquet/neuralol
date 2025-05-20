class Role:
    """
    Class holding player roles.
    """
    TOP = 'Top'
    JUNGLE = 'Jungle'
    MID = 'Mid'
    BOT = 'Bot'
    SUPPORT = 'Support'
    LIST = [TOP, JUNGLE, MID, BOT, SUPPORT]


class StatsCols:
    """
    Class holding players game stats column names.
    """
    GAME_ID = 'game_id'
    PLAYER_ID = 'player_id'
    PLAYER_NAME = 'player_name'
    TEAM_ID = 'team_id'
    TEAM_NAME = 'team_name'
    TEAM_ACRONYM = 'team_acronym'
    ROLE = 'role'
    WIN = 'win'
    GAME_LENGTH = 'game_length'
    CHAMPION_NAME = 'champion_name'
    TEAM_KILLS = 'team_kills'
    TOWER_KILLS = 'tower_kills'
    INHIBITOR_KILLS = 'inhibitor_kills'
    DRAGON_KILLS = 'dragon_kills'
    HERALD_KILLS = 'herald_kills'
    BARON_KILLS = 'baron_kills'
    PLAYER_KILLS = 'player_kills'
    PLAYER_DEATHS = 'player_deaths'
    PLAYER_ASSISTS = 'player_assists'
    TOTAL_MINIONS_KILLED = 'total_minions_killed'
    GOLD_EARNED = 'gold_earned'
    LEVEL = 'level'
    TOTAL_DAMAGE_DEALT = 'total_damage_dealt'
    TOTAL_DAMAGE_DEALT_TO_CHAMPIONS = 'total_damage_dealt_to_champions'
    TOTAL_DAMAGE_TAKEN = 'total_damage_taken'
    WARDS_PLACED = 'wards_placed'
    LARGEST_KILLING_SPREE = 'largest_killing_spree'
    LARGEST_MULTI_KILL = 'largest_multi_kill'


class NewFeature:
    """
    Class holding new feature names.
    """
    KLA = 'KLA'
    CS_PER_MIN = 'cs_per_min'
    TEAM_KILLS_PER_MIN = 'team_kills_per_min'
    OBJECTIVES_CONTROL = 'objectives_control'
    TOWER_CONTROL = 'tower_control'
    GOLD_PER_MIN = 'gold_per_min'
    LEVEL_PER_MIN = 'level_per_min'
    TOTAL_DAMAGE_PER_MIN = 'total_damage_per_min'
    DAMAGE_TO_CHAMPIONS_PER_MIN = 'damage_to_champions_per_min'
    DAMAGE_TAKEN_PER_MIN = 'damage_taken_per_min'


class Models:
    """
    Class holding model names.
    """
    RANDOM_FOREST = 'RandomForest'
    XGBOOST = 'XGBoost'
    DNN = 'DNN'
    LIST = [RANDOM_FOREST, XGBOOST, DNN]
