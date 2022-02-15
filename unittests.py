from MainGameFile import (
    GameState,
)


def test_generateNewWord():
    try:
        game = GameState()
        game.generateNewWord()
    except NameError:
        assert False, "generateNewWord not defined"

    game = GameState()
    testword = game.generateNewWord()
    for i in range(10000):
        assert len(testword) < 40


def test_scoreReset():
    try:
        game = GameState()
        game.scoreReset()
    except NameError:
        assert False, "scoreReset not defined"

    game = GameState()
    game.scoreReset()
    assert game.score == 0
    assert not game.congratsplayedbefore
