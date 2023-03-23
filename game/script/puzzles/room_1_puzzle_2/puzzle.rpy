init python:
    class PuzzleBoard(Board):
        def __init__(self, width=7, height=7,
                     move_cap=12,
                     piece_limit=4,
                     shuffle_matches=True,
                     show_next=False):
            self.move_cap = move_cap
            self.shuffle_matches = shuffle_matches
            self.show_next = show_next
            self.solution = []
            super(PuzzleBoard, self).__init__(width, height, piece_limit)

            self.show_solution = False
            self.player = (-1, -1)

        def populate_board(self):
            # NOTE: For normal reticle only.
            moves = 0
            heights = []
            for x in range(self.width):
                heights.append(0)
            possible_positions = []
            for i in range(1, self.width-1):
                possible_positions.append(i)
            while (not self.move_cap or moves < self.move_cap) and possible_positions:
                pos = random.choice(possible_positions)
                local_heights = heights[pos-1:pos+2]
                if max(local_heights) < self.height:
                    match = random_match(self.piece_limit)
                    pieces = [Piece(m) for m in match]
                    y = self.height-1-random.randint(0, min(local_heights))
                    for ny in range(0, y+1):
                        for nx in range(pos-1, pos+2):
                            if self.pieces[ny][nx]:
                                self.pieces[ny-1][nx] = self.pieces[ny][nx]
                    for x in range(pos-1, pos+2):
                        self.pieces[y][x] = pieces.pop(0)
                        heights[x] += 1
                    moves += 1
                    self.solution.insert(0, (pos, y))
                    if self.shuffle_matches:
                        match = list(match)
                        random.shuffle(list(match))
                        match = tuple(match)
                    self.matches.append(Match(match))

                else:
                    possible_positions.remove(pos)

        def populate_matches(self):
            # Puzzle mode generates matches and board at the same time
            # so we skip this step.
            return

        def trigger_reticle(self):
            if self.show_next and self.reticle != self.solution[0]: return
            self.last_reticle = self.reticle
            x = self.reticle[0]
            match = (self.pieces[self.reticle[1]][x-1],
                     self.pieces[self.reticle[1]][x],
                     self.pieces[self.reticle[1]][x+1])
            match = sorted(match)
            matched = False
            for i, m in enumerate(self.matches):
                if m == match and not m.matched:
                    if self.show_next:
                        self.solution.pop(0)
                    m.matched = True
                    matched = True
                    # Only allow one match at a time.
                    break

            if not matched: return

            for y in range(self.reticle[1], -1, -1):
                for x in range(self.reticle[0]-1, self.reticle[0]+2):
                    if self.pieces[y][x]:
                        if self.pieces[y-1][x]:
                            self.pieces[y][x].set_type(self.pieces[y-1][x].type)
                        else:
                            self.pieces[y][x] = None

            for x in range(self.reticle[0]-1, self.reticle[0]+2):
                if self.pieces[0][x]:
                    self.pieces[0][x] = None

            self.just_cleared = True

screen puzzle_playspace(b, interactable=True):
    add "#ffffff" at colorify(colors["background"])
    if b.just_cleared:
        use animated_board(b)
    else:
        use board(b)
    use puzzle_matches(b)
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

screen puzzle_matches(b):
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

label puzzle_mode:
    $ pb = PuzzleBoard(width=persistent.puzzle_width, height=persistent.puzzle_height, \
                       piece_limit=persistent.puzzle_piece_count, \
                       move_cap=persistent.puzzle_move_cap, \
                       shuffle_matches=persistent.puzzle_shuffle_matches, \
                       show_next=persistent.puzzle_show_solution)
    $ adt = persistent.puzzle_reticle_timeout
    call screen puzzle_playspace(pb)
    return
