
default difficulty_level = 2

define single_difficulty_puzzles = ["tutorial", "room1_meta", "room2_meta", "room3_meta"]

define old_puzzle_difficulty_mapper = {
    "room1_1": 3,
    "room1_2": 3,
    "room1_3": 3,
    "room2_1": 1,
    "room2_2": 3,
    "room2_3": 3,
    "room3_1": 3,
    "room3_2": 2,
    "room3_3": 2,
}

default difficulties_cleared = {
    "room1_1": None,
    "room1_2": None,
    "room1_3": None,
    "room2_1": None,
    "room2_2": None,
    "room2_3": None,
    "room3_1": None,
    "room3_2": None,
    "room3_3": None,
}

default bomb_level = 3
default hacking_level = 3
default decanting_level = 3
default evidence_level = 1
default panopticon_level = 3
default cybernetics_level = 3
default quilt_level = 3
default toy_level = 2
default cooking_level = 2

init python:
    def difficulty_change_reset():
        #room 1
        init_bomb_function(None)
        #room 2
        cybernetics_reset()
        #room 3
        #toy_board_reset(None)
        init_mise_en_place()
        renpy.retain_after_load()
        renpy.restart_interaction()
        #possibly necessary for speck's puzzles, for some reason they just won't update on their own:
        #renpy.reload_script()

    def solved_puzzles_convert():
        if isinstance(persistent.solved_puzzles, list):
            temp_dict = {1:[], 2:[], 3:[], "tutorial":False, "room1_meta":False, "room2_meta":False, "room3_meta":False}

            for k in old_puzzle_difficulty_mapper:
                if k in persistent.solved_puzzles:
                    temp_dict[old_puzzle_difficulty_mapper[k]].append(k)

            for k in single_difficulty_puzzles:
                if k in persistent.solved_puzzles:
                    temp_dict[k] = True

            persistent.solved_puzzles = temp_dict

        if float(_version) < 1.2:
            #fix set difficulties of active puzzles
            store.bomb_level = old_puzzle_difficulty_mapper["room1_1"]
            store.hacking_level = old_puzzle_difficulty_mapper["room1_2"]
            store.decanting_level = old_puzzle_difficulty_mapper["room1_3"]
            store.evidence_level = old_puzzle_difficulty_mapper["room2_1"]
            store.panopticon_level = old_puzzle_difficulty_mapper["room2_2"]
            store.cybernetics_level = old_puzzle_difficulty_mapper["room2_3"]
            store.quilt_level = old_puzzle_difficulty_mapper["room3_1"]
            store.toy_level = old_puzzle_difficulty_mapper["room3_2"]
            store.cooking_level = old_puzzle_difficulty_mapper["room3_3"]

            init_bomb_function(None)
            puzzle_board_reset(None)
            panopticon_init(True)
            cybernetics_reset(None)
            toy_board_reset(None)
            reset_cutting_board()

            renpy.scene("puzzles")

        store._version = config.version

    config.after_load_callbacks.append(solved_puzzles_convert)

    def clear_puzzle(name):
        if name in single_difficulty_puzzles and not persistent.solved_puzzles[name]:
            persistent.solved_puzzles[name] = True

        else:
            if name not in persistent.solved_puzzles[difficulty_level]:
                persistent.solved_puzzles[difficulty_level].append(name)

            store.difficulties_cleared[name] = difficulty_level

    def lowest_cleared_difficulty():
        lowest = 3
        for k,v in difficulties_cleared:
            if v == None:
                lowest = 0
                break
            elif v < lowest:
                lowest = v
        return lowest

    #some drag puzzles reset their positions after load
    def reset_puzzles_after_load():
        #room1
        init_bomb_function(None)

        #room2
        # cybernetics_reset()
        word_init()

        #room3
        scrapbook_init()
        # toy_board_reset(None)
        init_mise_en_place()
        pass

    config.after_load_callbacks.append(reset_puzzles_after_load)

default persistent.solved_puzzles = {1:[], 2:[], 3:[], "tutorial":False, "room1_meta":False, "room2_meta":False, "room3_meta":False}
