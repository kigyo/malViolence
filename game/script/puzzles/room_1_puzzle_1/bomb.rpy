define block_size = 80
default bomb = None
define offset_x = 715
define offset_y = 200
define bomb_mask = [[0, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1]]


# TODO center bound

init python:
    class Bomb(object):
        def __init__(self, x, y, parts, block_size=block_size, ox=offset_x, oy=offset_y):
            self.group = DragGroup()
            self.parts = parts
            for p in self.parts: p.set_group(self.group)
            self.x = x
            self.y = y
            self.ox = ox
            self.oy = oy
            self.block_size = block_size
            self.board = []
            self.data = []
            for y in range(self.y):
                self.board.append([])
                self.data.append([])
                for x in range(self.x):
                    self.data[y].append(0)
                    if bomb_mask[y][x]:
                        self.board[y].append(Drag(Fixed("#fff",
                                                        Fixed("#000", xysize=(self.block_size-2, self.block_size-2), align=(0.5, 0.5)),
                                                        xysize=(self.block_size, self.block_size)),
                                                  pos=(self.ox+x*self.block_size, self.oy+y*self.block_size),
                                                  draggable=False,
                                                  drag_name=(x, y)))
                        self.group.add(self.board[y][x])
                    else:
                        self.board[y].append(None)


    default_shape = [[1, 1],
                     [0, 1]]

    class Part(object):
        def __init__(self,
                     img="default_part",
                     shape=None,
                     x=600, y=400):

            self.shape = shape or [row[:] for row in default_shape]
            self.rotation = 0
            self.x = x
            self.y = y
            self.bench_x = x
            self.bench_y = y
            self.img = img
            self.last_filled = []
            # self.board = PartBoard(2, 3)

            self.handles = [[None for x in range(len(self.shape[0]))] for y in range(len(self.shape))]

            for y in range(len(self.shape)):
                for x in range(len(self.shape[0])):
                    if self.shape[y][x] > 0:
                        self.handles[y][x] = Drag('handle',
                                                  pos=(self.x+x*block_size, self.y+y*block_size),
                                                  droppable=False,
                                                  drag_name=(self.bench_x, self.bench_y),
                                                  drag_joined=self.joined,
                                                  dragged=renpy.curry(dragged)(self),
                                                  dragging=renpy.curry(dragging)(self),
                                                  activated=activated,
                                                  clicked=self.rotate,
                                                  alternate=renpy.curry(self.rotate)(False),
                                                  mouse_drop=True,
                                                  drag_offscreen=True)
            self.display = Drag(Transform(self.img, rotate_pad=False),
                                pos=(self.x, self.y),
                                drag_name=(self.bench_x, self.bench_y),
                                draggable=False,
                                droppable=False,
                                dragged=renpy.curry(dragged)(self),
                                dragging=renpy.curry(dragging)(self),
                                activated=activated,
                                drag_joined=self.joined,
                                drag_handle=(0,0,0,0),
                                clicked=self.rotate,
                                alternate=renpy.curry(self.rotate)(False),
                                drag_offscreen=True)

        def joined(self, drag):
            ret = [(self.display, 0, 0)]
            for y in range(len(self.shape)):
                for x in range(len(self.shape[0])):
                    if self.shape[y][x] > 0:
                        ret.append((self.handles[y][x], x*block_size, y*block_size))
            # ret =  [d for d in ret if d[0] == drag] + [d for d in ret if d[0] != drag]
            for t in ret:
                if t[0] == drag:
                    t[0].handle = True
                elif t[0]:
                    t[0].handle = False
            return ret

        def rotate(self, cw=True):
            if cw:
                self.rotation += 1
                self.rotation = 0 if self.rotation == 4 else self.rotation
                self.shape = list(zip(*self.shape[::-1]))
                self.handles = list(map(list, list(zip(*self.handles[::-1]))))
            else:
                self.rotation -= 1
                self.rotation = 3 if self.rotation == -1 else self.rotation
                self.shape = list(zip(*self.shape[::-1]))
                self.handles = list(map(list, list(zip(*self.handles[::-1]))))
                self.shape = list(zip(*self.shape[::-1]))
                self.handles = list(map(list, list(zip(*self.handles[::-1]))))
                self.shape = list(zip(*self.shape[::-1]))
                self.handles = list(map(list, list(zip(*self.handles[::-1]))))
            for y in range(len(self.handles)):
                for x in range(len(self.handles[y])):
                    if self.handles[y][x]:
                        self.handles[y][x].snap(self.display.x+x*block_size, self.display.y+y*block_size, 0.0)
            self.display.child.rotate = self.rotation*90
            self.display.child.update()
            self.display.child.update()
            self.display.child.update()
            self.display.snap(self.display.x, self.display.y, 0.0)
            renpy.retain_after_load()
            renpy.restart_interaction()

        def tidy(self, drags, drops):
            drag = drags[0]
            self.snap(drag, drag.x, drag.y)

        def snap(self, arg=None, x=None, y=None):
            x = x or self.bench_x
            y = y or self.bench_y
            arg.snap(x, y, 0.25)

        def __eq__(self, other):
            return False

        def set_group(self, g):
            g.add(self.display)
            for d in [d for row in self.handles for d in row if d is not None]:
                g.add(d)


    def dragged(part, drags, drop):
        if drop:
            drag = drags[0]
            if drag == part.display:
                mx, my = renpy.get_mouse_pos()
                offx, offy = (int(math.floor((mx-drag.x)/block_size)),
                              int(math.floor((my-drag.y)/block_size)))
                for py in range(len(part.handles)):
                    for px in range(len(part.handles[py])):
                        if part.handles[py][px]:
                            part.handles[py][px].handle = (px, py) == (offx, offy)
            x, y = drop.drag_name
            handle = [d for d in drags if d and d.handle][0]
            for py in range(len(part.handles)):
                for px in range(len(part.handles[py])):
                    if part.handles[py][px] and part.handles[py][px].handle:
                        ox, oy = (px, py)
                        break
            filled = []
            for py in range(len(part.handles)):
                for px in range(len(part.handles[py])):
                    if part.handles[py][px]:
                        pox, poy = (x+px-ox, y+py-oy)
                        if not 0 <= pox < len(bomb_mask[0]) or \
                           not 0 <= poy < len(bomb_mask) or \
                           not bomb_mask[y][x]:
                               return
                        filled.append((pox, poy))
            for (fx, fy) in filled:
                bomb.data[fy][fx] += 1
            part.last_filled = filled
            for py in range(len(part.handles)):
                for px in range(len(part.handles[py])):
                    if part.handles[py][px]:
                        part.handles[py][px].snap(bomb.ox+x*block_size+px*block_size-ox*block_size,
                                                  bomb.oy+y*block_size+py*block_size-oy*block_size, 0.25)
            part.display.snap(bomb.ox+x*block_size-ox*block_size,
                              bomb.oy+y*block_size-oy*block_size, 0.25)
        renpy.retain_after_load()
        renpy.restart_interaction()

    def dragging(part, drags):
        # TODO: Stretch goal to add snap on dragging.
        if part.last_filled:
            for (x, y) in part.last_filled:
                bomb.data[y][x] -= 1
            part.last_filled = []
            renpy.retain_after_load()
            renpy.restart_interaction()

    def activated(drags):
        pass

# label main_menu:
#     jump test_puzzles

label start_bomb:
    $ p = Part()
    $ bomb = Bomb(len(bomb_mask[0]), len(bomb_mask), [p])

    call screen bomb(bomb)
    # call screen piece_puzzle(puzzle_2)

screen bomb(b):
    fixed:
        add b.group
        add "bomb_borders" pos (b.ox-5, b.oy-5)
        fixed:
            pos (b.ox, b.oy)
            for y in range(len(b.data)):
                for x in range(len(b.data[0])):
                    if b.data[y][x] == 1:
                        add "#ffffff55" xysize (block_size, block_size) pos (x*block_size, y*block_size)
                    elif b.data[y][x] > 1:
                        add "#ff000088" xysize (block_size, block_size) pos (x*block_size, y*block_size)
    frame:
        align (0.5, 0.85)
        xysize (500, 200)
        vbox:
            xalign 0.5
            label "Instructions" xalign 0.5
            text "- Fit all the bomb pieces into the bomb casing -- be mindful of the interior"
