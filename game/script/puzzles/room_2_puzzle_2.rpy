default panopt = None

init python:
    class Panopticon(renpy.Displayable, NoRollback):
        adt = 0.25
        def __init__(self,
                     dependencies={0: [1, 3],
                                   1: [2],
                                   2: [0, 4],
                                   3: [2],
                                   4: [1, 3]},
                     solution = [[0, 4, 2, 1, 2]],
                     rings=["room2_2_color5",
                            "room2_2_color4",
                            "room2_2_color3",
                            "room2_2_color2",
                            "room2_2_color1"],
                     core="room2_2_base",
                     overlay="room2_2_overlay",
                     spokes=5,
                     center=(config.screen_width/2, config.screen_height/2)):
            super(Panopticon, self).__init__(self)
            self.solutions = []
            for sol in solution:
                self.solutions.extend([[(s+i)%spokes for s in sol] for i in range(spokes)])
            self.dependencies = dependencies
            self.turning = False
            self.img = rings
            self.core = core
            self.overlay = overlay
            self.rings = [Transform(r) for r in rings]
            self.center = center
            for r in self.rings:
                r.rotate = 0
                r.update()
            self.starts = [0 for r in rings]
            self.ends = [0 for r in rings]

            self.slots = [0 for r in rings]

            self.positions = [i*(360.0/spokes) for i in range(spokes)]

            self.focused = 0
            self.interactable = True
            self.elapsed = 0.0
            self.st = 0.0
            self.start = 0
            self.dt = 0
            self.ts = 0
            self.state = None

        def render(self, width, height, st, at):
            elapsed = max(st - self.st, 0.0)
            self.elapsed += elapsed
            self.st = st
            if self.turning:
                mx, my = renpy.get_mouse_pos()
                mx -= self.center[0]
                my -= self.center[1]
                da = self.start - math.degrees(math.atan2(mx, my))
                self.rings[self.focused].rotate = (self.starts[self.focused] + da) % 360
                self.rings[self.focused].update()
                for d in self.dependencies.get(self.focused, []):
                    self.rings[d].rotate = (self.starts[d] - da) % 360
                    self.rings[d].update()
            elif not self.interactable:
                self.rings[self.focused].rotate = self.starts[self.focused]- \
                    (self.starts[self.focused]-self.ends[self.focused])*(self.dt/Panopticon.adt)
                self.rings[self.focused].update()

                for d in self.dependencies.get(self.focused, []):
                    self.rings[d].rotate = self.starts[d]- \
                        (self.starts[d]-self.ends[d])*(self.dt/Panopticon.adt)
                    self.rings[d].update()

                self.dt += elapsed

                if self.dt >= Panopticon.adt:
                    self.starts[self.focused] = self.ends[self.focused]
                    self.rings[self.focused].rotate = self.ends[self.focused]
                    self.rings[self.focused].update()
                    for d in self.dependencies.get(self.focused, []):
                        self.starts[d] = self.ends[d]
                        self.rings[d].rotate = self.ends[d]
                        self.rings[d].update()
                    if self.slots in self.solutions:
                        self.state = "won"
                        store.room2["panopticon"] = "solved"
                    elif panopticon_moves >= panopticon_move_limit and not ("dead8" in persistent.dead_ends and not preferences.hard_mode):
                        self.state = "lost"
                    else:
                        self.interactable = True

            rv = renpy.Render(config.screen_width, config.screen_height)
            for r in self.rings:
                r = renpy.render(r, 700, 700, st, st)
                rv.blit(r, (0, 0))
            renpy.redraw(self, 0.0)
            return rv

        def check_angle(self):
            pass

        def start_turn(self):
            if self.reticle == -1 or not self.interactable: return
            self.turning = True
            mx, my = renpy.get_mouse_pos()
            mx -= self.center[0]
            my -= self.center[1]
            self.start = math.degrees(math.atan2(mx, my))
            self.focused = self.reticle

        def stop_turn(self):
            self.turning = False
            if self.starts[self.focused] == self.rings[self.focused].rotate:
                return
            slot = 0
            dist = abs(360 - self.rings[self.focused].rotate)
            for i in range(len(self.positions)):
                d = abs(self.positions[i] - self.rings[self.focused].rotate)
                if d < dist:
                    slot = i
                    dist = d
            if slot != self.slots[self.focused]:
                SetVariable("panopticon_moves", panopticon_moves+1)()
                renpy.restart_interaction()
            ds = self.slots[self.focused] - slot

            self.set_slot(self.focused, slot)

            for d in self.dependencies.get(self.focused, []):
                self.set_slot(d, (self.slots[d]+ds)%5)
            self.dt = 0.0
            self.st = self.elapsed
            self.interactable = False

        def set_slot(self, i, slot):
            self.starts[i] = self.rings[i].rotate
            self.slots[i] = slot
            self.ends[i] = self.positions[slot]
            if self.ends[i] == 0 and self.starts[i] > 180:
                self.starts[i] = -(360-self.rings[i].rotate)

        def set_focus(self, i):
            self.reticle = i

        def event(self, ev, x, y, st):
            if ev.type == pygame_sdl2.MOUSEBUTTONDOWN and ev.button is 1:
                self.start_turn()
            elif ev.type == pygame_sdl2.MOUSEBUTTONUP and ev.button is 1:
                self.stop_turn()
            return None

        def __eq__(self, other):
            return False

image panopt_key:
    "key"
    zoom 0.5

transform panopticon_button():
    alpha 1.0

# screen panopticon_test(panopt, interactable=True):
screen room2_panopticon(pan=None, interactable=True):
    sensitive (not inspect and not _menu)
    modal True
    tag puzzle
    layer "puzzles"
    zorder 5

    if difficulty_level != panopticon_level:
        timer 0.1 action Function(panopticon_init, True)

    if panopt.state:
        timer 0.01 action If(panopt.state=="won", true=Return(), false=Jump("panopticon_game_over"))

    frame style "puzzle_frame":
        imagebutton:
            idle "#ffffff01"
            action NullAction()
            hovered Function(panopt.set_focus, -1)
        fixed:
            align (0.15, 0.5)
            offset (-25, 40)
            fit_first True
            for i in range(len(panopt.img)):
                imagebutton:
                    idle panopt.img[i]
                    at panopticon_button
                    align (0.5, 0.5)
                    focus_mask True
                    action NullAction()
                    hovered Function(panopt.set_focus, i)
            add panopt.core:
                align (0.5, 0.5)
                if difficulty_level == 3:
                    zoom 1.05
        fixed:
            offset (0, 45)
            if interactable:
                add panopt

        fixed:
            align (0.15, 0.5)
            offset (-25, 40)
            fit_first True
            add panopt.overlay:
                align (0.5, 0.5)
                alpha 0.5
            add panopt.core:
                align (0.5, 0.5)
                if difficulty_level == 3:
                    zoom 1.05
        # frame:
        #     xysize (10, 10)
        #     anchor (0.5, 0.5)
        #     pos (500, 540)

        fixed xsize 775 yfill True xalign 1.0:
            vbox spacing 50:
                yoffset -20
                style_prefix "puzzle_description"
                null height 10
                label _("Instructions")
                text _("In a stealthy campaign, {color=#fff}Cautionne has managed to take control of a STOP holding center,{/color} where several young test subjects are being held in a futuristic panopticon.\n\nTo give them the best chance of survival, Cautionne needs to {color=#fff}rearrange the cells so that each group of escaping testees is balanced.{/color}\n\nThese groups are shown as {color=#fff}a circle, a triangle, a square{/color} and {color=#fff}an X.{/color}\n\nHowever, the bureaucratic systems have left only the bare minimum operating instructions on how to operate the panopticon.")
                null height 50
                text _("{color=#fff}Help Cautionne properly arrange the cells according to the limitations of the system.{/color}")
            add "panopt_key" xalign 0.5 yoffset 680
            if ("dead8" in persistent.dead_ends and not preferences.hard_mode):
                textbutton "RESTART" action [Function(panopticon_init), Function(renpy.restart_interaction), Hide("room2_panopticon"), Function(renpy.restart_interaction), Show("room2_panopticon")] style "confirm_button" xalign 0.0 yalign 1.0 at zoomed(0.75)
            textbutton "RETURN" action [SetVariable("panopticon_selected", None), Return(), With(puzzle_hide)] style "confirm_button" xalign 1.0 yalign 1.0
        fixed xsize 1000:
            if not ("dead8" in persistent.dead_ends and not preferences.hard_mode):
                frame xalign 1.0:
                    text str(panopticon_moves) + "/" + str(panopticon_move_limit) style "main_menu_button"

        if puzzle_cleared("room2_2") or ("dead8" in persistent.dead_ends and not preferences.hard_mode) or not preferences.hard_mode:
            use skip_button(room2, "panopticon", "room2_2", xalign=1.0)

    if config.developer:
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room2, "panopticon", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("panopticon_game_over")] style "main_menu_button"

init python:
    def panopticon_init(start=False):
        store.panopticon_moves = 0

        if difficulty_level == 1:
            # store.panopticon_move_limit = 20
            # store.panopt = Panopticon(dependencies={0: [], 1: [], 2: []},
            #          solution = [[0, 1, 2]],

            #          rings=["panopt_1_0",
            #                 "panopt_1_1",
            #                 "panopt_1_2"],
            #                           core="panopt_1_core",
            #                           spokes=4,
            #                           overlay=Null(width=700, height=700),
            #                           center=(500,540))
            store.panopt = Panopticon(dependencies={0: [1],
                                                    1: [2],
                                                    2: [0]},
                                      solution=[[3, 3, 4], [3, 1, 1]],
                                      rings=["panopticon_2_0",
                                             "panopticon_2_1",
                                             "panopticon_2_2"],
                                      core="panopticon_2_core",
                                      # overlay=Null(width=700, height=700),
                                      center=(500,540))
        elif difficulty_level == 2:
            store.panopticon_move_limit = 15
            store.panopt = Panopticon(dependencies={0: [1],
                                                    1: [3],
                                                    2: [1],
                                                    3: [0, 2]},
                                      solution = [[4, 4, 2, 4]],
                                      rings=["panopt_2_0",
                                             "panopt_2_1",
                                             "panopt_2_2",
                                             "panopt_2_3"],
                                      # overlay=Null(width=700, height=700),
                                      core="panopt_2_core",
                                      center=(500,540))
        elif difficulty_level == 3:
            store.panopticon_move_limit = 15
            store.panopt = Panopticon(center=(500,540))

        store.panopticon_selected = None
        store.panopticon_config = [0,0,0,0,0]
        store.panopticon_pos = [0,0,0,0,0]
        store.panopticon_reverse = []

        store.panopticon_level = difficulty_level

        if not start:
            renpy.notify(_("Restarting..."))

    def room2_panopticon_set(dir):

        store.panopticon_moves += 1

        if dir == "r":
            store.panopticon_config[panopticon_selected] += 1
            if panopticon_config[panopticon_selected] == 5:
                store.panopticon_config[panopticon_selected] = 0

            store.panopticon_reverse = panopticon_effects[panopticon_selected]
            for i in panopticon_effects[panopticon_selected]:
                store.panopticon_config[i] -= 1
                if panopticon_config[i] == -1:
                    store.panopticon_config[i] = 4
        else:
            store.panopticon_reverse = [panopticon_selected]
            store.panopticon_config[panopticon_selected] -= 1
            if panopticon_config[panopticon_selected] == -1:
                store.panopticon_config[panopticon_selected] = 4

            for i in panopticon_effects[panopticon_selected]:
                store.panopticon_config[i] += 1
                if panopticon_config[i] == 5:
                    store.panopticon_config[i] = 0
        store.panopticon_selected = None
        renpy.retain_after_load()

        if room2_panopticon_valid_solution():
            store.room2["panopticon"] = "solved"
            clear_puzzle("room2_2")
            return True

        if panopticon_moves >= panopticon_move_limit and not ("dead8" in persistent.dead_ends and not preferences.hard_mode):
            renpy.jump("panopticon_game_over")

        return

    def room2_panopticon_valid_solution():
        for angle in range(5):
            solution_list = []
            for row in range(5):
                temp = panopticon_values[row][angle-panopticon_config[row]]
                print(str(angle) +", " + str(row) + ": " + str(temp))
                if temp in solution_list:
                    print("uh oh!")
                    return False
                solution_list.append(temp)
        return True

default panopticon_moves = 0
default panopticon_move_limit = 20

default panopticon_selected = None
default panopticon_config = [0,0,0,0,0]
default panopticon_pos = [0,0,0,0,0]
default panopticon_reverse = []
define panopticon_effects = {0:[1,3], 1:[2], 2:[0,4], 3:[2], 4:[1,3]}
#circle = 1, x = 2, triangle = 3, square = 4. starts at bottom
define panopticon_values = {0:[4,2,3,4,3], 1:[4,3,1,2,0], 2:[0,0,1,3,0], 3:[4,1,2,1,4], 4:[2,1,2,3,0]}

screen room2_panopticon_tmp():
    sensitive (not inspect and not _menu)
    modal True
    tag puzzle
    layer "puzzles"
    zorder 5

    frame style "puzzle_frame":
        imagebutton idle Null(1920,1080) action SetVariable("panopticon_selected", None)
        fixed xsize 775 yfill True xalign 1.0:
            vbox spacing 50:
                style_prefix "puzzle_description"
                null height 10
                label _("Instructions")
                text _("In a stealthy campaign, {color=#fff}Cautionne has managed to take control of a STOP holding center,{/color} where several young test subjects are being held in a futuristic panopticon.\n\nTo give them the best chance of survival, Cautionne needs to {color=#fff}rearrange the cells so that each group of escaping testees is balanced.{/color}\n\nThese groups are shown as {color=#fff}a circle, a triangle, a square{/color} and {color=#fff}an X.{/color}\n\nHowever, the bureaucratic systems have left only the bare minimum operating instructions on how to operate the panopticon.\n\n{color=#fff}Help Cautionne properly arrange the cells according to the limitations of the system.{/color}")
            if "dead8" in persistent.dead_ends or not preferences.hard_mode:
                textbutton "RESTART" action [Function(panopticon_init), Hide("room2_panopticon"), Function(renpy.restart_interaction)] style "confirm_button" xalign 0.0 yalign 1.0 at zoomed(0.75)
            textbutton "RETURN" action [SetVariable("panopticon_selected", None), Return(), With(puzzle_hide)] style "confirm_button" xalign 1.0 yalign 1.0

        fixed xsize 1000:
            for i in range(len(panopticon_config)):
                if panopticon_pos[i] == panopticon_config[i] * 72:
                    imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i)] focus_mask True align (0.5,0.5) at hover_darken, rotated(panopticon_pos[i])
                elif i in panopticon_reverse:
                    imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i)] focus_mask True align (0.5,0.5) at hover_darken, rotate_reverse(panopticon_pos[i])
                    $ panopticon_pos[i] = panopticon_config[i] * 72
                elif i not in panopticon_reverse:
                    imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i)] focus_mask True align (0.5,0.5) at hover_darken, rotate_anim(panopticon_pos[i])
                    $ panopticon_pos[i] = panopticon_config[i] * 72
            add "puzzles/room2_2_base.png" align (0.5,0.5)

            showif panopticon_selected != None:
                #add "gui/overlay/confirm.png"
                hbox xalign 0.5 yalign 0.5 spacing 20 at alphashow:
                    frame:
                        textbutton "COUNTERCLOCKWISE" xysize (370, 64) text_size 60 action [Function(room2_panopticon_set, "l")]
                    frame:
                        textbutton "CLOCKWISE" xysize (370, 64) text_size 60 action [Function(room2_panopticon_set, "r")]
            if not ("dead8" in persistent.dead_ends and not preferences.hard_mode):
                frame xalign 1.0:
                    text str(panopticon_moves) + "/" + str(panopticon_move_limit) style "main_menu_button"

        if puzzle_cleared("room2_2") or ("dead8" in persistent.dead_ends and not preferences.hard_mode) or not preferences.hard_mode:
            textbutton "SKIP" style "confirm_button" action [SetDict(room2, "panopticon", "solved"), Return()]


    if config.developer:
        #vbox yalign 0.05 xalign 0.5:
        #    hbox:
        #        for i in range(len(panopticon_config)):
        #            text str(panopticon_config[i]) + " "
        #    hbox:
        #        for i in range(len(panopticon_config)):
        #            text str(panopticon_pos[i]) + " "
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room2, "panopticon", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("panopticon_game_over")] style "main_menu_button"

transform rotate_anim(val):
    rotate val
    linear 0.2 rotate val+72
transform rotate_reverse(val):
    rotate val
    linear 0.2 rotate val-72

transform hover_darken:
    on hover:
        ease 0.2 matrixcolor BrightnessMatrix(-0.15)
    on idle:
        ease 0.2 matrixcolor BrightnessMatrix(0.0)
    on selected_idle:
        ease 0.2 matrixcolor BrightnessMatrix(-0.3)
    on selected_hover:
        ease 0.2 matrixcolor BrightnessMatrix(-0.3)
