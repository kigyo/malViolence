default skip_used = False
default difficulty_level = 2

default persistent.difficulty = 2

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
    persistent.unknown_achievements = persistent.unknown_achievements or []

    if persistent.dead_ends:
        new_deadends = []
        for d in persistent.dead_ends:
            if isinstance(d, str):
                # It's a string not an Achievement, we need to convert it.
                if not d.startswith("achievement_"):
                    d = "achievement_%s" % d
                d = getattr(renpy.store, d, None)
                if not d:
                    # We don't know what this achievemnt is.
                    persistent.unknown_achievements.insert(0, d)
                    continue
            new_deadends.append(a)

        persistent.dead_ends = new_deadends

    if persistent.my_achievements:
        new_achievements = []
        for a in persistent.my_achievements:
            if isinstance(a, str):
                # It's a string not an Achievement, we need to convert it.
                if not a.startswith("achievement_"):
                    a = "achievement_%s" % a
                a = getattr(renpy.store, a, None)
                if not a:
                     # We don't know what this achievement is.
                    persistent.unknown_achievements.insert(0, a)
                    continue
            new_achievements.append(a)

        persistent.my_achievements = new_achievements

    if isinstance(persistent.solved_puzzles, list):
        temp_dict = {1:[], 2:[], 3:[], "tutorial":False, "room1_meta":False, "room2_meta":False, "room3_meta":False}

        for k in old_puzzle_difficulty_mapper:
            if k in persistent.solved_puzzles:
                temp_dict[old_puzzle_difficulty_mapper[k]].append(k)

        for k in single_difficulty_puzzles:
            if k in persistent.solved_puzzles:
                temp_dict[k] = True

        persistent.solved_puzzles = temp_dict

    def difficulty_change():
        # set variables
        persistent.difficulty = difficulty_level

        #room 1
        init_bomb_function(None)
        #room 2
        cybernetics_reset(None)
        #room 3
        toy_board_reset(None)
        init_mise_en_place()
        evidence_init(True)

        renpy.retain_after_load()
        renpy.restart_interaction()

    def solved_puzzles_convert():
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
            evidence_init()
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

        elif name not in single_difficulty_puzzles:
            if name not in persistent.solved_puzzles[difficulty_level]:
                persistent.solved_puzzles[difficulty_level].append(name)

            store.difficulties_cleared[name] = difficulty_level

    def puzzle_cleared(name):
        if name in single_difficulty_puzzles and persistent.solved_puzzles[name]:
            return True
        if name in persistent.solved_puzzles[difficulty_level]:
            return True
        return False

    def lowest_cleared_difficulty():
        if skip_used:
            return 0

        lowest = 3
        for k,v in difficulties_cleared.items():
            if v == None:
                lowest = 0
                break
            elif v < lowest:
                lowest = v
        return lowest

    def puzzle_achievements():
        cleared = lowest_cleared_difficulty()
        if cleared:
            if cleared >= 1:
                Achievement.add(achievement_difficulty1)

            if cleared >= 2:
                Achievement.add(achievement_difficulty2)

            if cleared >= 3:
                Achievement.add(achievement_difficulty3)

    #some drag puzzles reset their positions after load
    def reset_puzzles_after_load():
        #room1

        #room2
        word_init()

        #room3
        scrapbook_init()
        pass

    config.after_load_callbacks.append(reset_puzzles_after_load)

default persistent.solved_puzzles = {1:[], 2:[], 3:[], "tutorial":False, "room1_meta":False, "room2_meta":False, "room3_meta":False}

screen skip_button(room, puzzle, puzzle_name, xalign=0.0, yalign=0.0, xoffset=0, yoffset=0):
    textbutton "SKIP":
        style "confirm_button" xalign xalign yalign yalign xoffset xoffset yoffset yoffset
        action If(puzzle_cleared(puzzle_name), [SetDict(room, puzzle, "solved"), If(puzzle_name in single_difficulty_puzzles, SetDict(difficulties_cleared, puzzle_name, difficulty_level), NullAction()), Return()],
            Confirm(If(difficulty_level > 1, _("Are you sure you want to skip this puzzle? \nYou could also {color=#00e7ff}lower the difficulty{/color} instead."), _("Are you sure you want to skip this puzzle?")), [SetDict(room, puzzle, "solved"), SetVariable("skip_used",True), Return()], NullAction()))

label after_load:
    if not hasattr(achievement_start, "id"):
        $ achievement_start = Achievement('start')
        $ achievement_tfng = Achievement('tfng')
        $ achievement_room1 = Achievement('room1')
        $ achievement_room2 = Achievement('room2')
        $ achievement_room3 = Achievement('room3')
        $ achievement_deadfirst = Achievement('deadfirst')
        $ achievement_deadall = Achievement('deadall')
        # $ achievement_wrong = Achievement('wrong')
        $ achievement_end1 = Achievement('end1')
        $ achievement_end2 = Achievement('end2')
        $ achievement_end3 = Achievement('end3')
        $ achievement_investigate = Achievement('investigate')
        $ achievement_difficulty1 = Achievement('difficulty1')
        $ achievement_difficulty2 = Achievement('difficulty2')
        $ achievement_difficulty3 = Achievement('difficulty3')
        $ achievement_platinum = Achievement('all')

        $ achievement_dead1 = Achievement('dead1')
        $ achievement_dead2 = Achievement('dead2')
        $ achievement_dead3 = Achievement('dead3')
        $ achievement_dead4 = Achievement('dead4')
        $ achievement_dead5 = Achievement('dead5')
        $ achievement_dead6 = Achievement('dead6')
        $ achievement_dead7 = Achievement('dead7')
        $ achievement_dead8 = Achievement('dead8')
        $ achievement_dead9 = Achievement('dead9')
        $ achievement_dead10 = Achievement('dead10')
        $ achievement_dead11 = Achievement('dead11')
        $ achievement_dead12 = Achievement('dead12')
        $ achievement_dead13 = Achievement('dead13')

    if cutting_board_group:
        $ reset_cutting_board_drags()
    if bomb:
        $ bomb.reset_drags()
    return
