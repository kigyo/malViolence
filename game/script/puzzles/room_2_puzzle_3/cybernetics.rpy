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

label init_cybernetics:
    $ cyb = Cybernetic()
    return

screen cybernetics(cyb, interactables=True):
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
                            add "right_piece" align (0.5, 0.5)
                        if cyb.data[y][x][1]:
                            add "down_piece" align (0.5, 0.5)
                        if cyb.data[y][x][2]:
                            add "left_piece" align (0.5, 0.5)
                        if cyb.data[y][x][3]:
                            add "up_piece" align (0.5, 0.5)
                        if cyb.tracing and cyb.cursor == (x, y):
                            add "cursor" align (0.5, 0.5)
                        if cybernetic_input[y][x] is not None:
                            add "#ffffff55" xysize (65, 65) align (0.5, 0.5)
                            add "fixed_%s_piece" % Pipe.items[cybernetic_input[y][x]]:
                                align (0.5, 0.5)
                else:
                    null
    frame:
        xysize (650, 800)
        align (0.85, 0.35)
        has vbox
        xsize 550
        xalign 0.5
        label "Instructions" xalign 0.5
        text "- Lay down new synthetic nerual pathways, but be mindful of the original peices that cannot be moved!"
        text "- Neural pathways must form one continuous loop and occupy every available space."
        text "- Pathways can cross over themselves, but cannot retreace themselves. At any 4 way intersection, a neuron will always go straight."

        frame:
            xalign 0.5
            ypos 50
            textbutton "Submit" action NullAction()

image cursor:
    "reticle"
    linear 0.5 matrixcolor TintMatrix("#FFF")
    linear 0.5 matrixcolor TintMatrix("#30b0ff")
    repeat
