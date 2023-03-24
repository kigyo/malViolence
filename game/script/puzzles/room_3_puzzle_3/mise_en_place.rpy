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
            renpy.jump("solved_room_3_puzzle_3")
        else:
            renpy.jump("failed_room_3_puzzle_3")

    def check_sprawl(x, y, checked=None):
        if checked is None:
            checked = [(x, y)]

            count = 0
            for cy in range(len(cutting_board_data)):
                for cx in range(len(cutting_board_data[0])):
                    if cutting_board_data[y][x] == cutting_board_data[cy][cx]:
                        count += 1

            if count != ingredient_counts[ingredients[cutting_board_data[y][x]-1]]:
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
    style_prefix "ingredients"
    frame:
        xysize (600, 860)
        pos (1250, 50)
        vbox:
            xalign 0.5

            label "Ingredients" xalign 0.5
            if bacon_count >= ingredient_counts["bacon"]:
                text "{s}5 pieces of bacon{/s}"
            else:
                text "5 pieces of bacon"
            if strawberry_count >= ingredient_counts["strawberry"]:
                text "{s}7 strawberries{/s}"
            else:
                text "7 strawberries"
            if flour_count >= ingredient_counts["flour"]:
                text "{s}5 cups of flour{/s}"
            else:
                text "5 cups of flour"
            if snapper_count >= ingredient_counts["snapper"]:
                text "{s}6 snappers{/s}"
            else:
                text "6 snappers"
            if butter_count >= ingredient_counts["butter"]:
                text "{s}6 sticks of butter{/s}"
            else:
                text "6 sticks of butter"
            if blueberry_count >= ingredient_counts["blueberry"]:
                text "{s}9 blueberries{/s}"
            else:
                text "9 blue berries"
            if egg_count >= ingredient_counts["egg"]:
                text "{s}8 eggs{/s}"
            else:
                text "8 eggs"
            if nut_count >= ingredient_counts["nut"]:
                text "{s}2 nuts{/s}"
            else:
                text "2 nuts"
            if milk_count >= ingredient_counts["milk"]:
                text "{s}3 cartons of milk{/s}"
            else:
                text "3 cartons of milk"

            label "Instructions" xalign 0.5
            text "- Always begin cooking with {i}~mise en place~{/i}."
            text "- Drag items onto the board to arrange them them. Look at the ingredients list to figure out how many of each item should be laid out."
            text "- All items of the same type should be touching eachother orthganally."
            text "- Items of different types should not touch orthoganlly but can touch diagnally."
            text "- Drag uneeded items to the trash."

            null height 30

            hbox:
                xalign 0.5
                spacing 100
                frame:
                    textbutton "Trash"
                frame:
                    textbutton "Submit" action Function(check_board)

    add "cutting_board" pos (65, 200)

    for y in range(len(cutting_board_input)):
        for x in range(len(cutting_board_input[0])):
            fixed:
                pos (70+x*100, 205+y*100)
                fit_first True
                if cutting_board_input[y][x]:
                    add "fixed_cutting_board_tile"
                    add ingredients[cutting_board_input[y][x]-1]
                elif cutting_board_data[y][x]:
                    add "cutting_board_tile"
                    add ingredients[cutting_board_data[y][x]-1]
                else:
                    add "cutting_board_tile"

    $ x = 115
    for i in ingredients:
        use ingredient_base(i, x)
        $ x += 125

    if interactable:
        add cutting_board_group

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
