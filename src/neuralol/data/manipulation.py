import pandas as pd
from sklearn.model_selection import train_test_split

from neuralol.constants import StatsCols, NewFeature, Role


def get_model_players_game_features(role: str | None = None) -> list[str]:
    """
    Get the list of players game stats features used for the model. If a role is provided, only the features for that role are returned.

    Parameters
    ----------
    role : str | None, optional
        The role of the player. If None, all features are returned.
        - `Role.TOP`
        - `Role.JUNGLE`
        - `Role.MID`
        - `Role.BOT`
        - `Role.SUPPORT`

    Returns
    -------
    list[str]
        The list of players game stats features used for the model.
    """
    if role is not None and role not in Role.__dict__.values():
        raise ValueError(
            f"Invalid role: '{role}'. Use `Role` constant class.\nValid roles are: {Role.TOP}, {Role.JUNGLE}, {Role.MID}, {Role.BOT}, {Role.SUPPORT}.")

    features = [
        NewFeature.KLA,
        NewFeature.OBJECTIVES_CONTROL,
        NewFeature.TOWER_CONTROL,
        NewFeature.GOLD_PER_MIN,
        NewFeature.LEVEL_PER_MIN,
        NewFeature.TEAM_KILLS_PER_MIN,
        StatsCols.LARGEST_KILLING_SPREE,
        StatsCols.LARGEST_MULTI_KILL,
    ]

    # Add damage and CS features only for non-support roles
    if role != Role.SUPPORT:
        features.extend([
            NewFeature.CS_PER_MIN,
            NewFeature.TOTAL_DAMAGE_PER_MIN,
            NewFeature.DAMAGE_TO_CHAMPIONS_PER_MIN,
            NewFeature.DAMAGE_TAKEN_PER_MIN,
        ])

    return features


def role_test_split(df: pd.DataFrame, role: str, test_size: float = 0.2) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Split the dataframe into training+validation dataset and test dataset for a provided role.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to split.
    role : str
        The role to split by.
    test_size : float, optional
        The proportion of the dataset to include in the test split (default is 0.2).

    Returns
    -------
    tuple[pd.DataFrame]
        The training+validation dataset & target and the test dataset & target that have the role specified.
    """
    if role not in Role.LIST:
        raise ValueError(
            f"Invalid role: '{role}'. Use `Role` constant class.\nValid roles are: {Role.LIST}.")

    # Filter the dataframe by role
    df_role = df[df[StatsCols.ROLE] == role]

    X = df_role[get_model_players_game_features(role)]
    y = df_role[StatsCols.WIN]

    # Split the dataframe into train and test sets
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42)

    return X_train_val, X_test, y_train_val, y_test
