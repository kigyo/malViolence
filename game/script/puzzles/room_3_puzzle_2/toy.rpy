define toy_pieces = ["toy_1", "toy_2", "toy_3", "toy_4", "toy_5"]

define toys_description = _("""What a mess! You need to clean up all these toys by {color=#fff}sorting them into sets.{/color}

{color=#fff}A set{/color} is made up of {color=#fff}four unique toys.{/color} You can reach toys {color=#fff}by moving up, down, left, or right.{/color} You {color=#fff}can't move diagonally.{/color}

Plot your moves carefully! As the toys shift, they may get harder to reach...""")

image toy_walk_fast:
    "toy_walk_1"
    pause 0.05
    "toy_walk_2"
    pause 0.05
    repeat

image toy_walk_slow:
    "toy_walk_1"
    pause 0.85
    "toy_walk_2"
    pause 0.85
    repeat

init python:
    import random
    class ToyBoard(Board):
        def __init__(self, width=7, height=7,
                     move_cap=12,
                     piece_limit=4,
                     shuffle_matches=True,
                     match_length=4,
                     show_next=False,
                     player=(2, 2),
                     init=[[2, 3, 1, 3, 3],
                           [2, 1, 2, 3, 1],
                           [4, 4, 0, 2, 4],
                           [1, 1, 4, 3, 1],
                           [3, 2, 4, 2, 4]]):
            self.move_cap = move_cap
            self.shuffle_matches = shuffle_matches
            self.show_next = show_next
            self.solution = []
            self.player = player
            self.last_player = self.player
            self.init = init
            super(ToyBoard, self).__init__(width, height, piece_limit)
            self.match_length = match_length
            self.match = []
            self.match_pic = []
            self.just_pathed = []

            self.reticle_type = "single"
            self.h_buffer = 0

        def populate_board(self):
            # [(2, 2), (2, 1), (3, 1), (3, 0), (2, 0)]
            # [(3, 2), (3, 3), (2, 3), (1, 3), (0, 3)]
            # [(1, 3), (1, 2), (0, 2), (0, 1), (0, 0)]

            # [(3, 2), (3, 1), (4, 1), (4, 2)]
            # [(3, 2), (2, 2), (2, 3), (1, 3)]
            # [(1, 2), (1, 1), (1, 0), (0, 0)]
            # [(0, 1), (0, 2), (0, 3), (0, 4)]
            # [(1, 4), (2, 4), (2, 3), (3, 3)]
            # [(3, 4), (4, 4), (4, 3), (4, 2)]

            # [(4, 3), (4, 2), (5, 2), (5, 1), (4, 1)]
            # [(4, 4), (3, 4), (2, 4), (2, 3), (2, 2)]
            # [(1, 4), (1, 3), (1, 2), (2, 2), (2, 3)]
            # [(3, 4), (4, 4), (5, 4), (5, 3), (5, 2)]
            # [(5, 5), (4, 5), (3, 5), (3, 4), (3, 3)]
            # [(2, 5), (1, 5), (0, 5), (0, 4), (0, 3)]
            # [(1, 5), (1, 4), (0, 4), (0, 3), (0, 2)]

            for y in range(self.height):
                for x in range(self.width):
                    p = self.init[y][x]
                    if p:
                        self.pieces[y][x] = Piece(toy_pieces[p-1])

            self.pieces[self.player[1]][self.player[0]] = Piece("toy_walk_slow", player=True)

        def populate_matches(self):
            # Toy makes use of a set match, so this step is skipped.
            return

        def trigger_reticle(self):
            self.last_reticle = self.reticle
            if self.reticle in self.match:
                i = self.match.index(self.reticle)
                self.match = self.match[:i]
                self.match_pic = self.match_pic[:i]
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
            self.match_pic.append(self.pieces[self.match[-1][1]][self.match[-1][0]].type)
            if len(self.match) < self.match_length:
                return
            renpy.sound.play("audio/sfx/new malviolence sfx/plushsqueak.mp3")
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

            self.pieces[self.player[1]][self.player[0]] = Piece("toy_walk_slow")

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
                    if self.pieces[y][x] and self.pieces[y][x].type == "toy_walk_slow":
                        self.player = (x, y)
            self.just_cleared = True

            renpy.retain_after_load()

    def sort_matches(tup):
        lst = len(tup)
        for i in range(0, lst):
            for j in range(0, lst-i-1):
                if (tup[j][1] > tup[j + 1][1]):
                    temp = tup[j]
                    tup[j] = tup[j + 1]
                    tup[j + 1] = temp
        return tup

    def toy_board_reset(txt=_("Invalid. Restarting...")):
        if difficulty_level == 1:
            store.tb = ToyBoard(width=4, height=4, player=(1, 2),
                                match_length=5,
                                init=[[3, 2, 1, 4],
                                      [4, 1, 2, 5],
                                      [5, 0, 3, 1],
                                      [3, 5, 4, 2]])
            store.adt = 1.25
        elif difficulty_level == 2:
            store.tb = ToyBoard(width=5, height=5)
            store.adt = 1.0
        elif difficulty_level == 3:
            store.adt = 1.25
            store.tb = ToyBoard(width=6, height=6,
                                match_length=5,
                                player=(3, 3),
                                init=[[2, 3, 3, 1, 2, 1],
                                      [5, 4, 2, 5, 2, 5],
                                      [1, 1, 1, 5, 1, 3],
                                      [1, 5, 3, 0, 4, 4],
                                      [4, 4, 2, 5, 4, 3],
                                      [2, 5, 3, 2, 4, 3]])

        store.toy_level = difficulty_level

        if txt:
            renpy.notify(txt)
            renpy.hide_screen("toy_playspace")
            renpy.show_screen("toy_playspace",tb)

screen toy_playspace(b=None, interactable=True):
    tag puzzle
    layer "puzzles"
    modal True
    if difficulty_level != toy_level:
        timer 0.1 action Function(toy_board_reset, None)

    frame style "puzzle_frame":
        frame:
            xysize (400, 200)
            align 0.0,0.5
            has vbox
            xfill True
            xalign 0.5
            label "Current Match" xalign 0.5
            null height 35
            if not tb.match_pic:
                pass
                # text "None"
            else:
                hbox:
                    xoffset 30
                    for p in tb.match_pic:
                        add p
        if tb.just_cleared:
            use animated_board(tb, (550, 350))
        else:
            use board(tb, (550, 350))
        if interactable:
            use buttons(tb, (550, 350))
        use reticle(tb, (550, 350))
        if tb.just_cleared:
            timer adt action Function(tb.clear_anim)

        fixed xsize 675 xalign 1.0:
            fixed ysize 880:
                vbox spacing 50 yalign 0.5:
                    style_prefix "puzzle_description"
                    label _("Instructions")
                    text toys_description
            hbox xalign 1.0 yalign 1.0 ysize 100 spacing 20 xfill True:
                if "dead12" in persistent.dead_ends or not preferences.hard_mode:
                    textbutton "RESET" style "confirm_button" action Function(toy_board_reset, _("Restarting...")) text_color "#fff" sensitive not inspect xalign 0.0 yalign 0.5 at zoomed(0.75)
                textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] sensitive not inspect xalign 1.0 yalign 0.5

        if puzzle_cleared("room3_2") or not preferences.hard_mode:
            use skip_button(room3, "toys", "room3_2", xalign=1.0)

    if config.developer:
        vbox:
            textbutton _("Skip Puzzle") action [SetDict(room3, "toys", "solved"), Return()] style "confirm_button"
            textbutton _("Game Over") action [Jump("toys_game_over")] style "confirm_button"

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
                for m in tb.matches[:6]:
                    use match(m)
            if len(tb.matches) > 6:
                vbox:
                    for m in tb.matches[6:]:
                        use match(m)

transform found_match:
    alpha 0.45

label toy_mode:
    $ tb = ToyBoard(width=persistent.toy_width, height=persistent.toy_height, \
                       piece_limit=persistent.toy_piece_count, \
                       move_cap=persistent.toy_move_cap, \
                       shuffle_matches=persistent.toy_shuffle_matches, \
                       show_next=persistent.toy_show_solution)
    $ adt = 1.0
    call screen toy_playspace(tb)
    return
