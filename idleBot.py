from kaggle_environments.envs.halite.helpers import *


def agent(observation, configuration):
    board = Board(observation, configuration)
    current_player = board.current_player

    # Get my player.
    if len(current_player.shipyards) == 0:
        if len(current_player.ships) == 0:
            return current_player.next_actions

        converting_ship = current_player.ships[0]
        converting_ship.next_action = ShipAction.CONVERT

    for shipyard in current_player.shipyards:
        if len(current_player.ships) == 0 and board.current_player.halite >= 500:
            shipyard.next_action = ShipyardAction.SPAWN

    return current_player.next_actions
