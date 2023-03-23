init python:
    import random
    class ToyBoard(Board):
        def __init__(self, width=7, height=7,
                     move_cap=12,
                     piece_limit=4,
                     shuffle_matches=True,
                     show_next=False):
            self.move_cap = move_cap
            self.shuffle_matches = shuffle_matches
            self.show_next = show_next
            self.solution = []
            super(ToyBoard, self).__init__(width, height, piece_limit)

            self.match = []
            self.just_pathed = []
            self.player = (2, 2)
            self.last_player = (2, 2)

            self.reticle_type = "single"
            self.h_buffer = 0

        def populate_board(self):
            # player = (random.randrange(1, self.width-1), random.randrange(self.height))


            # CRITICAL : [(3, 2), (3, 1), (4, 1), (4, 2)]
            # CRITICAL : [(3, 2), (2, 2), (2, 3), (1, 3)]
            # CRITICAL : [(1, 2), (1, 1), (1, 0), (0, 0)]
            # CRITICAL : [(0, 1), (0, 2), (0, 3), (0, 4)]
            # CRITICAL : [(1, 4), (2, 4), (2, 3), (3, 3)]
            # CRITICAL : [(3, 4), (4, 4), (4, 3), (4, 2)]

            init = [[2, 3, 1, 3, 3],
                    [2, 1, 2, 3, 1],
                    [4, 4, 0, 2, 4],
                    [1, 1, 4, 3, 1],
                    [3, 2, 4, 2, 4]]

            for y in range(self.height):
                for x in range(0, self.width):
                    p = init[y][x]
                    if p:
                        self.pieces[y][x] = Piece(Pieces.get(p-1))

            self.player = (2, 2)
            self.pieces[self.player[1]][self.player[0]] = Piece("star", player=True)

        def populate_matches(self):
            # Toy makes use of a set match, so this step is skipped.
            return

        def trigger_reticle(self):
            self.last_reticle = self.reticle
            if self.reticle in self.match:
                i = self.match.index(self.reticle)
                self.match = self.match [:i]
                return

            if not self.match:
                if not((-1 <= self.player[0] - self.reticle[0] <= 1 and \
                        self.player[1] == self.reticle[1]) or \
                       (-1 <= self.player[1] - self.reticle[1] <= 1 and \
                        self.player[0] == self.reticle[0])):
                            return
            else:
                if not((-1 <= self.match[-1][0] - self.reticle[0] <= 1 and \
                        self.match[-1][1] == self.reticle[1]) or \
                       (-1 <= self.match[-1][1] - self.reticle[1] <= 1 and \
                        self.match[-1][0] == self.reticle[0])):
                            return
                elif self.pieces[self.reticle[1]][self.reticle[0]].type in [self.pieces[m[1]][m[0]] for m in self.match]:
                    return
            self.match.append(self.reticle)

            if len(self.match) < 4:
                return

            self.just_pathed = [(self.pieces[y][x].type, (x, y)) for (x, y) in self.match]

            self.pieces[self.player[1]][self.player[0]] = None
            self.last_player = self.player
            self.player = self.match[-1]
            # matches = sort_matches(self.match)
            matches = self.match

            for m in matches:
                x = m[0]
                y = m[1]
                self.pieces[y][x] = None

            self.pieces[self.player[1]][self.player[0]] = Piece("star")

            for x in range(self.width):
                for uy in range(self.height-2, -1, -1):
                    if self.pieces[uy][x] and not self.pieces[uy+1][x]:
                        ty = uy+1
                        while ty < self.height:
                            if self.pieces[ty][x]:
                                ty -= 1
                                break
                            else:
                                ty += 1
                        ty = min(ty, self.height-1)

                        self.pieces[ty][x] = Piece("")
                        self.pieces[ty][x].set_type(self.pieces[uy][x].type, dist=ty-uy)
                        self.pieces[uy][x] = None

            for y in range(self.height):
                for x in range(self.width):
                    if self.pieces[y][x] and self.pieces[y][x].type == "star":
                        self.player = (x, y)

            self.match = []

            self.just_cleared = True

    def sort_matches(tup):
        lst = len(tup)
        for i in range(0, lst):
            for j in range(0, lst-i-1):
                if (tup[j][1] > tup[j + 1][1]):
                    temp = tup[j]
                    tup[j] = tup[j + 1]
                    tup[j + 1] = temp
        return tup

screen toy_playspace(b, interactable=True):
    add "#ffffff" at colorify(colors["background"])
    if b.just_cleared:
        use animated_board(b)
    else:
        use board(b)
    use toy_matches(b)
    if interactable:
        use buttons(b)
    use reticle(b)
    use menu
    if b.just_cleared:
        timer adt action Function(b.clear_anim)

screen match(m):
    hbox:
        for p in m.pieces:
            fixed:
                xysize (80, 80)
                $ transforms = [colorify(colors[p])]
                if m.matched:
                    $ transforms.append(found_match)
                add p at transforms

screen toy_matches(b):
    fixed:
        pos (700, 100)
        fit_first True
        use colorized_frame(padding=(10, 10)):
            has hbox
            spacing 50
            vbox:
                spacing 10
                for m in b.matches[:6]:
                    use match(m)
            if len(b.matches) > 6:
                vbox:
                    for m in b.matches[6:]:
                        use match(m)

transform found_match:
    alpha 0.45

label toy_mode:
    $ tb = ToyBoard(width=persistent.toy_width, height=persistent.toy_height, \
                       piece_limit=persistent.toy_piece_count, \
                       move_cap=persistent.toy_move_cap, \
                       shuffle_matches=persistent.toy_shuffle_matches, \
                       show_next=persistent.toy_show_solution)
    $ adt = persistent.toy_reticle_timeout
    call screen toy_playspace(tb)
    return
