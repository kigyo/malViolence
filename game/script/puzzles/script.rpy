# This file contains scripting hooks for puzzles (starting labels, solve labels, fail labels).

# For testing.
label test_puzzles:
    scene layer "screens"
    menu:
        "Room 1 Puzzle 2":
            jump room_1_puzzle_2
        "Room 3 Puzzle 2":
            jump room_3_puzzle_2

label room_1_puzzle_2:
    $ pb = PuzzleBoard(width=6, height=6, move_cap=20)
    $ adt = 0.5
    show screen puzzle_playspace(pb, False)
    "<TODO: Insert intro script and rules.>"
    call screen puzzle_playspace(pb)

label solved_room_1_puzzle_2:
    show screen puzzle_playspace(pb, False)
    "You solved room_1_puzzle_2."
    hide screen puzzle_playspace
    jump test_puzzles

label failed_room_1_puzzle_2:
    show screen puzzle_playspace(pb, False)
    "You failed room_1_puzzle_2."
    hide screen puzzle_playspace
    jump test_puzzles

label room_3_puzzle_2:
    $ tb = ToyBoard(width=5, height=5)
    $ adt = persistent.toy_reticle_timeout
    show screen toy_playspace(tb, False)
    "<TODO: Insert intro script and rules.>"
    call screen toy_playspace(tb)

label solved_room_3_puzzle_2:
    show screen toy_playspace(tb, False)
    "You solved room_3_puzzle_2."
    hide screen toy_playspace
    jump test_puzzles

label failed_room_3_puzzle_2:
    show screen toy_playspace(tb, False)
    "You failed room_3_puzzle_2."
    hide screen toy_playspace
    jump test_puzzles
