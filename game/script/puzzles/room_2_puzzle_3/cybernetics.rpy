default cyb = None

define cybernetic_mask = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

default loop_colors = ["#FFFFFF",
                       "#31AFFF",
                       "#FF2F53",
                       "#FFF830",
                       "#34FFC8",
                       "#FF8C30",
                       "#4530FF",
                       "#CB30FF",
                       "#42C87C",
                       "#B262D7",
                       "#4165DC"]

default loop_data = None
default loop_counter = 1

define cybernetic_input = [
    [None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None,    4, None, None, None, None, None, None, None, None],
    [None,    0, None, None, None, None, None, None,    2, None, None, None],
    [None, None,    0, None, None,    6, None, None, None, None,    2, None],
    [None,    0, None, None,    2, None,    5, None, None, None, None, None],
    [None, None, None, None,    2, None, None,    3, None, None, None, None],
    [None, None,    1, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None]
]

define Pipe = Enum("cross",
                   "vertical",
                   "horizontal",
                   "left_top_bent",
                   "right_top_bent",
                   "left_bottom_bent",
                   "right_bottom_bent")

image fixed_vertical_piece:
    "fixed_straight_piece"

image fixed_horizontal_piece:
    rotate 90
    "fixed_straight_piece"

image fixed_left_top_bent_piece:
    "fixed_bent_piece"

image fixed_right_top_bent_piece:
    rotate 90
    "fixed_bent_piece"

image fixed_left_bottom_bent_piece:
    rotate 270
    "fixed_bent_piece"

image fixed_right_bottom_bent_piece:
    rotate 180
    "fixed_bent_piece"

image vertical_piece:
    "straight_piece"

image horizontal_piece:
    rotate 90
    "straight_piece"

image left_top:
    "bent_piece"

image right_top:
    rotate 90
    "bent_piece"

image left_bottom:
    rotate 180
    "bent_piece"

image right_piece:
    rotate 90
    "up_piece"

image down_piece:
    rotate 180
    "up_piece"

image left_piece:
    rotate 270
    "up_piece"

image right_bottom:
    rotate 270
    "bent_piece"

define z = 65.0

# TODO add T

init -1 python:
    import math

    class Cybernetic(renpy.Displayable, NoRollback):
        def __init__(self, x=170, y=150, w=12, h=10):
            super(Cybernetic, self).__init__(self)
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.pw = w*int(z)
            self.ph = h*int(z)
            self.data = [[[0,0,0,0] for x in range(self.w)] for y in range(self.h)]

            self.reticle = (-1, -1)
            self.cursor = (-1, -1)

            self.tracing = False
            self.last_trace = (0, 0)

        def get_coord(self):
            x, y = renpy.get_mouse_pos()
            if x > self.x and x < self.x + self.pw and \
               y > self.y and y < self.y + self.ph:
                   coord = (int(math.floor(x/z-self.x/z)), int(math.floor(y/z-self.y/z)))
                   if cybernetic_mask[coord[1]][coord[0]]:
                       self.reticle = coord
                       return True
            return False

        def render(self, width, height, st, at):
            rv = renpy.Render(config.screen_width, config.screen_height)
            renpy.redraw(self, 0.0 if self.tracing else 0.25)
            if self.tracing:
                self.check_reticle()
            return rv

        def check_reticle(self):
            if self.get_coord() and self.cursor != self.reticle:
                dx = self.reticle[0]-self.cursor[0]
                dy = self.reticle[1]-self.cursor[1]
                if (-1 <= dx <= 1 and not dy) or \
                   (-1 <= dy <= 1 and not dx):
                       if cybernetic_input[self.reticle[1]][self.reticle[0]]:
                           if not any([dx == 1 and Pipe.items[cybernetic_input[self.reticle[1]][self.reticle[0]]] in \
                                       [Pipe.cross, Pipe.horizontal, Pipe.left_top_bent, Pipe.left_bottom_bent], \
                                       dy == -1 and Pipe.items[cybernetic_input[self.reticle[1]][self.reticle[0]]] in \
                                       [Pipe.cross, Pipe.vertical, Pipe.left_bottom_bent, Pipe.right_bottom_bent], \
                                       dx == -1 and Pipe.items[cybernetic_input[self.reticle[1]][self.reticle[0]]] in \
                                       [Pipe.cross, Pipe.horizontal, Pipe.right_top_bent, Pipe.right_bottom_bent], \
                                       dy == 1 and Pipe.items[cybernetic_input[self.reticle[1]][self.reticle[0]]] in \
                                       [Pipe.cross, Pipe.vertical, Pipe.left_top_bent, Pipe.right_top_bent]]):
                                           return False
                       if cybernetic_input[self.cursor[1]][self.cursor[0]]:
                           if not any([dx == 1 and Pipe.items[cybernetic_input[self.cursor[1]][self.cursor[0]]] in \
                                   [Pipe.cross, Pipe.horizontal, Pipe.right_top_bent, Pipe.right_bottom_bent], \
                                   dy == -1 and Pipe.items[cybernetic_input[self.cursor[1]][self.cursor[0]]] in \
                                   [Pipe.cross, Pipe.vertical, Pipe.left_top_bent, Pipe.right_top_bent],
                                  dx == -1 and Pipe.items[cybernetic_input[self.cursor[1]][self.cursor[0]]] in \
                                  [Pipe.cross, Pipe.horizontal, Pipe.left_top_bent, Pipe.left_bottom_bent], \
                                  dy == 1 and Pipe.items[cybernetic_input[self.cursor[1]][self.cursor[0]]] in \
                                   [Pipe.cross, Pipe.vertical, Pipe.left_bottom_bent, Pipe.right_bottom_bent]]):
                                      return False
                       if dx == 1:
                           if self.data[self.reticle[1]][self.reticle[0]][2]:
                               self.data[self.reticle[1]][self.reticle[0]][2] = 0
                               self.data[self.cursor[1]][self.cursor[0]][0] = 0
                           else:
                               self.data[self.reticle[1]][self.reticle[0]][2] = 1
                               self.data[self.cursor[1]][self.cursor[0]][0] = 1
                       elif dx == -1:
                           if self.data[self.reticle[1]][self.reticle[0]][0]:
                               self.data[self.reticle[1]][self.reticle[0]][0] = 0
                               self.data[self.cursor[1]][self.cursor[0]][2] = 0
                           else:
                               self.data[self.reticle[1]][self.reticle[0]][0] = 1
                               self.data[self.cursor[1]][self.cursor[0]][2] = 1
                       elif dy == 1:
                           if self.data[self.reticle[1]][self.reticle[0]][3]:
                               self.data[self.reticle[1]][self.reticle[0]][3] = 0
                               self.data[self.cursor[1]][self.cursor[0]][1] = 0
                           else:
                               self.data[self.reticle[1]][self.reticle[0]][3] = 1
                               self.data[self.cursor[1]][self.cursor[0]][1] = 1
                       elif dy == -1:
                           if self.data[self.reticle[1]][self.reticle[0]][1]:
                               self.data[self.reticle[1]][self.reticle[0]][1] = 0
                               self.data[self.cursor[1]][self.cursor[0]][3] = 0
                           else:
                               self.data[self.reticle[1]][self.reticle[0]][1] = 1
                               self.data[self.cursor[1]][self.cursor[0]][3] = 1

                       self.cursor = self.reticle
                       renpy.retain_after_load()
                       renpy.restart_interaction()

        def start_trace(self):
            if self.get_coord():
                self.tracing = True
                self.cursor = self.reticle
                renpy.retain_after_load()
                renpy.restart_interaction()

        def stop_trace(self):
            self.tracing = False
            renpy.retain_after_load()
            renpy.restart_interaction()

        def event(self, ev, x, y, st):
            if ev.type == pygame_sdl2.MOUSEBUTTONDOWN and ev.button is 1:
                self.start_trace()
            elif ev.type == pygame_sdl2.MOUSEBUTTONUP and ev.button is 1:
                self.stop_trace()

        def check_broken(self):
            broken = False
            for y in range(self.h):
                for x in range(self.w):
                    if sum(self.data[y][x]) in [1, 3] or \
                           not all([self.verify_continuity(x, y, x+1, y),
                                    self.verify_continuity(x, y, x-1, y),
                                    self.verify_continuity(x, y, x, y+1),
                                    self.verify_continuity(x, y, x, y-1)]):
                                        broken = True
                                        break
                if broken: break
            return broken

        def verify(self):
            global loop_counter
            invalid = False
            for y in range(self.h):
                for x in range(self.w):
                    if cybernetic_mask[y][x] and sum(self.data[y][x]) in [0, 1, 3]:
                        invalid = True
                        break
                if invalid: break
            if invalid:
                if "dead9" in persistent.dead_ends or not preferences.hard_mode:
                    #cybernetics_reset()
                    renpy.notify(_("Not a valid solution."))
                    #TODO: some kind of error feedback
                    return
                else:
                    renpy.jump("recalibration_game_over")

            checked = []
            next = (0, 0)

            while next:
                next, checked = self.check_trace(checked, next)

            if len(set(checked)) == 74:
                store.room2["recalibration"] = "solved"
                return True

            else:
                tally = set(checked)
                loop_counter += 1
                for y in range(10):
                    for x in range(12):
                        if cybernetic_mask[y][x] and (x, y) not in tally:
                            checked = []
                            next = (x, y)
                            while next:
                                next, checked = self.check_trace(checked, next)
                            tally.update(checked)
                            loop_counter += 1

                if ("dead9" in persistent.dead_ends and not preferences.hard_mode):
                    cybernetics_reset()
                    renpy.restart_interaction()
                    #TODO: some kind of error feedback
                else:
                    renpy.jump("recalibration_game_over")

        def check_trace(self, checked, pos, tally_color=True):
            x, y = pos
            if x < 0 or y < 0:
                return (False, checked)
            first = False
            if not checked:
                frist = True
                checked = [pos]
                d = self.data[y][x]
                if d[0]:
                    pos = (x+1, y)
                    if tally_color:
                        loop_data[y][x][0] = loop_counter
                        loop_data[y][x+1][2] = loop_counter
                elif d[1]:
                    pos = (x, y+1)
                    if tally_color:
                        loop_data[y][x][1] = loop_counter
                        loop_data[y+1][x][3] = loop_counter
                elif d[2]:
                    pos = (x-1, y)
                    if tally_color:
                        loop_data[y][x][2] = loop_counter
                        loop_data[y][x-1][0] = loop_counter
                elif d[3]:
                    pos = (x, y-1)
                    if tally_color:
                        loop_data[y][x][3] = loop_counter
                        loop_data[y-1][x][1] = loop_counter
                x, y = pos
            ox, oy = checked[-1]

            dx = x - ox
            dy = y - oy

            next = None
            if dx:
                if dx == 1 and self.data[y][x][2] and self.data[oy][ox][0]:
                    if self.data[y][x][0]:
                        next = (1, 0)
                elif dx == -1 and self.data[y][x][0] and self.data[oy][ox][2]:
                    if self.data[y][x][2]:
                        next = (-1, 0)
                if not next:
                    if self.data[y][x][1]: next = (0, 1)
                    else: next = (0, -1)
            elif dy:
                if dy == 1 and self.data[y][x][3] and self.data[oy][ox][1]:
                    if self.data[y][x][1]:
                        next = (0, 1)
                elif dy == -1 and self.data[y][x][1] and self.data[oy][ox][3]:
                    if self.data[y][x][3]:
                        next = (0, -1)
                if not next:
                    if self.data[y][x][0]: next = (1, 0)
                    else: next = (-1, 0)

            if tally_color:
                if next[0] == 1:
                    loop_data[y][x+1][2] = loop_counter
                    loop_data[y][x][0] = loop_counter
                elif next[0] == -1:
                    loop_data[y][x-1][0] = loop_counter
                    loop_data[y][x][2] = loop_counter
                elif next[1] == -1:
                    loop_data[y-1][x][1] = loop_counter
                    loop_data[y][x][3] = loop_counter
                elif next[1] == 1:
                    loop_data[y+1][x][3] = loop_counter
                    loop_data[y][x][1] = loop_counter

            checked.append(pos)
            next = ((x+next[0], y+next[1]), checked)
            return (False, checked) if next[0] == checked[0] else next

        def verify_continuity(self, x1, y1, x2, y2):
            if not 0 < x1 < self.w or \
               not 0 < x2 < self.w or \
               not 0 < y1 < self.h or \
               not 0 < y2 < self.h or \
               not cybernetic_mask[y1][x1] or \
               not cybernetic_mask[y2][x2]:
                   return True

            dx = x1 - x2
            dy = y1 - y2
            d1 = self.data[y1][x1]
            d2 = self.data[y2][x2]

            if dx == 1:
                return (d1[2] and d2[0]) or (not d1[2] and not d2[0])
            elif dy == -1:
                return (d1[1] and d2[3]) or (not d1[1] and not d2[3])
            elif dx == -1:
                return (d1[0] and d2[2]) or (not d1[0] and not d2[2])
            elif dy == 1:
                return (d1[3] and d2[1]) or (not d1[3] and not d2[1])
    
    def cybernetics_reset(txt=_("Invalid. Restarting...")):
        store.cyb = Cybernetic()
        store.loop_data = [[[0,0,0,0] for x in range(12)] for y in range(10)]
        store.loop_counter = 1
        renpy.notify(txt)
        renpy.hide_screen("cybernetics")
        renpy.show_screen("cybernetics",cyb)

label init_cybernetics:
    $ cyb = Cybernetic()
    $ loop_data = [[[0,0,0,0] for x in range(12)] for y in range(10)]
    $ loop_counter = 1
    return

screen cybernetics(cyb, interactable=True):
    modal True
    tag puzzle
    layer "puzzles"
    
    frame style "puzzle_frame" padding 0,0,50,40:
        if interactable:
            add cyb
        grid 12 10:
            pos (170, 150)
            for y in range(10):
                for x in range(12):
                    if cybernetic_mask[y][x]:
                        frame:
                            xysize (65, 65)
                            if cyb.data[y][x][0]:
                                add "right_piece":
                                    align (0.5, 0.5)
                                    at colorify(loop_colors[loop_data[y][x][0]])
                            if cyb.data[y][x][1]:
                                add "down_piece":
                                    align (0.5, 0.5)
                                    at colorify(loop_colors[loop_data[y][x][1]])
                            if cyb.data[y][x][2]:
                                add "left_piece":
                                    align (0.5, 0.5)
                                    at colorify(loop_colors[loop_data[y][x][2]])
                            if cyb.data[y][x][3]:
                                add "up_piece":
                                    align (0.5, 0.5)
                                    at colorify(loop_colors[loop_data[y][x][3]])
                            if cyb.tracing and cyb.cursor == (x, y):
                                add "cursor" align (0.5, 0.5)
                            if cybernetic_input[y][x] is not None:
                                add "#ffffff55" xysize (65, 65) align (0.5, 0.5)
                                add "fixed_%s_piece" % Pipe.items[cybernetic_input[y][x]]:
                                    align (0.5, 0.5)
                    else:
                        null

        fixed xysize (710, 800):
            align (1.0, 0.35)
            style_prefix "cybernetics"
            vbox xalign 0.5 spacing 50:
                style_prefix "puzzle_description"
                label _("Instructions")
                text cybernetics_description

        hbox xalign 1.0 yalign 1.0 ysize 100 spacing 20:
            textbutton "RESET" style "confirm_button" action Function(cybernetics_reset, _("Restarting...")) text_color "#fff" sensitive not inspect xalign 0.0 yalign 0.5 at zoomed(0.75)
            textbutton "SUBMIT" style "confirm_button" action If(cyb.check_broken(), false=Function(cyb.verify)) sensitive not inspect xalign 0.5 yalign 0.5
            textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] sensitive not inspect xalign 1.0 yalign 0.5

    if "room2_3" in persistent.solved_puzzles or ("dead9" in persistent.dead_ends and not preferences.hard_mode) or not preferences.hard_mode:
        textbutton "SKIP" style "confirm_button" action [SetDict(room2, "recalibration", "solved"), Return()] pos (40,50)

    if config.developer:
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room2, "recalibration", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("recalibration_game_over")] style "main_menu_button"

style cybernetics_text:
    size 30 justify True

image cursor:
    "reticle"
    linear 0.5 matrixcolor TintMatrix("#FFF")
    linear 0.5 matrixcolor TintMatrix("#30b0ff")
    repeat
