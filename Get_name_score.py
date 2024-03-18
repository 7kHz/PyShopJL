from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()


# pprint(game_stamps)


def get_score(game_stamps: list, offset: int):
    if isinstance(offset, int):
        if offset < 0:
            return 'The offset is a positive number, try again'
        for game_stamp in game_stamps:
            if game_stamp["offset"] == offset:
                return game_stamp["score"]["home"], game_stamp["score"]["away"]
        return f'Score is not available for offset: {offset}'
    return 'The offset is a number, try again'


with open('game_stamps', 'w') as file:
    for stamp in game_stamps:
        file.write(str(stamp) + '\n')

print(get_score(game_stamps, 54555))
print(get_score(game_stamps, 32000))
