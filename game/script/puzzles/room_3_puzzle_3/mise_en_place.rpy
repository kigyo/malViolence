default cb_tile = 100

default ingredients = ["bacon",
                       "strawberry",
                       "flour",
                       "snapper",
                       "butter",
                       "blueberry",
                       "egg",
                       "nut",
                       "milk"]

define ingredient_counts = {"bacon": 5,
                            "strawberry": 7,
                            "flour": 5,
                            "snapper": 6,
                            "butter": 7,
                            "blueberry": 9,
                            "egg": 8,
                            "nut": 2,
                            "milk": 3}

default bacon_count = 1
default strawberry_count = 1
default flour_count = 1
default snapper_count = 1
default butter_count = 1
default blueberry_count = 1
default egg_count = 1
default nut_count = 1
default milk_count = 1
default orange_count = 1
default almond_count = 1
default sprinkle_count = 1
default chocolate_chip_count = 1
default bread_count = 1
default peach_count = 1
default cooking_error = None

default cutting_board_input = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                              [0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [4, 0, 0, 0, 0, 0, 0, 0, 9, 0, 8],
                              [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0]]

default cutting_board_group = None

init python:
    def ingredient_dragged(drags, drop):
        store.cooking_error = None
        drag = drags[0]
        if len(drag.drag_name) == 4:
            cutting_board_group.remove(drag)
            cutting_board_data[drag.drag_name[2]][drag.drag_name[1]] = 0
            setattr(renpy.store, "%s_count" % drag.drag_name[0],
                    getattr(renpy.store, "%s_count" % drag.drag_name[0], 0)-1)
        else:
            drag.snap(drag.drag_name[1], drag.drag_name[2])
        renpy.retain_after_load()
        renpy.restart_interaction()

    def cutting_board_dropped(drop, drags):
        drag = drags[0]
        if len(drop.drag_name) == 4:
            x = drop.drag_name[1]
            y = drop.drag_name[2]
            cutting_board_group.remove(drop)
            setattr(renpy.store, "%s_count" % drop.drag_name[0],
                    getattr(renpy.store, "%s_count" % drop.drag_name[0], 0)-1)
        else:
            x = drop.drag_name[0]
            y = drop.drag_name[1]

        setattr(renpy.store, "%s_count" % drag.drag_name[0],
                getattr(renpy.store, "%s_count" % drag.drag_name[0], 0)+1)

        cutting_board_data[y][x] = ingredients.index(drag.drag_name[0])+1
        d = Drag(Transform(drag.drag_name[0], zoom=cb_tile/100),
                 pos=(70+x*cb_tile, 205+y*cb_tile),
                 drag_name=(drag.drag_name[0], x, y, "obj"),
                 droppable=True,
                 dragged=ingredient_dragged,
                 dropped=cutting_board_dropped)
        cutting_board_group.add(d)
        d.snap(70+x*cb_tile, 205+y*cb_tile)

        renpy.retain_after_load()
        renpy.restart_interaction()

    def check_board():
        win = True

        # checked = []
        # for y in range(len(cutting_board_input)):
        #     l = []
        #     checked.append(l)
        #     for x in range(len(cutting_board_input[0])):
        #         l.append(False)

        for y in range(len(cutting_board_input)):
            for x in range(len(cutting_board_input[0])):
                if cutting_board_input[y][x]:
                    if not check_sprawl(x, y):
                        win = False

        if win:
            store.room3["cooking"] = "solved"
            clear_puzzle("room3_3")
            return True
        elif ("dead13" in persistent.dead_ends and not preferences.hard_mode):
            renpy.restart_interaction()
            #TODO: some kind of error feedback
            pass
        else:
            renpy.jump("cooking_game_over")

    def check_sprawl(x, y, checked=None):
        if checked is None:
            checked = [(x, y)]

            count = 0
            for cy in range(len(cutting_board_data)):
                for cx in range(len(cutting_board_data[0])):
                    if cutting_board_data[y][x] == cutting_board_data[cy][cx]:
                        count += 1

            if count != ingredient_counts[ingredients[cutting_board_data[y][x]-1]]:
                store.cooking_error = ingredients[cutting_board_data[y][x]-1]
                return False

            return all([check_sprawl(x+1, y, checked),
                        check_sprawl(x-1, y, checked),
                        check_sprawl(x, y+1, checked),
                        check_sprawl(x, y-1, checked)])
        else:
            if not 0 <= x < len(cutting_board_input[0]) or \
               not 0 <= y < len(cutting_board_input) or \
               not cutting_board_data[y][x] or\
               (x, y) in checked:
                   return True
            else:
                if cutting_board_data[y][x] == cutting_board_data[checked[0][1]][checked[0][0]]:
                    checked.append((x, y))
                    return all([check_sprawl(x+1, y, checked),
                                check_sprawl(x-1, y, checked),
                                check_sprawl(x, y+1, checked),
                                check_sprawl(x, y-1, checked)])
                else:
                    if not cooking_error:
                        store.cooking_error = [x,y]
                    return False

label init_mise_en_place:
    $ bacon_count = 1
    $ strawberry_count = 1
    $ flour_count = 1
    $ snapper_count = 1
    $ butter_count = 1
    $ blueberry_count = 1
    $ egg_count = 1
    $ nut_count = 1
    $ milk_count = 1
    $ orange_count = 1
    $ almond_count = 1
    $ sprinkle_count = 1
    $ chocolate_chip_count = 1
    $ bread_count = 1
    $ peach_count = 1

    $ cooking_error = None

    $ cutting_board_group = DragGroup()

    if difficulty_level == 1:
        $ cb_tile = 120
        $ ingredients = ["bacon",
                         "strawberry",
                         "flour",
                         "snapper",
                         "butter",
                         "blueberry",
                         "egg"]
        $ ingredient_counts = {"bacon": 5,
                               "strawberry": 6,
                               "flour": 2,
                               "snapper": 7,
                               "butter": 3,
                               "blueberry": 6,
                               "egg": 5}
        $ cutting_board_input = [[0, 0, 0, 0, 1, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 2, 0, 0, 0],
                                 [0, 6, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 7, 0, 0, 0, 0, 4, 0],
                                 [0, 0, 0, 0, 0, 0, 5, 0, 3],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    elif difficulty_level == 2:
        $ cb_tile = 100
        $ ingredients = ["bacon",
                         "strawberry",
                         "flour",
                         "snapper",
                         "butter",
                         "blueberry",
                         "egg",
                         "nut",
                         "milk"]
        $ ingredient_counts = {"bacon": 5,
                               "strawberry": 7,
                               "flour": 5,
                               "snapper": 6,
                               "butter": 7,
                               "blueberry": 9,
                               "egg": 8,
                               "nut": 2,
                               "milk": 3}
        $ cutting_board_input = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [4, 0, 0, 0, 0, 0, 0, 0, 9, 0, 8],
                                 [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0]]
    elif difficulty_level == 3:
        $ cb_tile = 80
        $ ingredients = ["bacon",
                         "strawberry",
                         "flour",
                         "snapper",
                         "butter",
                         "blueberry",
                         "egg",
                         "nut",
                         "milk",
                         "orange",
                         "almond",
                         "sprinkle",
                         "chocolate_chip",
                         "bread",
                         "peach"]
        $ ingredient_counts = {"bacon": 5,
                               "strawberry": 6,
                               "flour": 4,
                               "snapper": 8,
                               "butter": 7,
                               "blueberry": 6,
                               "egg": 4,
                               "nut": 6,
                               "milk": 7,
                               "orange": 2,
                               "almond": 5,
                               "sprinkle": 9,
                               "chocolate_chip": 2,
                               "bread": 5,
                               "peach": 3}
        $ cutting_board_input = [[ 0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  5,  0,  6,  0],
                                 [ 0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                                 [ 0,  0,  2,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0],
                                 [ 0,  0,  0,  0, 12,  0,  0,  0,  0,  0,  0, 15,  0,  7],
                                 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                                 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                                 [ 0, 13,  0,  0, 11,  0,  0,  0,  9,  0,  0,  0,  0,  0],
                                 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                                 [14,  0,  0,  0,  0,  0,  0, 10,  0,  0,  8,  0,  0,  0]]
    python:
        cutting_board_data = [row[:] for row in cutting_board_input]

        # x = 115-int(cb_tile/2)
        # for i in ingredients:
        #     cutting_board_group.add(Drag(Transform(i, zoom=cb_tile/100),
        #                                  pos=(x, int(cb_tile/2)),
        #                                  drag_name=(i, x, int(cb_tile/2)),
        #                                  dragged=ingredient_dragged))
        #     x += cb_tile+25

        for y in range(len(cutting_board_input)):
            for x in range(len(cutting_board_input[0])):
                if cutting_board_input[y][x]:
                    cutting_board_group.add(Drag(Fixed(Transform("fixed_cutting_board_tile", zoom=cb_tile/100), Transform(ingredients[cutting_board_input[y][x]-1], zoom=cb_tile/100), fit_first=True),
                                                 pos=(70+x*cb_tile, 205+y*cb_tile),
                                                 droppable=True,
                                                 draggable=False))
                    cutting_board_group.add(Drag(Transform(ingredients[cutting_board_input[y][x]-1], zoom=cb_tile/100),
                                                 pos=(70+x*cb_tile, 205+y*cb_tile),
                                                 drag_name=(ingredients[cutting_board_input[y][x]-1], 70+x*cb_tile, 205+y*cb_tile),
                                                 dragged=ingredient_dragged))
                else:
                    cutting_board_group.add(Drag(Transform("cutting_board_tile", zoom=cb_tile/100),
                                                 pos=(70+x*cb_tile, 205+y*cb_tile),
                                                 xysize=(100, 100),
                                                 drag_name=(x, y),
                                                 droppable=True,
                                                 draggable=False,
                                                 dropped=cutting_board_dropped))
    return

label reset_cutting_board():
    call init_mise_en_place from _call_init_mise_en_place_1
    hide screen mise_en_place
    call screen mise_en_place

style ingredients_text:
    color "#6f593d"
    size 24
    xsize 500

style ingredients_label_text:
    color "#62574a"

style ingredients_frame:
    background Frame("cutting_board_tile", 10, 10)

style ingredients_button_text:
    idle_color "#6f593d"
    hover_color "#C1C0BE"

screen mise_en_place(interactable=True):
    sensitive (not inspect and not _menu)
    modal True
    tag puzzle
    layer "puzzles"

    frame style "puzzle_frame" padding 0,0,50,40:

        frame style_prefix "ingredients":
            xysize (600, 820)
            pos (1250, 130)
            vbox:
                xalign 0.5

                label "Ingredients" xalign 0.5
                if difficulty_level == 1:
                    text "- 5 pieces of bacon" strikethrough bacon_count == ingredient_counts["bacon"]:
                        if cooking_error == "bacon":
                            color "#d20000" bold True
                    text "- 6 strawberries" strikethrough strawberry_count == ingredient_counts["strawberry"]:
                        if cooking_error == "strawberry":
                            color "#d20000" bold True
                    text "- 2 cups of flour" strikethrough flour_count == ingredient_counts["flour"]:
                        if cooking_error == "flour":
                            color "#d20000" bold True
                    text "- 7 snappers" strikethrough snapper_count == ingredient_counts["snapper"]:
                        if cooking_error == "snapper":
                            color "#d20000" bold True
                    text "- 3 sticks of butter" strikethrough butter_count == ingredient_counts["butter"]:
                        if cooking_error == "butter":
                            color "#d20000" bold True
                    text "- 6 blueberries" strikethrough blueberry_count == ingredient_counts["blueberry"]:
                        if cooking_error == "blueberry":
                            color "#d20000" bold True
                    text "- 5 eggs" strikethrough egg_count == ingredient_counts["egg"]:
                        if cooking_error == "egg":
                            color "#d20000" bold True
                    null height 5
                elif difficulty_level == 2:
                    hbox:
                        spacing 20
                        vbox:
                            text "- 5 pieces of bacon" strikethrough bacon_count == ingredient_counts["bacon"]:
                                if cooking_error == "bacon":
                                    color "#d20000" bold True
                            text "- 7 strawberries" strikethrough strawberry_count == ingredient_counts["strawberry"]:
                                if cooking_error == "strawberry":
                                    color "#d20000" bold True
                            text "- 5 cups of flour" strikethrough flour_count == ingredient_counts["flour"]:
                                if cooking_error == "flour":
                                    color "#d20000" bold True
                            text "- 6 snappers" strikethrough snapper_count == ingredient_counts["snapper"]:
                                if cooking_error == "snapper":
                                    color "#d20000" bold True
                            text "- 7 sticks of butter" strikethrough butter_count == ingredient_counts["butter"]:
                                if cooking_error == "butter":
                                    color "#d20000" bold True
                            text "- 9 blueberries" strikethrough blueberry_count == ingredient_counts["blueberry"]:
                                if cooking_error == "blueberry":
                                    color "#d20000" bold True
                        vbox:
                            text "- 8 eggs" strikethrough egg_count == ingredient_counts["egg"]:
                                if cooking_error == "egg":
                                    color "#d20000" bold True
                            text "- 2 nuts" strikethrough nut_count == ingredient_counts["nut"]:
                                if cooking_error == "nut":
                                    color "#d20000" bold True
                            text "- 3 cartons of milk" strikethrough milk_count == ingredient_counts["milk"]:
                                if cooking_error == "milk":
                                    color "#d20000" bold True
                    null height 5
                elif difficulty_level == 3:
                    hbox:
                        spacing 20
                        vbox:
                            text "- 5 pieces of bacon" strikethrough bacon_count == ingredient_counts["bacon"]:
                                if cooking_error == "bacon":
                                    color "#d20000" bold True
                            text "- 6 strawberries" strikethrough strawberry_count == ingredient_counts["strawberry"]:
                                if cooking_error == "strawberry":
                                    color "#d20000" bold True
                            text "- 4 cups of flour" strikethrough flour_count == ingredient_counts["flour"]:
                                if cooking_error == "flour":
                                    color "#d20000" bold True
                            text "- 8 snappers" strikethrough snapper_count == ingredient_counts["snapper"]:
                                if cooking_error == "snapper":
                                    color "#d20000" bold True
                            text "- 7 sticks of butter" strikethrough butter_count == ingredient_counts["butter"]:
                                if cooking_error == "butter":
                                    color "#d20000" bold True
                            text "- 6 blueberries" strikethrough blueberry_count == ingredient_counts["blueberry"]:
                                if cooking_error == "blueberry":
                                    color "#d20000" bold True
                            text "- 4 eggs" strikethrough egg_count == ingredient_counts["egg"]:
                                if cooking_error == "egg":
                                    color "#d20000" bold True
                            text "- 6 nuts" strikethrough nut_count == ingredient_counts["nut"]:
                                if cooking_error == "nut":
                                    color "#d20000" bold True

                        vbox:
                            text "- 7 cartons of milk" strikethrough milk_count == ingredient_counts["milk"]:
                                if cooking_error == "milk":
                                    color "#d20000" bold True
                            text "- 2 oranges" strikethrough orange_count == ingredient_counts["orange"]:
                                if cooking_error == "orange":
                                    color "#d20000" bold True
                            text "- 5 almonds" strikethrough almond_count == ingredient_counts["almond"]:
                                if cooking_error == "almond":
                                    color "#d20000" bold True
                            text "- 9 pinches of sprinkles" strikethrough sprinkle_count == ingredient_counts["sprinkle"]:
                                if cooking_error == "sprinkle":
                                    color "#d20000" bold True
                            text "- 2 chocolate chips" strikethrough chocolate_chip_count == ingredient_counts["chocolate_chip"]:
                                if cooking_error == "chocolate_chip":
                                    color "#d20000" bold True
                            text "- 5 slices of bread" strikethrough bread_count == ingredient_counts["bread"]:
                                if cooking_error == "bread":
                                    color "#d20000" bold True
                            text "- 3 peaches" strikethrough peach_count == ingredient_counts["peach"]:
                                if cooking_error == "peach":
                                    color "#d20000" bold True
                    null height 5

                label "Instructions" xalign 0.5
                text "- Always begin cooking with {i}{b}~mise en place~.{/i}{/b}"
                text "- {b}Drag items onto the board to arrange them.{/b} Look at the ingredients list to figure out how many of each item should be laid out on the counter."
                text "- {b}All items of the same type{/b} should touch each other {b}at right angles{/b}"
                text "- {b}Items of different types{/b} should not touch at right angles, but can touch {b}diagonally.{/b}"
                text "- {b}Drag uneeded items{/b} to the {b}trash.{/b}"

                null height 30

        hbox xalign 1.0 yalign 1.0 ysize 100 spacing 112:
            textbutton "RESET" style "confirm_button" action Call("reset_cutting_board") text_color "#fff" align (0.0, 0.5)
            textbutton "TRASH" style "confirm_button" text_color "#fff" sensitive not inspect xalign 0.0 yalign 0.5
            textbutton "SUBMIT" style "confirm_button" action Function(check_board) sensitive not inspect xalign 0.5 yalign 0.5 xoffset -40
            textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] sensitive not inspect xalign 1.0 yalign 0.5

        # add "cutting_board" pos (65, 200)
        add "#CFC6BC" pos (65, 200) xysize(cb_tile*len(cutting_board_input[0])+10, cb_tile*len(cutting_board_input)+10)

        for y in range(len(cutting_board_input)):
            for x in range(len(cutting_board_input[0])):
                fixed:
                    pos (70+x*cb_tile, 205+y*cb_tile)
                    fit_first True
                    if cutting_board_input[y][x]:
                        pass
                        add "fixed_cutting_board_tile":
                            zoom cb_tile/100
                        if cooking_error == [x,y]:
                            add Solid("#d20000")
                        add ingredients[cutting_board_input[y][x]-1]:
                            zoom cb_tile/100
                    elif cutting_board_data[y][x]:
                        add "cutting_board_tile":
                            zoom cb_tile/100
                        if cooking_error == [x,y]:
                            add Solid("#d20000")
                        add ingredients[cutting_board_data[y][x]-1]:
                            zoom cb_tile/100
                    else:
                        add "cutting_board_tile":
                            zoom cb_tile/100

        # $ x = 115
        # for i in ingredients:
        #     use ingredient_base(i, x)
        #     $ x += cb_tile+25

        if not inspect:
            add cutting_board_group

        for y in range(len(cutting_board_input)):
            for x in range(len(cutting_board_input[0])):
                fixed:
                    pos (70+x*cb_tile, 205+y*cb_tile)
                    xysize (cb_tile, cb_tile)
                    if cutting_board_input[y][x]:
                        $ amt = ingredient_counts[ingredients[cutting_board_data[y][x]-1]] - getattr(renpy.store, "%s_count" % ingredients[cutting_board_data[y][x]-1])
                        text "[amt]" outlines[(absolute(1), "#000", absolute(0), absolute(0))] align (1.0, 1.0) yoffset 12

        if isinstance(cooking_error,list):
            add Solid("#d20000") pos (70+cooking_error[0]*cb_tile, 205+cooking_error[1]*cb_tile) xysize (cb_tile, cb_tile) alpha 0.5

    if "room3_3" in persistent.solved_puzzles or not preferences.hard_mode:
        textbutton "SKIP" style "confirm_button" action [SetDict(room3, "cooking", "solved"), Return()] xpos 40 yalign 1.0 yoffset -50

    if config.developer:
        hbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room3, "cooking", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("cooking_game_over")] style "main_menu_button"

screen ingredient_base(ingredient, x):
    frame:
        background Frame("cutting_board_tile", 2, 2)
        xysize (cb_tile, cb_tile)
        pos (x, cb_tile)
        anchor (0.5, 0.5)
        add ingredient:
            align(0.5, 0.5)
            zoom cb_tile/100

screen ingredient(ingredient, x):
    drag:
        pos (x, cb_tile)
        xysize (cb_tile, cb_tile)
        anchor(0.5, 0.5)
        drag_raise True
        add ingredient:
            zoom cb_tile/100
