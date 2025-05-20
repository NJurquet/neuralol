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
        # NewFeature.OBJECTIVES_CONTROL,
        # NewFeature.TOWER_CONTROL,
        NewFeature.GOLD_PER_MIN,
        NewFeature.LEVEL_PER_MIN,
        # NewFeature.TEAM_KILLS_PER_MIN,
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


def role_train_val_test_split(df: pd.DataFrame, role: str, val_size: float = 0.15, test_size: float = 0.1, show: bool = True) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Split the dataframe into training, validation and test datasets for a provided role.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to split.
    role : str
        The role to split by.
    val_size : float, optional
        The proportion of the dataset to include in the validation split (default is 0.15).
    test_size : float, optional
        The proportion of the dataset to include in the test split (default is 0.1).

    Returns
    -------
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
        The training dataset & target, validation dataset & target, and test dataset & target that have the role specified.
    """
    if role not in Role.LIST:
        raise ValueError(
            f"Invalid role: '{role}'. Use `Role` constant class.\nValid roles are: {Role.LIST}.")

    # Filter the dataframe by role
    df_role = df[df[StatsCols.ROLE] == role]

    X = df_role
    y = df_role[StatsCols.WIN]

    # Split the dataframe into train+val and test sets
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42)

    # Calculate the validation size relative to the train+val set
    relative_val_size = val_size / (1 - test_size)

    # Further split the train+val set into train and validation sets
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=relative_val_size, random_state=42)

    if show:
        from IPython.display import display
        # Calculate total dataset size
        total_size = X.shape[0]
        # Create a dataframe to display the split information
        split_info = pd.DataFrame({
            'Split': ['Training set', 'Validation set', 'Test set', 'Total'],
            'Samples': [X_train.shape[0], X_val.shape[0], X_test.shape[0], total_size],
            'Proportion (%)': [
                X_train.shape[0]/total_size * 100,
                X_val.shape[0]/total_size * 100,
                X_test.shape[0]/total_size * 100,
                100.0
            ]
        })
        # Format the percentage columns
        split_info['Proportion (%)'] = split_info['Proportion (%)'].round(2)
        display(split_info)

    return X_train, X_val, X_test, y_train, y_val, y_test
