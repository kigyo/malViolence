define puzzle_pieces = ["0", "1", "carat", "uwu"]

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
            seed = random.randint(0, 8000)
            seed = 7637
            # glog("Seed: %s" % seed)
            random.seed(seed)
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
                    # match = random_match(self.piece_limit, puzzle_pieces)
                    # match = random.choices(["0, 1, carat, uwu"], cum_weights=[35, 35, 15, 15], k=3)
                    match = random.choices(["0", "1", "carat", "uwu"], weights=[8, 8, 1, 1], k=3)
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
    add "#000"
    if b.just_cleared:
        use animated_board(b, (735, 150))
    else:
        use board(b, (735, 150))
    use puzzle_matches(b)
    if interactable:
        use buttons(b, (735, 150))
    use reticle(b, (735, 150))
    use menu
    if b.just_cleared:
        timer adt action Function(b.clear_anim)

    use colorized_frame(padding=(10, 10), xysize=(600, 800), pos=(1258, 100), background="#000", accent="#fff"):
        has vbox
        xalign 0.5
        spacing 20
        style_prefix "cybernetics"
        label "Instructions" text_color "#fff" xalign 0.5
        # text "    Cautionne has obtained a list of security codes for a STOP medical facility and plans to use them to sabotage the cybernetic update proceedure of a top official."
        text "    Using the given list of codes, break into the system, but be careful! Codes are only half the hack. They need to be used at the correct time and place otherwise you may end up locking yourself out of the system."
        text "    Use the mouse or keybaord to clear out codes as you see them in the system, but be aware of how clearing out codes rearranges the system and changes what codes will be available for you afterwards."
        text "    ALL the codes must be used to fully clear the fire wall and sucessfully break into the system."
        text "    Codes are unodered, so long as the three individual components are the same, the codes count as the same."


screen p_match(m):
    hbox:
        for p in m.pieces:
            fixed:
                xysize (80, 80)
                $ transforms = [colorify(colors[p])]
                if m.matched:
                    $ transforms.append(found_match)
                add p at transforms:
                    xysize (65, 65)

screen puzzle_matches(b):
    fixed:
        pos (50, 100)
        fit_first True
        use colorized_frame(accent="#fff", background="#000"):
            has vbox
            label "Codes" text_color "#fff" xalign 0.5
            null height 24
            hbox:
                spacing 50
                vbox:
                    spacing 10
                    for m in b.matches[:8]:
                        use p_match(m)
                if len(b.matches) > 8:
                    vbox:
                        for m in b.matches[8:]:
                            use p_match(m)

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
