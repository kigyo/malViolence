default persistent.default_width = 6
default persistent.default_height = 6
default persistent.default_reticle_timeout = 0.5
default persistent.default_piece_count = 4

default adt = 50
default cw = 80
default ch = 80

init:
    $ config.keymap['button_select'].append('K_SPACE')

init -1 python:
    import math
    import random
    # TODO: track seeds

    class Enum(object):
        def __init__(self, *items):
            self.items = []
            if type(items[0]) is tuple:
                for i in items:
                    self.items.append(i[0])
                    pairs = items
            else:
                pairs = dict(zip(items, items))
                self.items = items
            for (key, value) in pairs.items():
                self.__setattr__(key, value)

        def copy(self):
            return self.items[:]

        def random(self, num=4):
            # TODO: Num is a bad parameter name.
            return random.choice(self.items[:num])

        def get(self, num=4):
            return self.items[num]

    Pieces = Enum("square", "circle", "diamond", "triangle", "star")
    Dir = Enum("up", "down", "left", "right")
    renpy.store.pieces = Pieces

    def random_match(num=4, input=None):
        if not input:
            return(Pieces.random(num), Pieces.random(num), Pieces.random(num))
        else:
            return(random.choice(input), random.choice(input), random.choice(input))

    class Board(object):
        def __init__(self, width=7, height=7, piece_limit=4):
            self.width = width
            self.height = height
            self.piece_limit = piece_limit

            self.pieces = []

            self.piece_limit = piece_limit
            self.h_buffer = 1
            self.set_reticle(int(self.width/2), self.height-1)

            for y in range(self.height):
                self.pieces.append([])
                for x in range(self.width):
                    self.pieces[y].append(None)

            self.matches = []

            self.populate_board()
            self.populate_matches()

            self.matched = []

            self.last_reticle = None
            self.last_match_index = None
            self.just_cleared = False

            self.match_count = 0
            self.move_count = 0

            # TODO: Move this to reticle once that is implemented.
            self.player = (-1, -1)
        @property
        def square_meter(self):
            return self._square_meter

        @square_meter.setter
        def square_meter(self, value):
            self._square_meter = min(max(value, 0), 100)

        @property
        def circle_meter(self):
            return self._circle_meter

        @circle_meter.setter
        def circle_meter(self, value):
            self._circle_meter = min(max(value, 0), 100)

        @property
        def diamond_meter(self):
            return self._diamond_meter

        @diamond_meter.setter
        def diamond_meter(self, value):
            self._diamond_meter = min(max(value, 0), 100)

        @property
        def triangle_meter(self):
            return self._triangle_meter

        @triangle_meter.setter
        def triangle_meter(self, value):
            self._triangle_meter = min(max(value, 0), 100)

        @property
        def star_meter(self):
            return self._star_meter

        @star_meter.setter
        def star_meter(self, value):
            self._star_meter = min(max(value, 0), 100)

        @property
        def good_mojo_meter(self):
            return self._good_mojo_meter

        @good_mojo_meter.setter
        def good_mojo_meter(self, value):
            self._good_mojo_meter = min(max(value, 0), 100)

        @property
        def bad_mojo_meter(self):
            return self._bad_mojo_meter

        @bad_mojo_meter.setter
        def bad_mojo_meter(self, value):
            self._bad_mojo_meter = min(max(value, 0), 100)

        def populate_board(self):
            for y in range(self.height):
                for x in range(self.width):
                    self.pieces[y][x] = Piece(type_limit=self.piece_limit)

        def populate_matches(self):
            for i in range(3):
                self.matches.append(Match(piece_limit=self.piece_limit))

        def set_reticle(self, x, y):
            # For default reticle.
            # TODO: Add other reticles and also checks for empty boards (so ret doesn't go widly out of exptected bnounds)
            if x == 0: x += self.h_buffer
            elif x == self.width-1: x -= self.h_buffer
            self.reticle = (x, y)
            self.reticle_type = "default"

        def clear_anim(self):
            self.last_reticle = None
            self.last_match_index = None
            self.just_cleared = False
            for y in range(self.height):
                for x in range(self.width):
                    if self.pieces[y][x]:
                        self.pieces[y][x].last = None
                        self.dist = 1

            # TODO: Move this to inheriting classes.
            if isinstance(self, PuzzleBoard):
                win = True
                for y in range(self.height):
                    for x in range(self.width):
                        if self.pieces[y][x]:
                            win = False
                            break
                if win:
                    renpy.jump('solved_room_1_puzzle_2')

                lose = True
                for y in range(self.height):
                    if not lose: break
                    for x in range(self.width-2):
                        if not lose: break
                        match = [self.pieces[y][x],
                                 self.pieces[y][x+1],
                                 self.pieces[y][x+2]]
                        if None in match:
                            continue
                        match = sorted(match)
                        for m in self.matches:
                            if not m.matched and m == match:
                                lose = False
                                break
                if lose:
                    renpy.jump('failed_room_1_puzzle_2')

            elif isinstance(self, ToyBoard):
                win = True
                for y in range(self.height):
                    for x in range(self.width):
                        if self.pieces[y][x] and self.player != (x, y):
                            win = False
                            break
                if win:
                    renpy.jump('solved_room_3_puzzle_2')
                if not self.check_toy_path(self.player):
                    renpy.jump('failed_room_3_puzzle_2')

        def check_toy_path(self, pos, path=None):
            x = pos[0]
            y = pos[1]

            if not 0 <= x < self.width or \
               not 0 <= y < self.height or \
               not self.pieces[y][x] or\
               (path and (x, y) in path):
                   # self.player == (x, y):
                   return False

            if path is not None:
                if (x, y) == self.player: return
                if any([self.pieces[y][x].type == self.pieces[dy][dx].type for (dx, dy) in path]):
                    return False
                else:
                    path.append((x, y))
                    if len(path) >= 4:
                        return True
            else:
                path = []

            return any([self.check_toy_path((x+1, y), path[:]),
                        self.check_toy_path((x-1, y), path[:]),
                        self.check_toy_path((x, y+1), path[:]),
                        self.check_toy_path((x, y-1), path[:])])


        def trigger_reticle(self):
            self.last_reticle = self.reticle
            self.move_count += 1
            x = self.reticle[0]
            match = (self.pieces[self.reticle[1]][x-1],
                     self.pieces[self.reticle[1]][x],
                     self.pieces[self.reticle[1]][x+1])
            match = sorted(match)

            for i, m in enumerate(self.matches):
                if m == match and not m.matched:
                    self.last_match_index = i
                    self.matched.insert(0, m)
                    del self.matches[i]
                    self.matches.insert(0, Match(piece_limit=self.piece_limit))
                    self.match_count += 1
                    renpy.store.race.player.boost()
                    # for p in match:
                    #     setattr(self, p.type +"_meter", getattr(self, p.type+"_meter")+5)
                    # TODO: Do we want to allow mutiple matches on the off chance that comes up? Should we filter matches so there are no dupes in the first place?
                    break
            for p in match:
                setattr(self, p.type +"_meter", getattr(self, p.type+"_meter")+5)
            if self.last_match_index is None:
                self.bad_mojo_meter += 5

            for y in range(self.reticle[1], 0, -1):
                for x in range(self.reticle[0]-1, self.reticle[0]+2):
                    self.pieces[y][x].set_type(self.pieces[y-1][x].type)
            for x in range(self.reticle[0]-1, self.reticle[0]+2):
                self.pieces[0][x].set_type(Pieces.random(self.piece_limit))

            self.just_cleared = True

        def __eq__(self, other):
            return False

    class Reticle(object):
        def __init__(self, x, y, board, reticle_type="default"):
            self.type=reticle_type
            self.x = x
            self.y = y
            self.board = board

        def set_pos(self, x, y):
            pass

    class Match(object):
        def __init__(self, pieces=None, piece_limit=4):
            self.pieces = pieces or random_match(piece_limit)
            self.last = None
            self.matched = False

        def __eq__(self, other):
            if isinstance(other, Match):
                return sorted(other.pieces) == sorted(self.pieces)
            elif isinstance(other, tuple) or isinstance(other, list) and all(other):
                # return sorted(other) == sorted(self.pieces)
                return sorted([p.type for p in other]) == sorted(self.pieces)
            return False

    class Piece(object):
        def __init__(self, type=None, type_limit=4, player=False):
            self.type = type or Pieces.random(type_limit)
            self.last = None
            # self.color = colors[self.type]
            self.color = "#fff"
            self.dist = 0
            self.player = player

        @property
        def img(self):
            return self.type

        def set_type(self, type, dist=0):
            self.last = self.type
            self.type = type
            self.dist = dist

        def __eq__(self, other):
            if isinstance(other, Piece):
                return self.type == other.type
            elif isinstance(other, str):
                return self.type == other
            return False

        def __lt__(self, other):
            if isinstance(other, Piece):
                return self.type < other.type
            elif isinstance(other, str):
                return self.type < other
            return False

        def __gt__(self, other):
            if isinstance(other, Piece):
                return self.type > other.type
            elif isinstance(other, str):
                return self.type > other
            return False

transform next():
    linear adt matrixcolor BrightnessMatrix(0.5)
    linear adt matrixcolor BrightnessMatrix(0.0)
    repeat

transform full_meter():
    linear adt matrixcolor BrightnessMatrix(0.25)
    linear adt matrixcolor BrightnessMatrix(0.0)
    repeat

transform full_bad_mojo_meter():
    linear adt matrixcolor BrightnessMatrix(0.25)*TintMatrix("#ff0000ee")
    linear adt matrixcolor BrightnessMatrix(0.0)*TintMatrix("#ffffff")
    repeat

transform match_slide_in():
    yoffset -85 alpha 0.0
    linear adt yoffset 0 alpha 1.0

transform match_slide_down():
    yoffset -85
    linear adt yoffset 0

transform matched_slide_in(b):
    yoffset ((2-b.last_match_index)*-90)-220
    linear adt yoffset 0

transform matched_slide_down():
    yoffset -85
    linear adt yoffset 0

transform label:
    yoffset -50

# For sucessful match.
transform bop_down():
    pass

# For destroying any pieces.
transform bop_off(x, y):
    pass

# For destroying matched pieces.
transform explode(x, y):
    pass

# For pieces refilling.
transform slide_in(x, y, d=0):
    pos (x*cw, (y-1)*ch)
    alpha 0.0
    pause d
    linear adt pos (x*cw, y*ch) alpha 1.0

# For pieces sliding to refill.
transform slide_down(x, y, d=0, dist=1, dt=adt):
    pos (x*cw, (y-dist)*ch)
    pause d
    linear dt pos (x*cw, y*ch)

transform player_chomp(path, dt, dist, pdt):
    # Path is always 5 long.
    pos (path[0][1][0]*cw, path[0][1][1]*ch)
    linear dt/4 pos (path[1][1][0]*cw, path[1][1][1]*ch)
    linear dt/4 pos (path[2][1][0]*cw, path[2][1][1]*ch)
    linear dt/4 pos (path[3][1][0]*cw, path[3][1][1]*ch)
    linear dt/4 pos (path[4][1][0]*cw, path[4][1][1]*ch)
    linear pdt pos (path[4][1][0]*cw, path[4][1][1]*ch+dist*ch)

transform just_pathed(dt, i):
    alpha 1.0
    pause (dt/4)*(i+1)
    alpha 0.0
    pause 0.0

transform matched():
    on show:
        linear adt matrixcolor im.matrix.saturation(0.5)
    on replace:
        matrixcolor im.matrix.saturation(0.5)

screen animated_board(b, pos=(100, 100)):
    tag board
    use board(b, pos)

screen board(b, pos=(100, 100)):
    tag board
    fixed:
        pos pos
        for y in range(b.height):
            for x in range(b.width):
                if b.pieces[y][x]:
                    use board_piece(b, x, y)
        if b.just_cleared and isinstance(b, ToyBoard):
            for i in range(len(b.just_pathed)):
                $ (p, (cx, cy)) = b.just_pathed[i]
                add p:
                    pos (cx*ch, cy*cw)
                    # at [colorify("#fff"), just_pathed(adt/2, i)]
                    at [just_pathed(adt/2, i)]
                    align (0.5, 0.5)


screen board_piece(b, x, y):
    $ transforms = [colorify(colors[b.pieces[y][x].type])]
    if isinstance(b, PuzzleBoard):
        if b.show_next and b.solution and (b.solution[0][0] == x and b.solution[0][1] == y):
            $ transforms.append(next)
        if b.just_cleared and b.pieces[y][x].last:
            $ transforms.append(slide_down(x, y))
    elif isinstance(b, ToyBoard):
        if b.just_cleared:
            if (x, y) == b.player:
                $ transforms.append(player_chomp([('star', b.last_player)]+b.just_pathed, dt=adt*0.75, dist=b.pieces[y][x].dist, pdt=adt*0.25))
            elif b.pieces[y][x].last:
                $ transforms.append(slide_down(x, y, dist=b.pieces[y][x].dist, dt=adt*0.25, d=adt*0.75))
        elif (x, y) in b.match:
            $ transforms.append(colorify("#ff000055"))
    else:
        if b.just_cleared and b.pieces[y][x].last:
            if y == 0:
                $ transforms.append(slide_in(x, y))
            else:
                $ transforms.append(slide_down(x, y))
    add b.pieces[y][x].img:
        at transforms
        pos (x*ch, y*cw)
        align (0.5, 0.5)
        if isinstance(b, PuzzleBoard):
            xysize (65, 65)

screen piece(p, transforms=None):
    $ transforms = transforms or []
    $ transforms.append(colorify(colors[p]))
    fixed:
        xysize (cw, ch)
        add p at transforms
        align (0.5, 0.5)
        if isinstance(b, PuzzleBoard):
            xysize (65, 65)

screen buttons(b, pos=(100, 100)):
    default h_buffer = b.h_buffer
    if isinstance(b, ToyBoard):
        $ h_buffer = 0
    fixed:
        pos pos
        for y in range(b.height):
            for x in range(max(h_buffer, 1)):
                if b.pieces[y][x]:
                    imagebutton:
                        pos (int(cw*h_buffer/2), y*ch)
                        xysize(cw*(h_buffer+1), ch)
                        anchor (0.5, 0.5)
                        idle Null()
                        # idle "#ff00ff88"
                        if (x, y) == b.player:
                            pass
                        elif not b.just_cleared:
                            action [Function(b.trigger_reticle)]
                        else:
                            action NullAction()
                        hovered Function(b.set_reticle, h_buffer, y)
        for y in range(b.height):
            for x in range(h_buffer+1, b.width-1-h_buffer):
                if b.pieces[y][x]:
                    imagebutton:
                        pos (x*cw, y*ch)
                        xysize(cw, ch)
                        align (0.5, 0.5)
                        idle Null()
                        # idle "#ffffff88"
                        if (x, y) == b.player:
                            pass
                        elif not b.just_cleared:
                            action [Function(b.trigger_reticle)]
                        else:
                            action NullAction()
                        hovered Function(b.set_reticle, x, y)
        for y in range(b.height):
            for x in range(min(b.width-h_buffer, b.width-1), b.width):
                if b.pieces[y][x]:
                    imagebutton:
                        pos (int(b.width*cw-(cw*(h_buffer+1))+(cw*h_buffer)/2), y*ch)
                        xysize(cw*(h_buffer+1), ch)
                        align (0.5, 0.5)
                        idle Null()
                        # idle "#ff00ff88"
                        if (x, y) == b.player:
                            pass
                        elif not b.just_cleared:
                            action [Function(b.trigger_reticle)]
                        else:
                            action NullAction()
                        hovered Function(b.set_reticle, b.width-1-h_buffer, y)

image tint:
    "#000"
    alpha 0.65

transform fade_in():
    alpha 0.0
    linear 0.5 alpha 1.0

screen matches(b):
    fixed:
        pos (830, 100)
        fit_first True
        xanchor 0.5
        use colorized_frame(padding=(10, 10)):
            has vbox
            spacing 10
            for m in b.matches:
                hbox:
                    for p in m.pieces:
                        use piece(p)

screen matched(b):
    fixed:
        pos (830, 500)
        fit_first True
        xanchor 0.5
        use colorized_frame(xysize=(260, 800), padding=(10, 10), xalign=0.5):
            has vbox
            spacing 10
            for m in b.matched:
                hbox:
                    for p in m.pieces:
                        use pieces(p)

screen animated_matches(b):
    fixed:
        pos (830, 100)
        fit_first True
        xanchor 0.5
        use colorized_frame(padding=(10, 10)):
            has vbox
            spacing 10
            for i, m in enumerate(b.matches):
                hbox:
                    if board.last_match_index is not None:
                        if i == 0:
                            at match_slide_in
                        elif i <= board.last_match_index:
                            at match_slide_down
                    for p in m.pieces:
                        use piece(p)

screen matched(b):
    fixed:
        pos (830, 500)
        fit_first True
        xanchor 0.5
        use colorized_frame(xysize=(260, 800), padding=(10, 10), xalign=0.5):
            has vbox
            spacing 10
            for m in b.matched:
                hbox:
                    for p in m.pieces:
                        use piece(p)

screen animated_matched(b):
    fixed:
        pos (830, 500)
        fit_first True
        xanchor 0.5
        use colorized_frame(xysize=(260, 800), padding=(10, 10), xalign=0.5):
            has vbox
            spacing 10
            for i, m in enumerate(b.matched):
                hbox:
                    for p in m.pieces:
                        $ transforms = []
                        if b.last_match_index is not None:
                            if i == 0:
                                $ transforms.append(matched_slide_in(b))
                            else:
                                $ transforms.append(matched_slide_down)
                        use piece(p, transforms)

transform reticle_insensitive:
    linear 0.25 alpha 0.15

transform reticle_idle:
    linear 0.25 alpha 1.0
    block:
        linear 0.65 alpha 0.65
        linear 0.65 alpha 1.0
        repeat

screen reticle(b, pos=(100, 100)):
    default ret = "default"
    if isinstance(b, ToyBoard):
        $ ret = "single"
    if isinstance(b, PuzzleBoard):
        $ ret = "default"
    fixed:
        pos pos
        if b.just_cleared:
            at reticle_insensitive
        else:
            at reticle_idle
        add "reticle_%s" % ret:
            at colorify(colors["reticle"])
            align (0.5, 0.5)
            pos(b.reticle[0]*cw, b.reticle [1]*ch)

default pb = None
default tb = None

label init_puzzle_board():
    $ pb = PuzzleBoard(width=6, height=10, move_cap=12)
    $ adt = 0.5
    return


label init_toy_board():
    $ tb = ToyBoard(width=5, height=5)
    $ adt = persistent.toy_reticle_timeout
    return
