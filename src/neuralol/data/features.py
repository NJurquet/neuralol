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
