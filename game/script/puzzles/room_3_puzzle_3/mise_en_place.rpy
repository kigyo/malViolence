define ingredients = ["bacon",
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
                            "butter": 6,
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
default cooking_error = None

define cutting_board_input = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                              [0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [4, 0, 0, 0, 0, 0, 0, 0, 9, 0, 8],
                              [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0]]

default cutting_board_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
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
            drag.snap(drag.drag_name[1]-50, drag.drag_name[2]-50)
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
        d = Drag(drag.drag_name[0],
                 pos=(70+x*100, 205+y*100),
                 drag_name=(drag.drag_name[0], x, y, "obj"),
                 droppable=True,
                 dragged=ingredient_dragged,
                 dropped=cutting_board_dropped)
        cutting_board_group.add(d)
        d.snap(70+x*100, 205+y*100)

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
    $ cooking_error = None

    $ cutting_board_group = DragGroup()
    python:
        cutting_board_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                              [0, 0, 3, 0, 0, 0, 0, 6, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [4, 0, 0, 0, 0, 0, 0, 0, 9, 0, 8],
                              [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0]]

        x = 115
        for i in ingredients:
            cutting_board_group.add(Drag(i,
                                         pos=(x, 100),
                                         anchor=(0.5, 0.5),
                                         drag_name=(i, x, 100),
                                         dragged=ingredient_dragged))
            x += 125

        for y in range(len(cutting_board_input)):
            for x in range(len(cutting_board_input[0])):
                if cutting_board_input[y][x]:
                    cutting_board_group.add(Drag(Fixed("fixed_cutting_board_tile", ingredients[cutting_board_input[y][x]-1], fit_first=True),
                                                 pos=(70+x*100, 205+y*100),
                                                 droppable=True,
                                                 draggable=False))
                else:
                    cutting_board_group.add(Drag("cutting_board_tile",
                                                 pos=(70+x*100, 205+y*100),
                                                 xysize=(100, 100),
                                                 drag_name=(x, y),
                                                 droppable=True,
                                                 draggable=False,
                                                 dropped=cutting_board_dropped))
    return

label reset_cutting_board():
    call init_mise_en_place
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
    modal True
    tag puzzle
    layer "puzzles"

    frame style "puzzle_frame" padding 0,0,50,40:

        frame style_prefix "ingredients":
            xysize (600, 860)
            pos (1250, 50)
            vbox:
                xalign 0.5

                label "Ingredients" xalign 0.5
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
                text "- 6 sticks of butter" strikethrough butter_count == ingredient_counts["butter"]:
                    if cooking_error == "butter":
                        color "#d20000" bold True
                text "- 9 blueberries" strikethrough blueberry_count == ingredient_counts["blueberry"]:
                    if cooking_error == "blueberry":
                        color "#d20000" bold True
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

        add "cutting_board" pos (65, 200)

        for y in range(len(cutting_board_input)):
            for x in range(len(cutting_board_input[0])):
                fixed:
                    pos (70+x*100, 205+y*100)
                    fit_first True
                    if cutting_board_input[y][x]:
                        add "fixed_cutting_board_tile"
                        if cooking_error == [x,y]:
                            add Solid("#d20000")
                        add ingredients[cutting_board_input[y][x]-1]
                    elif cutting_board_data[y][x]:
                        add "cutting_board_tile"
                        if cooking_error == [x,y]:
                            add Solid("#d20000")
                        add ingredients[cutting_board_data[y][x]-1]
                    else:
                        add "cutting_board_tile"

        $ x = 115
        for i in ingredients:
            use ingredient_base(i, x)
            $ x += 125

        if not inspect:
            add cutting_board_group

        if isinstance(cooking_error,list):
            add Solid("#d20000") pos (70+cooking_error[0]*100, 205+cooking_error[1]*100) xysize (100, 100) alpha 0.5

    if "room3_3" in persistent.solved_puzzles:
        textbutton "SKIP" style "confirm_button" action [SetDict(room3, "cooking", "solved"), Return()] pos (40,50)

    if config.developer:
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room3, "cooking", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("cooking_game_over")] style "main_menu_button"

screen ingredient_base(ingredient, x):
    frame:
        background "cutting_board_tile"
        xysize (100, 100)
        pos (x, 100)
        anchor (0.5, 0.5)
        add ingredient:
            align(0.5, 0.5)

screen ingredient(ingredient, x):
    drag:
        pos (x, 100)
        anchor(0.5, 0.5)
        drag_raise True
        add ingredient
