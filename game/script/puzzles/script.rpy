# This file contains scripting hooks for puzzles (starting labels, solve labels, fail labels).

# For testing.
label test_puzzles:
    scene layer "screens"
    menu:
        "Room 1 Puzzle 2":
            jump room_1_puzzle_2
        "Room 2 Puzzle 3":
            jump room_2_puzzle_3
        "Room 3 Puzzle 2":
            jump room_3_puzzle_2
        "Room 3 Puzzle 3":
            jump room_3_puzzle_3

label room_1_puzzle_1:
    call init_bomb
    show screen bomb(bomb, False)
    "<TODO: Insert intro script and rules.>"
    call screen bomb(bomb)

label solved_room_1_puzzle_1:
    show screen bomb(bomb, False)
    "You solved room_1_puzzle_1."
    hide screen bomb
    jump test_puzzles

label failed_room_1_puzzle_1:
    show screen bomb(bomb, False)
    "You failed room_1_puzzle_1."
    hide screen bomb
    jump test_puzzles

label room_1_puzzle_2:
    call init_puzzle_board
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

label room_2_puzzle_3:
    call init_cybernetics
    show screen cybernetics(cyb, False)
    "<TODO: Insert intro script and rules.>"
    call screen cybernetics(cyb)

label solved_room_2_puzzle_3:
    show screen cybernetics(cyb, False)
    "You solved room_2_puzzle_3."
    hide screen cybernetics
    jump test_puzzles

label failed_room_2_puzzle_3:
    jump recalibration_game_over
    show screen cybernetics(cyb, False)
    "You failed room_2_puzzle_3."
    hide screen cybernetics
    jump test_puzzles

label room_3_puzzle_2:
    call init_toy_board
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

label room_3_puzzle_3:
    call init_mise_en_place
    show screen mise_en_place(False)
    "<TODO: Insert intro script and rules.>"
    pause 0.0
    $ renpy.retain_after_load()
    call screen mise_en_place

label solved_room_3_puzzle_3:
    show screen mise_en_place(False)
    "You solved room_3_puzzle_2."
    jump test_puzzles

label failed_room_3_puzzle_3:
    show screen mise_en_place(False)
    "You failed room_3_puzzle_3."
    jump test_puzzles
