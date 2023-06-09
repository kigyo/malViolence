define puzzle_pieces = ["0", "1", "carat", "uwu"]

init python:
    class PuzzleBoard(Board):
        def __init__(self, width=7, height=7,
                     move_cap=12,
                     piece_limit=4,
                     shuffle_matches=True,
                     show_next=False,
                     level=3,
                     seed=6107,
                     weights=[3, 3, 1, 1]):
            self.move_cap = move_cap
            self.shuffle_matches = shuffle_matches
            self.show_next = show_next
            self.solution = []
            self.seed = seed
            self.weights = weights
            super(PuzzleBoard, self).__init__(width, height, piece_limit)

            self.show_solution = False
            self.player = (-1, -1)
            self.level = level

        def populate_board(self):
            random.seed(self.seed)
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
                    match = random.choices(["0", "1", "carat", "uwu"], weights=self.weights, k=3)
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
            if self.shuffle_matches:
                match = sorted(match)
            # else:
            #     match = match.reverse()
            matched = False
            for i, m in enumerate(self.matches):
                if m.matched or \
                   (self.shuffle_matches and m != match) or \
                   (not self.shuffle_matches and [p.type for p in match] != m.pieces):
                       continue
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
            renpy.retain_after_load()

    def puzzle_board_reset(txt=_("Invalid. Restarting...")):
        # seed = random.randint(0, 88888888)
        # glog("Seed: %s" % seed)
        if difficulty_level == 1:
            store.pb = PuzzleBoard(width=4, height=9, move_cap=12, shuffle_matches=False, weights=[8, 8, 1, 1], seed=6030284)
        elif difficulty_level == 2:
            store.pb = PuzzleBoard(width=6, height=8, move_cap=10, shuffle_matches=False, weights=[5, 5, 1, 1], seed=1487961)
        else:
            store.pb = PuzzleBoard(width=8, height=9, move_cap=17, shuffle_matches=False, weights=[3, 3, 1, 1])
        store.adt = 0.5
        if txt:
            renpy.notify(txt)
            renpy.hide_screen("puzzle_playspace")
            renpy.show_screen("puzzle_playspace",pb)
        store.hacking_level = difficulty_level

screen puzzle_playspace(b, interactable=True):
    sensitive (not inspect and not _menu)
    tag puzzle
    layer "puzzles"
    modal True
    add "#000"

    if difficulty_level != hacking_level:
        timer 0.1 action Function(puzzle_board_reset, None)

    frame style "puzzle_frame" padding 0,0,50,40:
        if pb.just_cleared:
            use animated_board(pb, (665, 150))
        else:
            use board(pb, (665, 150))
        use puzzle_matches(pb)
        if interactable:
            use buttons(pb, (665, 150))
        use reticle(pb, (665, 150))
        use menu
        if pb.just_cleared:
            timer adt action Function(pb.clear_anim)

        fixed xsize 580 xalign 1.0:
            fixed ysize 880:
                vbox spacing 50 yalign 0.5:
                    style_prefix "puzzle_description"
                    null height 50
                    label _("Instructions")
                    text hacking_description

            hbox xfill True yalign 1.0 ysize 100:
                if preferences.puzzle_resets:
                    textbutton "RESET" style "confirm_button" action Function(puzzle_board_reset, _("Restarting...")) xalign 0.0 yalign 0.5 sensitive interactable at zoomed(0.75)
                textbutton "RETURN" style "confirm_button" action [SetVariable("inspect", None), Hide(transition=puzzle_hide)] xalign 1.0 yalign 0.5 sensitive interactable

        if puzzle_cleared("room1_2") or not preferences.hard_mode:
            use skip_button(room1, "hacking", "room1_2", yoffset=50, xalign=1.0)

    if config.developer:
        vbox:
            textbutton _("Skip Puzzle") action [SetDict(room1, "hacking", "solved"), Return()] style "confirm_button"
            textbutton _("Game Over") action [Jump("hacking_game_over")] style "confirm_button"

screen p_match(m):
    hbox:
        for p in m.pieces:
            fixed:
                xysize (80, 80)
                add p:
                    if m.matched:
                        at colorify(colors[p]),found_match
                    else:
                        at colorify(colors[p])
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
                    for m in pb.matches[:8]:
                        use p_match(m)
                if len(pb.matches) > 8:
                    vbox:
                        for m in pb.matches[8:]:
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
