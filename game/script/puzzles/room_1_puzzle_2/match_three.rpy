init python:
    class MatchThreeBoard(Board):
        # def __init__(self, width=7, height=7,
        #              piece_limit=4):
        #     super(MatchThreeBoard, self).__init__(width, height, piece_limit)

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
