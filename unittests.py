from MainGameFile import (
    GameState,
)


game = GameState()


def test_generateNewWord():
    try:
        game.generateNewWord()
    except NameError:
        assert False, "generateNewWord not defined"

    testword = game.generateNewWord()
    assert len(testword) < 39
    assert len(testword) > 3


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
